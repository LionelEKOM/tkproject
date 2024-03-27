from customtkinter import *

# Dictionnaire des classes
classes = {
    1: "GL3A",
    2: "GL3B",
    3: "GL3C",
    4: "GL3D",
    5: "SR3A",
    6: "SR3B",
}

# Fonction pour retourner la clé d'une classe
def get_key(classe):
    for key, value in classes.items():
        if value == classe:
            return key

# Création de la fenêtre
fenetre = CTk()

# Création du combobox
combo = CTkComboBox(fenetre, values=list(classes.values()))
combo.pack(pady=20)

# Fonction pour afficher la clé lorsqu'une classe est sélectionnée
def on_select(event):
    classe = combo.get()
    key = get_key(classe)
    print(f"Clé sélectionnée : {key}")

# Ajout de l'événement de sélection
combo.bind("<<ComboboxSelected>>", on_select)

# Affichage de la fenêtre
fenetre.mainloop()

