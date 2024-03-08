import tkinter as tk
from tkinter import *


class InterfaceLost():
    def __init__(self):
        #self.chat_server = ChatServeur('localhost', 8585)
        #self.chat_client = ChatClient('localhost', 8585)
        self.screen = tk.Tk()
        self.screen.title("MyDiscord")
        self.screen.geometry("600x700")
        self.screen.resizable(False, False)
        self.screen.configure(background="#343541")
        # self.entry_email.get()
        # self.entry_password.get()

    def background_image(self):
        # Créer un Canvas pour afficher l'image
        canvas = tk.Canvas(self.screen, width=800, height=850, bg="#343541", borderwidth=0, highlightthickness=0)
        canvas.pack()

        # Charger l'image et l'afficher dans le Canvas
        self.image_background = tk.PhotoImage(file="assets/cieletoiles3.png")
        canvas.create_image(-60, 0, anchor=tk.NW, image=self.image_background) 
        # Ajouter le texte sur le canevas avec un fond transparent
        canvas.create_text(140, 240, anchor=tk.NW, text="Reinitialisation \n                du \n  mot de passe", fill="#AC66FB", font=("ROGFonts-Regular", 20))
        # Rafraîchir le canevas pour afficher les changements
        canvas.update()

        # Gardez une référence à l'image pour éviter la garbage collection
     #   canvas.image = photo_title
    #def add_text(self):
        # # Charger l'image à utiliser comme arrière-plan du titre
        # image_title = Image.open("assets/cieletoiles1.png")  # Assurez-vous que le format de l'image prend en charge la transparence (PNG)
        # photo_title = ImageTk.PhotoImage(image_title)

        # # Créer un canevas pour afficher l'image en arrière-plan
        # canvas = Canvas(self.screen, borderwidth=0, highlightthickness=0, background="#343541", width=600, height=50)
        # canvas.place(x=0, y=0)

        # # Ajouter l'image en arrière-plan du canevas
        # canvas.create_image(0, 0, anchor=tk.NW, image=photo_title)




    # def enter_name(self):
    #     # Création et placement du label et du champ de saisie pour le prénom
    #     self.label_name = tk.Label(self.screen, text="Prenom", bg="#61008E", font='ROGFonts-Regular')
    #     self.label_name.place(x=240, y=220)
        

    #     self.entry_name = tk.Entry(self.screen, bg="#AC66FB")
    #     self.entry_name.place(x=190, y=250, width=200, height=30)

    # def enter_surname(self):
    #     # Création et placement du label et du champ de saisie pour le nom
    #     self.label_surname = tk.Label(self.screen, text="Nom", bg="#61008E", font='ROGFonts-Regular')
    #     self.label_surname.place(x=260, y=300)
        

    #     self.entry_surname = tk.Entry(self.screen, bg="#AC66FB")
    #     self.entry_surname.place(x=190, y=330, width=200, height=30)

    def enter_email(self):
        # Création et placement du label et du champ de saisie pour l'email
        self.label_email = tk.Label(self.screen, text="Email", bg="#61008E", font='ROGFonts-Regular')
        self.label_email.place(x=250, y=380)
        

        self.entry_email = tk.Entry(self.screen, bg="#AC66FB")
        self.entry_email.place(x=190, y=410, width=200, height=30)

    def btn_valid(self):
        # Création et placement du bouton d'inscription
        self.button_login = tk.Button(self.screen, text="Valider", bg="#BC1A86", font='ROGFonts-Regular')
        self.button_login.place(x=220, y=550)


interface_lost = InterfaceLost()
interface_lost.background_image()
#interface_lost.add_text()
#interface_lost.enter_name()
#interface_lost.enter_surname()
interface_lost.enter_email()
interface_lost.btn_valid()
interface_lost.screen.mainloop()  # Démarrer la boucle principale après la création des widgets