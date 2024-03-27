from subprocess import call
from customtkinter import *
from tkinter import *
from tkinter import messagebox


win = CTk()
win.geometry('925x500+150+100')
win.iconbitmap('my_env/assets/img/logo.ico')
win.config(bg='#fff')
win.resizable(False, False)

def deconnexion():
    # Demande de confirmation
    reponse = messagebox.askyesno(
        title="Déconnexion",
        message="Voulez-vous vraiment vous déconnecter ?",
        icon="question",
    )
    # Redirection si confirmation
    if reponse:
        print("Déconnexion en cours...")
        # Exemple : redirection vers la page de connexion
        win.destroy()
        call(["python", "apk.py"])  # Lance le script login.

    else:
        print("Déconnexion annulée.")

#-------------- Frame ------------------------
frame = Frame(win, width=300, height=760, bg='#57a1f8')
frame.pack(side=LEFT)

#------------- Label ----------------
h1 = CTkLabel(master=frame, text='School score', fg_color='#57a1f8', font=('Microsoft Yahei UI Light', 18, 'bold',))
h1.place(x=30, y= 15)
CTkFrame(frame, width=120, height=2, bg_color='black', fg_color='black').place(x=30, y=40)


# Créer le bouton de déconnexion
button = CTkButton(
    master=frame,
    text="Déconnexion",
    command=deconnexion,
    width=120,
    fg_color= '#f80505',
    hover_color="#46e59e",
    border_width=2,
    font=("Arial", 12),
    corner_radius=10,
)

# Positionner le bouton
button.place(x=30, y=460)

#------------------ Main -----------------

main = CTkFrame(win, width=720, height=495, corner_radius=8, bg_color='white')
main.place(x=202, y=2)

h2 = CTkLabel(main, text='Connexion', font=('Roboto', 16, 'bold'))
h2.place(x=80, y=20)
CTkFrame(main, width=85, height=2, bg_color='black', fg_color='black').place(x=80, y=45)

#++++++++++++++++++ Input +++++++++++++++
c1 = CTkEntry(main, width=85, corner_radius=8, placeholder_text='Firstname', font=('Arial', 10, 'italic'), border_color='white')
c1.place(x=60, y=55)

win.mainloop()