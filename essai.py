from tkinter import *
import mysql.connector
from tkinter import *
from customtkinter import *

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="devoir"
)
cursor = conn.cursor()

# Création de l'interface graphique
app = Tk()
app.title("Gestion des Apprenants par Classe")
app.geometry("720x300")

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox_var = StringVar(value="GL3A")
combobox = CTkComboBox(app, values=["option 1", "option 2"],
command=combobox_callback, variable=combobox_var)
combobox.pack(pady=20)


# Création du Ctkcombobox pour afficher les classes
classes = {
    1 : 'SIL',
    2 : 'CP', 
    3 : 'CE1', 
    4 : 'CE2'
}
# combo_classes = CTkComboBox(app, values=classes.keys())
# combo_classe = CTkComboBox(app, values=list(classes.keys()))
# combo_classe.pack(pady=20)
# print(classes.values())
# Création de la liste des apprenants
# apprenants_list = Listbox(app)
# apprenants_list.pack(pady=10)



# Méthode pour récupérer les apprenants d'une classe spécifique
def get_apprenants(classe):
    cursor.execute("SELECT nom, prenom FROM Etudiant WHERE idClasse = %s", (classe))
    apprenants = cursor.fetchall()
    return apprenants

# Fonction pour mettre à jour la liste des apprenants
# def update_apprenants(event):
#     classe_selected = combo_classe.get()
#     apprenants_list.delete(0, END)
#     apprenants = get_apprenants(classe_selected)
#     for apprenant in apprenants:
#         apprenants_list.insert(END, f"{apprenant[0]} {apprenant[1]}")

# # Lier la fonction à l'événement de sélection d'une classe
# combo_classe.bind("<<ComboboxSelected>>", update_apprenants)

# Affichage de l'interface graphique
app.mainloop()

# Fermeture de la connexion à la base de données
conn.close()



# from model.Personne import Personne

# print("Registering...")
# lastname = str(input("Enter your Last Name: "))
# firstname = str(input("Enter your First Name: "))
# sexe = str(input("Enter your Age: "))
    

# P1 = Personne(lastname, firstname, sexe)
# print(f"{P1.generer_matricule()}, {P1.nom}")