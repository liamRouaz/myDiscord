import tkinter as tk

class ConnexionInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connexion ")
        self.root.geometry("600x800")
        
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root, show="*")
        
        self.login_button = tk.Button(self.root, text="Connexion", command=self.login)
        self.register_button = tk.Button(self.root, text="Inscription", command=self.register)
        
        self.username_label.grid(row=0, column=0)
        self.username_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)
        self.login_button.grid(row=2, column=0)
        self.register_button.grid(row=2, column=1)
        
        self.root.mainloop()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Implement your login logic here
        user_id = self.authenticate_user(username, password)
        if user_id:
            print(f"Logged in successfully with user id {user_id}")
        else:
            print("Invalid username or password")
    
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Implement your registration logic here
        print(f"Attempting to register with username {username} and password {password}")
    
    def authenticate_user(self, email, password):
        # This is a placeholder for your actual database connection and query
        # Replace this with your actual database query logic
        # For example, if you are using SQLite, you would use a cursor to execute the query
        query = "SELECT id FROM users WHERE email = %s AND password = %s"
        params = (email, password)
        result = self.db.fetch_data(query, params)
        return result[0][0] if result else None

app = ConnexionInterface()
