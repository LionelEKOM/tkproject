import webbrowser
from customtkinter import*
from tkinter import*

def change():
    webbrowser.open_new('https://www.coodemaroc.com/2022/12/p_25.html')

#cCreation d'une fenetre 

app = CTk()

#Personnalisation d'une fenetre 
app.title("StudentScore")
app.geometry("720x450")
app.minsize(480, 320)

#icnoe de l'apk
app.iconbitmap("my_env/assets/img/logo.ico")

#background color 
app.config(bg="#47B77F")

#creer un frame 
frame = Frame(app, bg="#47B77F")
frame.pack(expand="true")

#Ajout du texte 
label_title = Label(frame, text="Hello world !!", font=("Roboto", 40), bg="#47B77F", fg="white")
label_title.pack()

label_title = Label(frame, text="What's going today ?!!", font=("Roboto", 25), bg="#47B77F", fg="white")
label_title.pack()

#Creer un button
btn = Button(frame, text="sign up", font=("Roboto", 40), bg="white", fg="#47B77F", command=change)
btn.pack(pady=30, fill=X)

#Affichage d'une fenetre 
app.mainloop()