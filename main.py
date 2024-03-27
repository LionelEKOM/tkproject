import tkinter as tk
import customtkinter
# Fonction pour afficher la fenêtre de détail d'un étudiant
def show_student_details(student_id):
    pass

# Création de la fenêtre principale
window = tk.Tk()
window.title("EnthrallIT Admin Dashboard")

# Création du menu
menu = tk.Menu(window)
window.config(menu=menu)

# Création du sous-menu "Students"
students_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Students", menu=students_menu)
students_menu.add_command(label="Students List", command=lambda: show_student_details("all"))
students_menu.add_command(label="Application List", command=lambda: show_student_details("application"))

# Création du sous-menu "Mentors"
mentors_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Mentors", menu=mentors_menu)
mentors_menu.add_command(label="Mentors List", command=lambda: show_student_details("mentor"))

# Création du cadre pour le contenu principal
content_frame = tk.Frame(window)
content_frame.pack(fill=tk.BOTH, expand=True)

# Création des labels et entries pour l'en-tête de la table
header_labels = [
    "",
    "SI",
    "Name",
    "Application",
    "Exam",
    "Class Video",
    "Student ID",
    "HW %",
    "HW GPA",
    "Honor Board",
    "Select Course",
    "Course",
]
header_frames = []
for i, label in enumerate(header_labels):
    frame = tk.Frame(content_frame)
    frame.pack(fill=tk.X, side=tk.TOP)
    tk.Label(frame, text=label, anchor="w").pack(side=tk.LEFT, fill=tk.X)
    header_frames.append(frame)

# Création des labels et entries pour les lignes de la table
line_labels = [
    "",
    "1",
    "Caldwell Decker",
    "40",
    "Class Notes",
    "202201",
    "EIT20220111",
    "50.00",
    "2.00",
    "",
    "2.00",
    "Home",
]
line_frames = []
for i in range(0, len(line_labels), 2):
    frame = tk.Frame(content_frame)
    frame.pack(fill=tk.X, side=tk.TOP)
    tk.Label(frame, text=line_labels[i], anchor="w").pack(side=tk.LEFT, fill=tk.X)
    entry = tk.Entry(frame)
    entry.insert(tk.END, line_labels[i + 1])
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    line_frames.append(frame)

# Fonction pour afficher la fenêtre de détail d'un étudiant
def show_student_details(student_id):
    if student_id == "all":
        # Afficher la liste de tous les étudiants
        pass
    elif student_id == "application":
        # Afficher la liste des demandes d'inscription
        pass
    elif student_id == "mentor":
        # Afficher la liste des mentors
        pass
    else:
        # Afficher les détails d'un étudiant spécifique
        pass

# Lancement de la boucle principale
window.mainloop()

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()