import tkinter as tk
from tkinter import messagebox
from ChatServeur import ChatServeur
from ChatClient import ChatClient
from Channel import Channel



class InterfaceLogin():
    def __init__(self):
        self.chat_server = ChatServeur('10.10.0.38', 5000)                                        #('10.10.100.103', 5000)
        self.screen = tk.Tk()
        self.screen.title("MyDiscord")
        self.screen.geometry("600x700")
        self.screen.resizable(False, False)
        self.screen.configure(background="#343541")
        # self.create_widgets()
        # self.entry_email.get()
        # self.entry_password.get()

    def background_image(self):
        # Créer un Canvas pour afficher l'image
        canvas = tk.Canvas(self.screen, width=800, height=850, bg="#343541", borderwidth=0, highlightthickness=0)
        canvas.pack()

        # Charger l'image et l'afficher dans le Canvas
        self.image_background = tk.PhotoImage(file="assets/cieletoiles.png")
        canvas.create_image(-60, 0, anchor=tk.NW, image=self.image_background) 

    def enter_email(self):
        # Création et placement du label et du champ de saisie pour l'email
        self.label_email = tk.Label(self.screen, text="Email", bg="#61008E", font='ROGFonts-Regular')
        self.label_email.place(x=250, y=240)
        

        self.entry_email = tk.Entry(self.screen, bg="#AC66FB")
        self.entry_email.place(x=190, y=270, width=200, height=30)

    def enter_password(self):
        # Création et placement du label et du champ de saisie pour le mot de passe
        self.label_password = tk.Label(self.screen, text="Mot de passe", bg="#61008E", font='ROGFonts-Regular')
        self.label_password.place(x=193, y=320)


        self.entry_password = tk.Entry(self.screen, show="*", bg="#AC66FB") # Affiche des astérisques pour le mot de passe
        self.entry_password.place(x=190, y=350, width=200, height=30)
    def btn_login(self):
        # Création et placement du bouton de connexion
        self.button_login = tk.Button(self.screen, text="Se connecter", command=self.validate_login, bg="#AC66FB", font='ROGFonts-Regular')
        self.button_login.place(x=180, y=500)

    def btn_register(self):
        # Création et placement du bouton d'inscription
        self.button_login = tk.Button(self.screen, text="Creer un compte", bg="#BC1A86", font='ROGFonts-Regular', command=self.register)
        self.button_login.place(x=160, y=560)

    def btn_forgot_password(self):
        # Création et placement du bouton pour le cas de mot de passe oublié ou email perdu
        self.button_forgot_password = tk.Button(self.screen, text="Mot de passe ou Email oublie", command=self.forgot_password, bg="#61008E", font='ROGFonts-Regular')
        self.button_forgot_password.place(x=75, y=620)
    
    # Fonction pour valider la connexion
    def validate_login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        # Authentifier l'utilisateur avec le serveur
        user_id = self.chat_server.authenticate_user(email, password)

        if user_id is not None:
            messagebox.showinfo("Connexion réussie", f"Bienvenue, {email} !")

            # Connectez le client au serveur après la validation des identifiants
            self.chat_client = ChatClient('10.10.0.38', 5000)
            self.chat_client.connect_to_server(email, password, user_id)
            
            self.screen.destroy()

            channels = Channel.get_channels()
            from ChatApp import ChatApp
            root = tk.Tk()
            app = ChatApp(root, self.chat_client, channels) # Passer les canaux à ChatApp
            root.mainloop()
        else:
            messagebox.showerror("Échec de la connexion", "Identifiant ou mot de passe incorrect")

    def register(self):
        self.screen.destroy()
        from InterfaceRegister import ALL
    # def open_main_interface(self):
    #     # Ajoutez le code pour ouvrir l'interface principale après la connexion réussie
    #     pass

    # Fonction pour gérer le cas de mot de passe oublié ou email perdu
    def forgot_password(self):
        # Vous pouvez implémenter votre logique pour gérer les mots de passe oubliés ou les e-mails perdus ici
        self.screen.destroy()
        # from InterfaceLost import ALL

interfacelogin = InterfaceLogin()
interfacelogin.background_image()
interfacelogin.enter_email()
interfacelogin.enter_password()
interfacelogin.btn_login()
interfacelogin.btn_register()
interfacelogin.btn_forgot_password()
interfacelogin.screen.mainloop()
