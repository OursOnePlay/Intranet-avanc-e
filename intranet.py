import tkinter as tk
import requests
import datetime
import json
from tkinter import simpledialog
from tkinter import messagebox
import os
import webbrowser

window = tk.Tk()
window.title("Intranet")
window.config(bg="skyblue")

left_frame = tk.Frame(window, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

right_frame = tk.Frame(window, width=400, height=400)
right_frame.grid(row=0, column=1, padx=10, pady=5)

user_name = tk.StringVar()
user_name.set("Utilisateur")

def save_name():
    with open("user.json", "w") as f:
        json.dump(user_name.get(), f)

def load_name():
    try:
        with open("user.json", "r") as f:
            name = json.load(f)
            user_name.set(name)
    except FileNotFoundError:
        pass

load_name()

welcome_text = tk.Label(left_frame, text="Bienvenue sur l'intranet", font=("Arial", 20))
welcome_text.pack()

user_text = tk.Label(left_frame, textvariable=user_name, font=("Arial", 16))
user_text.pack()

time_text = tk.Label(left_frame, text="Il est " + datetime.datetime.now().strftime("%H:%M:%S"), font=("Arial", 16))
time_text.pack()

greet_text = tk.Label(left_frame, font=("Arial", 16))
greet_text.pack()

shortcuts_text = tk.Label(left_frame, text="Voici quelques raccourcis utiles:", font=("Arial", 16))
shortcuts_text.pack()

add_button = tk.Button(left_frame, text="Ajouter un raccourci", command=lambda: add_shortcut())
add_button.pack()

delete_button = tk.Button(left_frame, text="Supprimer un raccourci", command=lambda: delete_shortcut())
delete_button.pack()

change_button = tk.Button(left_frame, text="Changer le nom de l'utilisateur", command=lambda: change_name())
user_name.trace("w", lambda *args: save_name())
change_button.pack()

try:
    with open("shortcuts.json", "r") as f:
        shortcuts = json.load(f)
except FileNotFoundError:
    shortcuts = {}

for name, path in shortcuts.items():
    shortcut_button = tk.Button(left_frame, text=name, command=lambda p=path: open_shortcut(p))
    shortcut_button.pack()

def add_shortcut():
    user_input = simpledialog.askstring("Ajouter un raccourci", "Entrez le nom et le chemin du raccourci séparés par une virgule")
    try:
        name, path = user_input.split(",")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une virgule entre le nom et le chemin du raccourci")
        return add_shortcut()
    shortcuts[name] = path
    with open("shortcuts.json", "w") as f:
        json.dump(shortcuts, f)
    shortcut_button = tk.Button(left_frame, text=name, command=lambda p=path: open_shortcut(p))
    shortcut_button.pack()

def delete_shortcut():
    code = simpledialog.askstring("Supprimer un raccourci", "Entrez le code de sécurité")
    if code == "motdepassepardefaut":
        name = simpledialog.askstring("Supprimer un raccourci", "Entrez le nom du raccourci à supprimer")
        if name in shortcuts:
            del shortcuts[name]
            with open("shortcuts.json", "w") as f:
                json.dump(shortcuts, f)
            for widget in left_frame.winfo_children():
                if widget.cget("text") == name:
                    widget.destroy()
            messagebox.showinfo("Confirmation", "Le raccourci a été supprimé avec succès.")
        else:
            messagebox.showerror("Erreur", "Le nom du raccourci n'existe pas.")
    else:
        messagebox.showerror("Erreur", "Le code de sécurité est incorrect.")

def open_shortcut(path):
    if path.startswith("http"):
        webbrowser.open(path)
    else:
        path = path.replace("\\", "\\\\")
        os.startfile(path)

def change_name():
    new_name = simpledialog.askstring("Changer le nom de l'utilisateur", "Entrez le nouveau nom de l'utilisateur")
    if new_name:
        user_name.set(new_name)
        messagebox.showinfo("Confirmation", "Le nom de l'utilisateur a été changé avec succès.")
    else:
        messagebox.showerror("Erreur", "Le nom de l'utilisateur ne peut pas être vide.")

def greet_user():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        greet = "Bonne matinée ☀️"
    elif current_hour < 14:
        greet = "Bon appétit 🍽️"
    elif current_hour < 18:
        greet = "Bonne après-midi 😯"
    else:
        greet = "Bonne soirée 🌃"
    greet += " " + user_name.get()
    greet_text.config(text=greet)
    greet_text.after(60000, greet_user)

canvas = tk.Canvas(right_frame, width=400, height=400)
canvas.pack()

import os
import random
from PIL import ImageTk, Image

images = [f for f in os.listdir("C:/Users/Documents/Intranet/image") if f.endswith(".png")]

random_image = random.choice(images)

image = ImageTk.PhotoImage(Image.open("C:/Users/Documents/Intranet/image" + random_image))

canvas.create_image(200, 200, image=image)

def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_text.config(text="Il est " + current_time)
    time_text.after(1000, update_time)

update_time()
greet_user()
window.mainloop()
