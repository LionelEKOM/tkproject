from datetime import date
import random
import string


class Personne:

    def __init__(self, nom, prenom, sexe):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
    """Méthode qui génère un numéro de matricule unique"""

    def generer_matricule(self):
        # Caractères autorisés pour le matricule
        caracteres = string.ascii_uppercase + string.digits
    
        # Génération du matricule aléatoire
        matricule = ''.join(random.choices(caracteres, k=6))
    
        return matricule
    
    # def display():
    #     print(f"Nom : {Personne.nom}")
    #     print(f"Prenom : {Personne.prenom}")
    #     print(f"Sexe : {Personne.sexe}")
    #     print(f"Matricule : {Personne.generer_matricule()}")



class Etudiant(Personne):

    def __init__(self, nom, prenom, sexe, date_naissance, id_classe):
        super().__init__(nom, prenom, sexe)
        self.matricule = self.generer_matricule()
        self.date_naissance = date_naissance
        self.id_classe = id_classe



# Exemple d'utilisation
# etudiant1 = Etudiant("Njoya", "Clarence", "M", date(2000, 1, 1), 1)
# etudiant2 = Etudiant("Tchinda", "Paul", "H", date(2001, 2, 2), 2)
# etudiant3 = Etudiant("Moukoko", "Joel", "M", date(2002, 3, 3), 3)

# print(f"Matricule étudiant 1 : {etudiant1.matricule}")
# print(f"Matricule étudiant 2 : {etudiant2.matricule}")
# print(f"Matricule étudiant 3 : {etudiant3.matricule}")

class Enseignant(Personne):
    def __init__(self, nom, prenom, sexe):
        super().__init__(nom, prenom, sexe)
        self.matricule_ens = self.generer_matricule()


# E1  = Enseignant("Kabongo", "Francis", "M")
# E2  = Enseignant("Linga", "Jacques", "H")

# print(f"{E1.nom} Matricule : {E1.matricule_ens}\n")
# print(f"{E2.nom} Matricule : {E2.matricule_ens}\n")