import customtkinter
from tkinter import *

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Personnalisation de la fenetre 
        self.title("Login")
        self.geometry("925x500+300+200")
        self.iconbitmap("my_env/assets/img/logo.ico")
        self.configure(bg="#fff")
        #self.minsize(720, 420) Taille limite de la fenetre 
        self.grid_columnconfigure((0, 1), weight=1)
        # self.resizable(False, False) #Permet de ne plus modifier les dimensions de la fenetre

        #Insertion de l'image 
        img = PhotoImage(file='my_env/assets/img/login.png')
        Label(self, image=img, bg='white').place(x=50, y=50)

        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.button = customtkinter.CTkButton(self.frame, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="nsw", columnspan=2)
        self.checkbox_1 = customtkinter.CTkCheckBox(self.frame, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsw")
        self.checkbox_2 = customtkinter.CTkCheckBox(self.frame, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="nsw")


    def button_callback(self):
        print("button pressed")