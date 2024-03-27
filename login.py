
from subprocess import call
from tkinter import messagebox
from customtkinter import *
from tkinter import *
import mysql.connector

from model.Personne import Personne
# from subprocess import call #Permet le deplacement d'une fenetre a une autre

#Creation de la fenetre 
root = Tk()

#Personnalisation de la fenetre
root.title('StudentScore')
root.geometry('925x500+150+100')#('150+100') represente la disposition l'interface au niveau de l'ecran
root.iconbitmap('my_env/assets/img/logo.ico')
root.config(bg='#fff')
root.resizable(False, False)

#Verification des identifiants 
def signin():
    username = user.get()
    password = code.get()


    # Vérifier les identifiants dans la base de données
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="devoir"
    )
    cursor = connection.cursor()

    # Exécuter une requête SELECT pour vérifier les identifiants
    query = "SELECT * FROM user WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    # Fermer la connexion à la base de données
    connection.close()

    if result:
        root.destroy()
        call(["python", "test.py"])  # Lance le script login.
        # Identifiants valides
        # screen = Toplevel(root)
        # # screen = Tk()
        # screen.title('Homepage')
        # screen.geometry('925x500+150+100')
        # screen.config(bg='white')
        # screen.iconbitmap("my_env/assets/img/logo.ico")

        # Label(screen, text='Hello world !!', bg='#fff', font=('Roboto', 50, 'bold')).pack(expand=True)
        # screen.mainloop()

    else:
        # Identifiants invalides
        messagebox.showerror(title='Warning !!', message='Identifiants invalides !!!')


#insertion d'une image
img = PhotoImage(file='my_env/assets/img/login.png')
Label(root, image=img, bg='#fff').place(x=50, y=50)

#creation d'un frame 
frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Connexion', fg='#57a1f8', bg='white', font=('Roboto', 23, 'bold'))
heading.place(x=90, y=5)

#champs
############################# Username ##########################

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', bg='white', border=0, font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('FocusOut', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

############################# Password ##########################

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        user.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', bg='white', border=0, font=('Microsoft Yahei UI Light', 11), show='*')
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('FocusOut', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


######################### Button ######################
Button(frame, width=39, pady=7, text='Connexion', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=signin).place(x=35, y=204)
label = Label(frame, text='Vous n\'avez pas de compte ?', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=75, y=260)

sign_up = Button(frame, width=6, text='S\'inscrire', fg='#57a1f8', bg='white', cursor='hand2', border=0)
sign_up.place(x=245, y=260)

# c1 = CTkEntry(frame, width=150, placeholder_text='Hello wolrd', corner_radius=10, bg_color='white')
# c1.grid(row=25, column=10, padx=30, pady=190)


root.mainloop()