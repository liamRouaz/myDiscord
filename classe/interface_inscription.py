import tkinter as tk
from Users import Users
from ChatServeur import ChatServeur

class InterfaceInscription:
    def __init__(self, server):
        self.server = server
        self.root = tk.Tk()
        self.root.title("Inscription")
        self.root.geometry("600x800")
        
        self.first_name_label = tk.Label(self.root, text="First Name:")
        self.first_name_entry = tk.Entry(self.root)
        self.last_name_label = tk.Label(self.root, text="Last Name:")
        self.last_name_entry = tk.Entry(self.root)
        self.email_label = tk.Label(self.root, text="Email:")
        self.email_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root, show="*")
        self.confirm_password_label = tk.Label(self.root, text="Confirm Password:")
        self.confirm_password_entry = tk.Entry(self.root, show="*")
        
        self.register_button = tk.Button(self.root, text="Inscription", command=self.register)
        
        self.first_name_label.grid(row=0, column=0)
        self.first_name_entry.grid(row=0, column=1)
        self.last_name_label.grid(row=1, column=0)
        self.last_name_entry.grid(row=1, column=1)
        self.email_label.grid(row=2, column=0)
        self.email_entry.grid(row=2, column=1)
        self.password_label.grid(row=3, column=0)
        self.password_entry.grid(row=3, column=1)
        self.confirm_password_label.grid(row=4, column=0)
        self.confirm_password_entry.grid(row=4, column=1)

        self.register_button.grid(row=5, column=1)
        
        self.root.mainloop()
    
    def create_user(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        if password != confirm_password:
            print("Password confirmation does not match")
            return

        user_info = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }

        user = Users(first_name, last_name, email, password, '10.10.94.117', 5000)
        user.register_user(**user_info)  # Utilisation de l'opérateur ** pour déballer le dictionnaire

    def register(self):
        self.create_user()

# Run the interface
server = ChatServeur("10.10.94.117", 5000) 
app = InterfaceInscription(server)


# import tkinter as tk
# from Users import Users

# class InterfaceInscription:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Inscription")
#         self.root.geometry("600x800")
        
#         self.first_name_label = tk.Label(self.root, text="First Name:")
#         self.first_name_entry = tk.Entry(self.root)
#         self.last_name_label = tk.Label(self.root, text="Last Name:")
#         self.last_name_entry = tk.Entry(self.root)
#         self.email_label = tk.Label(self.root, text="Email:")
#         self.email_entry = tk.Entry(self.root)
#         self.password_label = tk.Label(self.root, text="Password:")
#         self.password_entry = tk.Entry(self.root, show="*")
#         self.confirm_password_label = tk.Label(self.root, text="Confirm Password:")
#         self.confirm_password_entry = tk.Entry(self.root, show="*")
        
#         self.register_button = tk.Button(self.root, text="Inscription", command=self.register)
        
#         self.first_name_label.grid(row=0, column=0)
#         self.first_name_entry.grid(row=0, column=1)
#         self.last_name_label.grid(row=1, column=0)
#         self.last_name_entry.grid(row=1, column=1)
#         self.email_label.grid(row=2, column=0)
#         self.email_entry.grid(row=2, column=1)
#         self.password_label.grid(row=3, column=0)
#         self.password_entry.grid(row=3, column=1)
#         self.confirm_password_label.grid(row=4, column=0)
#         self.confirm_password_entry.grid(row=4, column=1)

#         self.register_button.grid(row=5, column=1)
        
#         self.root.mainloop()
    
#     def register(self):
#         first_name = self.first_name_entry.get()
#         last_name = self.last_name_entry.get()
#         email = self.email_entry.get()
#         password = self.password_entry.get()
#         confirm_password = self.confirm_password_entry.get()
        
#         if password != confirm_password:
#             print("Password confirmation does not match")
#             return

#         user_info = {
#             "first_name": first_name,
#             "last_name": last_name,
#             "email": email,
#             "password": password
#         }

#         user = Users()
#         user.register_user(user_info)

# # Run the interface
# app = InterfaceInscription()
