from tkinter import Tk, Label, Button

def create_student():
    # Code pour créer un nouvel étudiant
    pass

def display_student():
    # Code pour afficher les détails d'un étudiant
    pass

def modify_student_grade():
    # Code pour modifier la note d'un étudiant
    pass

def display_student_grades():
    # Code pour afficher les notes d'un étudiant
    pass

def search_student():
    # Code pour rechercher un étudiant
    pass

# Fonction pour ouvrir la page d'accueil
def open_homepage():
    # Créer une fenêtre
    homepage = Tk()
    homepage.title('Gestion des étudiants')
    homepage.geometry('400x300')

    # Labels
    Label(homepage, text='Bienvenue dans l\'application de gestion des étudiants', font=('Arial', 16)).pack(pady=20)
    
    # Boutons
    Button(homepage, text='Créer un étudiant', width=20, command=create_student).pack()
    Button(homepage, text='Afficher un étudiant', width=20, command=display_student).pack()
    Button(homepage, text='Modifier la note d\'un étudiant', width=20, command=modify_student_grade).pack()
    Button(homepage, text='Afficher les notes d\'un étudiant', width=20, command=display_student_grades).pack()
    Button(homepage, text='Rechercher un étudiant', width=20, command=search_student).pack()

    # Lancer la boucle principale
    homepage.mainloop()

# Appeler la fonction pour ouvrir la page d'accueil
open_homepage()