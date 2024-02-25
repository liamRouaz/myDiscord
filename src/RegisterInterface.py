import tkinter as tk
from tkinter import messagebox
#from ChatServeur import ChatServeur
#from ChatClient import ChatClient
import cv2
from PIL import Image, ImageTk


class InterfaceLogin:
    def __init__(self):
        #self.chat_server = ChatServeur('localhost', 8585)
        #self.chat_client = ChatClient('localhost', 8585)
        self.screen = tk.Tk()
        self.screen.title("MyDiscord")
        self.screen.geometry("600x700")
        self.screen.resizable(False, False)
        self.screen.configure(background="#343541")
        self.create_widgets()
        self.entry_email.get()
        self.entry_password.get()

# # Créez un canevas pour afficher la vidéo
#         self.canvas = tk.Canvas(self.screen, width=800, height=800)
#         self.canvas.pack()

#         # Chargez la vidéo avec OpenCV
#         self.vid = cv2.VideoCapture('assets/etoiles.mp4')
#         if not self.vid.isOpened():
#             raise ValueError("Impossible d'ouvrir la vidéo")

#         self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
#         self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

#         # Calculez les coordonnées pour centrer la vidéo dans le canevas
#         self.x = (800 - self.width) // 2
#         self.y = (600 - self.height) // 2

#         # Affichez la première image de la vidéo sur le canevas
#         self.photo = None
#         self.update()
        
#     def update(self):
#         # Lisez une image à partir de la vidéo
#         ret, frame = self.vid.read()
#         if ret:
#             # Convertissez l'image en format compatible avec tkinter
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
#             # Affichez l'image centrée dans le canevas
#             self.canvas.create_image(self.x, self.y, anchor=tk.NW, image=self.photo)
#         self.screen.after(20, self.update)

#     def __del__(self):
#         if self.vid.isOpened():
#             self.vid.release()

    def create_widgets(self):
        # Créez les widgets de l'interface ici
        self.background_image()
        self.enter_email()
        self.enter_password()
        self.btn_login()
        self.btn_register()
        self.btn_forgot_password()

    def background_image(self):
        # Créer un Canvas pour afficher l'image
        canvas = tk.Canvas(self.screen, width=800, height=850, bg="#343541", borderwidth=0, highlightthickness=0)
        canvas.pack()

        # Charger l'image et l'afficher dans le Canvas
        self.image_background = tk.PhotoImage(file="assets/cieletoiles2.png")
        canvas.create_image(-60, 0, anchor=tk.NW, image=self.image_background) 

    def title(self):
        # Création et placement du label et du champ de saisie pour le mot de passe
        self.label_password = tk.Label(self.screen, text="MyDiscord", bg="#343541")
        self.label_password.pack() 

    def enter_email(self):
        # Création et placement du label et du champ de saisie pour l'email
        self.label_email = tk.Label(self.screen, text="Email", bg="#61008E", font='ROGFonts-Regular')
        self.label_email.place(x=250, y=300)
        

        self.entry_email = tk.Entry(self.screen, bg="#AC66FB")
        self.entry_email.place(x=190, y=330, width=200, height=30)

    def enter_password(self):
        # Création et placement du label et du champ de saisie pour le mot de passe
        self.label_password = tk.Label(self.screen, text="Mot de passe", bg="#61008E", font='ROGFonts-Regular')
        self.label_password.place(x=193, y=390)


        self.entry_password = tk.Entry(self.screen, show="*", bg="#AC66FB") # Affiche des astérisques pour le mot de passe
        self.entry_password.place(x=190, y=420, width=200, height=30)


    def btn_login(self):
        # Création et placement du bouton de connexion
        self.button_login = tk.Button(self.screen, text="Se connecter", command=self.validate_login, bg="#AC66FB", font='ROGFonts-Regular')
        self.button_login.place(x=180, y=500)

    def btn_register(self):
        # Création et placement du bouton d'inscription
        self.button_login = tk.Button(self.screen, text="Creer un compte", bg="#BC1A86", font='ROGFonts-Regular')
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
interfacelogin = InterfaceLogin()
interfacelogin.screen.mainloop()  # Démarrer la boucle principale après la création des widgets
#app = VideoBackgroundApp(root, 'assets/etoiles.mp4')


# import tkinter as tk
# from Users import Users

# class RegisterInterface:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("MyDiscord")
#         self.root.geometry("600x800")
        
#         self.first_name_label = tk.Label(self.root, text="Prénom : ")
#         self.first_name_entry = tk.Entry(self.root)
#         #self.first_name_entry = Users.first_name
#         self.last_name_label = tk.Label(self.root, text="Nom : ")
#         self.last_name_entry = tk.Entry(self.root)
#         #self.last_name_entry = Users.last_name
#         self.email_label = tk.Label(self.root, text="Email : ")
#         self.email_entry = tk.Entry(self.root)
#         #self.email_entry = Users.email
#         self.password_label = tk.Label(self.root, text="Mot de passe : ")
#         self.password_entry = tk.Entry(self.root)
#         #self.password_entry = Users.password
#         # self.confirm_password_label = tk.Label(self.root, text="Confirmation mot de passe : ")
#         # self.confirm_password_entry = tk.Entry(self.root, show="*")
        
#         self.register_button = tk.Button(self.root, text="Inscription", command=self.register_user)
        
#         self.first_name_label.grid(row=0, column=0)
#         self.first_name_entry.grid(row=0, column=1)
#         self.last_name_label.grid(row=1, column=0)
#         self.last_name_entry.grid(row=1, column=1)
#         self.email_label.grid(row=2, column=0)
#         self.email_entry.grid(row=2, column=1)
#         self.password_label.grid(row=5, column=0)
#         self.password_entry.grid(row=5, column=1)
#         # self.confirm_password_label.grid(row=6, column=0)
#         # self.confirm_password_entry.grid(row=6, column=1)

#         self.register_button.grid(row=7, column=1)
        
#         self.root.mainloop()
    
#     def register(self):
#         first_name = self.first_name_entry.get()
#         last_name = self.last_name_entry.get()
#         email = self.email_entry.get()
#         password = self.password_entry.get()
#         #confirm_password = self.confirm_password_entry.get()
        
       
#         self.register_user(first_name, last_name, email, password)

#     def register_user(self):
#         first_name = self.first_name_entry.get()
#         last_name = self.last_name_entry.get()
#         email = self.email_entry.get()
#         password = self.password_entry.get()
#         # Here you can add your logic to save the user to the database
#         user = Users(first_name, last_name, email, password)
#         print(f"Utilisateur {user.first_name} enregistré avec succès !")    

# # Run the interface
# app = RegisterInterface()
