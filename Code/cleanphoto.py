import os
from PIL import Image, ImageTk
from PIL.ExifTags import TAGS
import shutil
from datetime import datetime
import locale
from tkinter import filedialog, StringVar, IntVar, messagebox
from threading import Thread, Event
from queue import Queue
from ttkbootstrap import Style
from ttkbootstrap.widgets import Radiobutton, Button, Label, Entry, Frame, Progressbar
import sys
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

Save_statut = False

try:
    locale.setlocale(locale.LC_TIME, 'fr_FR')
except:
    print("Erreur lors du passage de la langue : Français")

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":
                    return value
    except Exception as e:
        print(f"Erreur lors de la lecture des métadonnées pour {image_path}: {e}")
    return None

def get_video_creation_date(video_path):
    try:
        parser = createParser(video_path)
        if not parser:
            raise ValueError(f"Impossible de parser le fichier {video_path}")
        
        metadata = extractMetadata(parser)
        if metadata and metadata.has("creation_date"):
            return metadata.get("creation_date").strftime("%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Erreur lors de la lecture des métadonnées vidéo pour {video_path}: {e}")
    return None

def organize_photos(source_dir, destination_dir, action_without_date, progress_var, status_queue, action_month):
    total_files = sum(len(files) for _, _, files in os.walk(source_dir))
    processed_files = 0

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    copied_files = []

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)

            

            if cancel_event.is_set():
                # for copied_file in copied_files:
                #     try:
                #         os.remove(copied_file)
                #     except Exception as e:
                #         status_queue.put(f"Erreur lors de la suppression : {copied_file}: {e}")
                status_queue.put("Organisation annulée.")
                reset_progress()
                status_queue.put("Organisation annulée.")
                toggle_buttons(organizing=False)
                return


            pause_event.wait()

            try:
                if file.lower().endswith(('jpg', 'jpeg', 'png', 'mp4', 'avi', 'mov')):
                    if file.lower().endswith(('mp4', 'avi', 'mov')):  
                        date_str = get_video_creation_date(file_path)
                    else:  
                        date_str = get_exif_data(file_path)
                    
                    if date_str:
                        date_obj = datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
                        year = date_obj.strftime("%Y")
                        month = date_obj.strftime("%B").capitalize() if action_month == 1 else date_obj.strftime("%m")

                        target_dir = os.path.join(destination_dir, year, month)
                        os.makedirs(target_dir, exist_ok=True)
                        dest_path = shutil.copy2(file_path, target_dir)
                        copied_files.append(dest_path)
                        status_queue.put(f"Copié : {file}")
                    else:
                        if action_without_date == 1:
                            status_queue.put(f"Fichier non daté : {file}")
                        elif action_without_date == 2:
                            target_dir = os.path.join(destination_dir, "Autre")
                            os.makedirs(target_dir, exist_ok=True)
                            dest_path = shutil.copy2(file_path, target_dir)
                            copied_files.append(dest_path)
                            status_queue.put(f"Classé dans 'Autre' : {file}")
                processed_files += 1
                progress_var.set((processed_files / total_files) * 100)
            except Exception as e:
                status_queue.put(f"Erreur pour {file}: {e}")
    status_queue.put("Organisation terminée !")
    reset_progress()
    toggle_buttons(organizing=False)

def start_organization_thread():
    if not source_dir_var.get() or not destination_dir_var.get():
        status_label.config(text="Veuillez sélectionner les dossiers source et destination.")
        return

    cancel_event.clear()

    status_queue.queue.clear()
    thread = Thread(
        target=organize_photos,
        args=(
            source_dir_var.get(),
            destination_dir_var.get(),
            action_var.get(),
            progress_var,
            status_queue,
            action_var2.get(),
        ),
    )
    thread.start()
    toggle_buttons(organizing=True)
    app.after(100, process_queue)


def toggle_buttons(organizing):
    global Save_statut
    if organizing:
        Save_statut = True
        organize_button.grid_remove()
        pause_button.grid(row=7, column=0, padx=10)
        cancel_button.grid(row=7, column=1, padx=10)
    else:
        Save_statut = False
        pause_button.grid_remove()
        cancel_button.grid_remove()
        organize_button.grid(row=7, column=0, columnspan=3, pady=30)

def pause_resume():
    if pause_event.is_set():
        print("activer")
        pause_event.clear()
        pause_button.config(text="Reprendre")
    else:
        print("desactiver")
        pause_event.set()
        pause_button.config(text="Pause")


def cancel_organization():
    pause_event.set()
    cancel_event.set()
    toggle_buttons(organizing=False)
    reset_progress()

def reset_progress():
    progress_var.set(0)
    progress_label.config(text="0%")

def process_queue():
    while not status_queue.empty():
        message = status_queue.get()
        status_label.config(text=message)
    app.after(100, process_queue)

def select_directory(var):
    directory = filedialog.askdirectory()
    if directory:
        var.set(directory)


app = Style(theme="flatly").master
app.title("CleanPhoto 1.0.1")

app_width, app_height = 800, 450
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_coordinate = (screen_width // 2) - (app_width // 2)
y_coordinate = (screen_height // 2) - (app_height // 2)
app.geometry(f"{app_width}x{app_height}+{x_coordinate}+{y_coordinate}")
app.resizable(False, False)


source_dir_var = StringVar()
default_destination = os.path.join(os.getcwd(), "Tri")
destination_dir_var = StringVar(value=default_destination)
action_var = IntVar(value=2)
action_var2 = IntVar(value=1)
progress_var = IntVar(value=0)
status_queue = Queue()
pause_event = Event()
cancel_event = Event()
pause_event.set()

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

logo_frame = Label(app)
logo_img = Image.open(resource_path("logo.png"))
logo_img = logo_img.resize((80, 80), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
app.iconphoto(True, logo_photo)

def on_closing():
    if Save_statut != True:
        if messagebox.askokcancel("Quitter", "Êtes-vous sûr de vouloir quitter ?"):
            pause_event.set()
            app.destroy() 
            os._exit(0)
    else:
        if messagebox.askokcancel("Sauvegarde en cours !", "La sauvegarde sera brutalement interrompue."):
            pause_event.set()
            app.destroy()       
            os._exit(0)


app.protocol("WM_DELETE_WINDOW", on_closing)


main_frame = Frame(app, padding=20)
main_frame.pack(fill="both", expand=True)

Label(main_frame, text="CleanPhoto Tool", font="-size 20 -weight bold").grid(row=0, column=0, columnspan=3, pady=10)

Label(main_frame, text="Dossier source :", anchor="w").grid(row=1, column=0, padx=10, pady=10, sticky="e")
Entry(main_frame, textvariable=source_dir_var, width=80).grid(row=1, column=1, padx=10)
Button(main_frame, text="Sélectionner", command=lambda: select_directory(source_dir_var), bootstyle="primary").grid(row=1, column=2, padx=10)

Label(main_frame, text="Dossier destination :", anchor="w").grid(row=2, column=0, padx=10, pady=10, sticky="e")
Entry(main_frame, textvariable=destination_dir_var, width=80).grid(row=2, column=1, padx=10)
Button(main_frame, text="Sélectionner", command=lambda: select_directory(destination_dir_var), bootstyle="primary").grid(row=2, column=2, padx=10)



Label(main_frame, text="Photos sans date :", anchor="w").grid(row=3, column=0, padx=10, pady=10, sticky="e")
Radiobutton(main_frame, text="Ne rien faire", variable=action_var, value=1, bootstyle="info").grid(row=3, column=1, sticky="w")
Radiobutton(main_frame, text="Ranger dans 'Autre'", variable=action_var, value=2, bootstyle="info").grid(row=3, column=1, sticky="w", padx=200)


Label(main_frame, text="Format des mois :", anchor="w").grid(row=4, column=0, padx=10, pady=10, sticky="e")
Radiobutton(main_frame, text="Janvier, Février, Mars", variable=action_var2, value=1, bootstyle="success").grid(row=4, column=1, sticky="w")
Radiobutton(main_frame, text="01, 02, 03", variable=action_var2, value=2, bootstyle="success").grid(row=4, column=1, sticky="w", padx=200)



progress_frame = Frame(main_frame, relief="solid", borderwidth=0, padding=1)
progress_frame.grid(row=5, column=0, columnspan=2, pady=20, sticky="e")

progress_bar = Progressbar(progress_frame, variable=progress_var, length=580, bootstyle="info-striped")
progress_bar.pack(fill="x", expand=True, padx=2, pady=2)

progress_label = Label(main_frame, text="0%", font="-size 10", anchor="w")
progress_label.grid(row=5, column=2, padx=0)

def update_progress_label(*args):
    progress_label.config(text=f"{progress_var.get()}%")

progress_var.trace_add("write", update_progress_label)

status_label = Label(main_frame, text="Remplissez vos choix et commencez le tri !", font="-size 12", relief="flat", anchor="center")
status_label.grid(row=6, column=0, columnspan=3, pady=10, sticky="we")


organize_button = Button(main_frame, text="Organiser", command=start_organization_thread, bootstyle="success-outline", width=20, padding=10)
pause_button = Button(main_frame, text="Pause", command=pause_resume, bootstyle="warning-outline", width=15, padding=10)
cancel_button = Button(main_frame, text="Annuler", command=cancel_organization, bootstyle="danger-outline", width=15, padding=10)

organize_button.grid(row=7, column=0, columnspan=3, pady=30)
pause_button.grid(row=7, column=0, columnspan=2)
cancel_button.grid(row=7, column=0, columnspan=4)

pause_button.grid_remove()
cancel_button.grid_remove()

app.mainloop()
