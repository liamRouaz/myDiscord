import tkinter as tk
from tkinter import messagebox
#from ChatServeur import ChatServeur
#from ChatClient import ChatClient
import cv2
from PIL import Image, ImageTk


class InterfaceRegister():
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
        self.image_background = tk.PhotoImage(file="assets/cieletoiles2.png")
        canvas.create_image(-60, 0, anchor=tk.NW, image=self.image_background) 

    def enter_name(self):
        # Création et placement du label et du champ de saisie pour le prénom
        self.label_name = tk.Label(self.screen, text="Prenom", bg="#61008E", font='ROGFonts-Regular')
        self.label_name.place(x=240, y=200)
        

        self.entry_name = tk.Entry(self.screen, bg="#AC66FB")
        self.entry_name.place(x=190, y=230, width=200, height=30)

    def enter_surname(self):
        # Création et placement du label et du champ de saisie pour le nom
        self.label_surname = tk.Label(self.screen, text="Nom", bg="#61008E", font='ROGFonts-Regular')
        self.label_surname.place(x=260, y=280)
        

        self.entry_surname = tk.Entry(self.screen, bg="#AC66FB")
        self.entry_surname.place(x=190, y=310, width=200, height=30)

    def enter_email(self):
        # Création et placement du label et du champ de saisie pour l'email
        self.label_email = tk.Label(self.screen, text="Email", bg="#61008E", font='ROGFonts-Regular')
        self.label_email.place(x=250, y=360)
        

        self.entry_email = tk.Entry(self.screen, bg="#AC66FB")
        self.entry_email.place(x=190, y=390, width=200, height=30)

    def enter_password(self):
        # Création et placement du label et du champ de saisie pour le mot de passe
        self.label_password = tk.Label(self.screen, text="Mot de passe", bg="#61008E", font='ROGFonts-Regular')
        self.label_password.place(x=193, y=440)


        self.entry_password = tk.Entry(self.screen, show="*", bg="#AC66FB") # Affiche des astérisques pour le mot de passe
        self.entry_password.place(x=190, y=470, width=200, height=30)

    def verif_password(self):
        # Création et placement du label et du champ de saisie pour la vérification du mot de passe
        self.label_verif_password = tk.Label(self.screen, text="Verification du mot de passe", bg="#61008E", font='ROGFonts-Regular')
        self.label_verif_password.place(x=90, y=520)
        

        self.entry_verif_password = tk.Entry(self.screen, bg="#AC66FB", show="*")
        self.entry_verif_password.place(x=190, y=550, width=200, height=30)

    def btn_register(self):
        # Création et placement du bouton d'inscription
        self.button_login = tk.Button(self.screen, text="Creer compte", bg="#BC1A86", font='ROGFonts-Regular')
        self.button_login.place(x=180, y=620)

    
    # Fonction pour valider la connexion
    def validate_login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        # Authentifier l'utilisateur avec le serveur
        user_id = self.chat_server.authenticate_user(email, password)
        print(user_id)

        if user_id is not None:
            messagebox.showinfo("Connexion réussie", f"Bienvenue, {email} !")
            # Connectez le client au serveur après la validation des identifiants
            self.chat_client.connect_to_server(email, password, user_id)  # Fournir également l'identifiant de l'utilisateur
            # Fermez l'interface après la connexion
            self.screen.destroy()
        else:
            messagebox.showerror("Échec de la connexion", "Identifiant ou mot de passe incorrect")


    # def open_main_interface(self):
    #     # Ajoutez le code pour ouvrir l'interface principale après la connexion réussie
    #     pass

    # Fonction pour gérer le cas de mot de passe oublié ou email perdu
    def forgot_password(self):
        # Vous pouvez implémenter votre logique pour gérer les mots de passe oubliés ou les e-mails perdus ici
        messagebox.showinfo("Fonctionnalité non implémentée", "Désolé, cette fonctionnalité n'est pas encore disponible.")

interfacelogin = InterfaceRegister()
interfacelogin.background_image()
interfacelogin.enter_name()
interfacelogin.enter_surname()
interfacelogin.enter_email()
interfacelogin.enter_password()
interfacelogin.verif_password()
interfacelogin.btn_register()
interfacelogin.screen.mainloop()  # Démarrer la boucle principale après la création des widgets
