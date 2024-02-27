import tkinter as tk
from tkinter import messagebox
from ChatServeur import ChatServeur
from ChatClient import ChatClient


class InterfaceLogin:
    def __init__(self):
        self.chat_server = ChatServeur('10.10.94.117', 5000)
        self.chat_client = ChatClient('10.10.94.117', 5000)
        self.screen = tk.Tk()
        self.screen.title("MyDiscord")
        self.screen.geometry("600x700")
        self.screen.resizable(False, False)
        self.screen.configure(background="#343541")
        self.create_widgets()
        self.entry_email.get()
        self.entry_password.get()
        self.screen.mainloop()  # Démarrer la boucle principale après la création des widgets

    def create_widgets(self):
        # Créez les widgets de l'interface ici
        self.background_image()
        self.enter_email()
        self.enter_password()
        self.btn_login()
        self.btn_forgot_password()

    def background_image(self):
        # Créer un Canvas pour afficher l'image
        canvas = tk.Canvas(self.screen, width=500, height=550, bg="#343541", borderwidth=0, highlightthickness=0)
        canvas.pack()

        # Charger l'image et l'afficher dans le Canvas
        self.image_background = tk.PhotoImage(file="classe/discorde.png")
        canvas.create_image(62,  50, anchor=tk.NW, image=self.image_background)  

    def enter_email(self):
        # Création et placement du label et du champ de saisie pour l'email
        self.label_email = tk.Label(self.screen, text="Email :", bg="#343541")
        self.label_email.pack()

        self.entry_email = tk.Entry(self.screen)
        self.entry_email.pack()

    def enter_password(self):
        # Création et placement du label et du champ de saisie pour le mot de passe
        self.label_password = tk.Label(self.screen, text="Mot de passe :", bg="#343541")
        self.label_password.pack()

        self.entry_password = tk.Entry(self.screen, show="*") # Affiche des astérisques pour le mot de passe
        self.entry_password.pack()

    def btn_login(self):
        # Création et placement du bouton de connexion
        self.button_login = tk.Button(self.screen, text="Se connecter", command=self.validate_login)
        self.button_login.pack()

    def btn_forgot_password(self):
        # Création et placement du bouton pour le cas de mot de passe oublié ou email perdu
        self.button_forgot_password = tk.Button(self.screen, text="Mot de passe ou Email perdu?", command=self.forgot_password)
        self.button_forgot_password.pack()

    
    # Fonction pour valider la connexion
    def validate_login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        # Authentifier l'utilisateur avec le serveur
        user_id = self.chat_server.authenticate_user(email, password)

        if user_id is not None:
            messagebox.showinfo("Connexion réussie", f"Bienvenue, {email} !")
            # Connectez le client au serveur après la validation des identifiants
            self.chat_client.connect_to_server(email, password, user_id)  # Fournir également l'identifiant de l'utilisateur
            self.chat_client.start() 
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




