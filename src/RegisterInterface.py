import tkinter as tk
from Users import Users

class RegisterInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MyDiscord")
        self.root.geometry("600x800")
        
        self.first_name_label = tk.Label(self.root, text="Prénom : ")
        self.first_name_entry = tk.Entry(self.root)
        #self.first_name_entry = Users.first_name
        self.last_name_label = tk.Label(self.root, text="Nom : ")
        self.last_name_entry = tk.Entry(self.root)
        #self.last_name_entry = Users.last_name
        self.email_label = tk.Label(self.root, text="Email : ")
        self.email_entry = tk.Entry(self.root)
        #self.email_entry = Users.email
        self.password_label = tk.Label(self.root, text="Mot de passe : ")
        self.password_entry = tk.Entry(self.root)
        #self.password_entry = Users.password
        # self.confirm_password_label = tk.Label(self.root, text="Confirmation mot de passe : ")
        # self.confirm_password_entry = tk.Entry(self.root, show="*")
        
        self.register_button = tk.Button(self.root, text="Inscription", command=self.register_user)
        
        self.first_name_label.grid(row=0, column=0)
        self.first_name_entry.grid(row=0, column=1)
        self.last_name_label.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)
        self.email_label.grid(row=2, column=0)
        self.email_entry.grid(row=2, column=1)
        self.password_label.grid(row=5, column=0)
        self.password_entry.grid(row=5, column=1)
        # self.confirm_password_label.grid(row=6, column=0)
        # self.confirm_password_entry.grid(row=6, column=1)

        self.register_button.grid(row=7, column=1)
        
        self.root.mainloop()
    
    def register(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        #confirm_password = self.confirm_password_entry.get()
        
       
        self.register_user(first_name, last_name, email, password)

    def register_user(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Here you can add your logic to save the user to the database
        user = Users(first_name, last_name, email, password)
        print(f"Utilisateur {user.first_name} enregistré avec succès !")    

# Run the interface
app = RegisterInterface()
