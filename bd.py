from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import mysql.connector
from tkinter import *
from customtkinter import *
from tkcalendar import DateEntry
from model.Personne import Etudiant


'''Reset all the entry fields'''
def reset_fields():
        entry_nom.delete(0, END)
        entry_prenom.delete(0, END)



def inserer_etudiant():
    # Récupérer les valeurs des champs saisis par l'utilisateur
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    classe = combo_classe.get()
    sexe = valeur_sexe.get()
    dateNaiss = entry_date.get()
    
    # Vérifier si tous les champs sont remplis
    if nom and prenom and classe and sexe and dateNaiss:
        etudiant = Etudiant(nom, prenom, sexe, dateNaiss, classe)
        matrucule = etudiant.matricule
        # Exécuter la requête SQL pour insérer l'étudiant dans la base de données
        cursor.execute("INSERT INTO Etudiant (matEtudiant, idClasse, nom, prenom, sexe, dateNaiss ) VALUES (%s, %s, %s, %s, %s, %s)", (matrucule, etudiant.id_classe, etudiant.nom, etudiant.prenom, etudiant.sexe, etudiant.date_naissance))
        conn.commit()
        # Message de succès
        messagebox.showinfo("Succès", "L'étudiant a été ajouté avec succès à la base de données.")
        fenetre.destroy()
    else:
        # Message d'erreur si un champ est manquant
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="devoir"
)
cursor = conn.cursor()

fenetre = Tk()
frame_etudiants = Frame(fenetre)
fenetre.geometry('1020x620')
frame_etudiants.pack()

#+++++++++++++++ Affichage des donnees d'une BD +++++++++++++++++
tree = Treeview(fenetre, columns= (1, 2, 3, 4), height=3, show= "headings")
tree.place(x=20, y=10, width=450, height=220)

tree.heading(1,  text="Nom")
tree.heading(2,  text="Prenom")
tree.heading(3,  text="Sexe")
tree.heading(4,  text="Date Naissance")

tree.column(1, width=90)
tree.column(2, width=80)
tree.column(3, width=100)
tree.column(4, width=120)
# Requête SQL pour sélectionner les étudiants
sql = "SELECT nom, prenom, sexe, datenaiss FROM Etudiant"
cursor.execute(sql)

# Parcourir les résultats et les afficher dans la Frame
for row in cursor.fetchall():
    # Créer un widget Label pour chaque étudiant
    tree.insert('', END, values=row)


main = CTkFrame(fenetre, width=550, height=305, corner_radius=8, bg_color='white')
main.place(x=502, y=2)

# Création des champs de saisie pour le nom, prénom et la classe de l'étudiant
label_nom = CTkLabel(main, text="Nom :")
label_nom.grid(row=0, column=0, padx=5, pady=10)
entry_nom = CTkEntry(main, placeholder_text='votre nom')
entry_nom.grid(row=0, column=1, padx=5, pady=0)

label_prenom = CTkLabel(main, text="Prénom :")
label_prenom.grid(row=1, column=0, padx=10, pady=10)
entry_prenom = CTkEntry(main, placeholder_text='Votre prenom')
entry_prenom.grid(row=1, column=1)

# Champ Classe
label_classe = CTkLabel(main, text="Classe :")
label_classe.grid(row=2, column=0, padx=10, pady=10)

# Classes disponibles
classes = {1 : "GL3A", 2 : "GL3B", 3 : "GL3C", 4 : "GL3D", 5 : "SR3A", 6 : "SR3B"}

# Fonction pour retourner la clé d'une classe
def get_key(classe):
    for key, value in classes.items():
        if value == classe:
            return key
        
combo_classe = CTkComboBox(main, values=list(classes.values()))
combo_classe.grid(row=2, column=1)

# Fonction pour afficher la clé lorsqu'une classe est sélectionnée
def on_select(event):
    classe = combo_classe.get()
    key = get_key(classe)
    print(f"Clé sélectionnée : {key}")

# Ajout de l'événement de sélection
combo_classe.bind("<<ComboboxSelected>>", on_select)

# Champ Sexe
label_sexe = CTkLabel(main, text="Sexe :")
label_sexe.grid(row=3, column=0, padx=5, pady=10)

# Radio buttons pour le sexe
valeur_sexe = StringVar(value="M")
radio_homme = CTkRadioButton(main, text="Homme", variable=valeur_sexe, value="M")
radio_homme.grid(row=3, column=1, padx=5, pady=0)
radio_femme = CTkRadioButton(main, text="Femme", variable=valeur_sexe, value="F")
radio_femme.grid(row=3, column=2, padx=2, pady=0)
print(valeur_sexe)

# Champ Date de naissance

label_date = CTkLabel(main, text="Date de naissance :")
label_date.grid(row=4, column=0, padx=5, pady=10)
entry_date = DateEntry(main, date_pattern='yyyy-mm-dd')  # Utilisation du widget DateEntry avec le motif de date spécifié
entry_date.grid(row=4, column=1, padx=5, pady=0)


# Bouton pour ajouter l'étudiant
btn_ajouter = CTkButton(main, text="Ajouter étudiant", command=inserer_etudiant)
btn_ajouter.grid(row=5, columnspan=2, pady=10)


fenetre.mainloop()

# Fermer la connexion à la base de données
conn.close()
