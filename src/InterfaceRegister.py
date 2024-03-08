import tkinter as tk
from Users import Users



class InterfaceRegister():
    def __init__(self):
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

    def enter_first_name(self):
        # Création et placement du label et du champ de saisie pour le prénom
        self.label_first_name = tk.Label(self.screen, text="Prenom", bg="#61008E", font='ROGFonts-Regular')
        self.label_first_name.place(x=240, y=200)
        

        self.entry_first_name = tk.Entry(self.screen, bg="#AC66FB")
        self.entry_first_name.place(x=190, y=230, width=200, height=30)

    def enter_last_name(self):
        # Création et placement du label et du champ de saisie pour le nom
        self.label_last_name = tk.Label(self.screen, text="Nom", bg="#61008E", font='ROGFonts-Regular')
        self.label_last_name.place(x=260, y=280)
        

        self.entry_last_name = tk.Entry(self.screen, bg="#AC66FB")
        self.entry_last_name.place(x=190, y=310, width=200, height=30)

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

    def confirm_password(self):
        # Création et placement du label et du champ de saisie pour la vérification du mot de passe
        self.label_confirm_password = tk.Label(self.screen, text="Verification du mot de passe", bg="#61008E", font='ROGFonts-Regular')
        self.label_confirm_password.place(x=90, y=520)
        

        self.entry_confirm_password = tk.Entry(self.screen, bg="#AC66FB", show="*")
        self.entry_confirm_password.place(x=190, y=550, width=200, height=30)

    def btn_register(self):
        # Création et placement du bouton d'inscription
        self.button_login = tk.Button(self.screen, text="Creer compte", bg="#BC1A86", font='ROGFonts-Regular', command=self.register_user)
        self.button_login.place(x=180, y=620)

    
    def create_user(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        if password != confirm_password:
            print("Password confirmation does not match")
            return

        user_info = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }
        user = Users()
        user.create_user(**user_info)

    def register_user(self):
        self.create_user()

if __name__ == "__main__":
    HOST = '10.10.0.38'
    PORT = 5000
    #app = InterfaceRegister()


interfacelogin = InterfaceRegister()
interfacelogin.background_image()
interfacelogin.enter_first_name()
interfacelogin.enter_last_name()
interfacelogin.enter_email()
interfacelogin.enter_password()
interfacelogin.confirm_password()
interfacelogin.btn_register()
interfacelogin.screen.mainloop()  # Démarrer la boucle principale après la création des widgets
