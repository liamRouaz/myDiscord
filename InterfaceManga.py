import tkinter as tk
from tkinter import ttk, Canvas, Listbox
from datetime import datetime
from PIL import Image, ImageTk
#Pour connecter les interface 
#from interface_connexion import InterfaceConnexion  # Import de l'interface de connexion

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")
        self.root.geometry("600x400")

        # Création de la liste des canaux
        self.channel_list = Listbox(self.root)
        self.channel_list.pack(side="left", fill="y")
        self.channel_list.insert(1, "General 💬")  # Canal général
        self.channel_list.insert(2, "Movie 📀")    # Canal de film
        self.channel_list.insert(3, "Sport 🏓")    # Canal de sport
        self.channel_list.insert(4, "Manga 📖")    # Canal de manga
        self.channel_list.bind("<<ListboxSelect>>", self.select_channel)

        # Création de la liste des messages
        self.message_list = tk.Text(self.root, wrap="word")
        self.message_list.pack(side="top", fill="both", expand=True)

        # Frame pour le champ de saisie et le bouton d'envoi
        text_channel_frame = ttk.Frame(self.root)
        text_channel_frame.pack(side="bottom", fill="x")

        # Champ de saisie pour le message
        self.message_entry = tk.Entry(text_channel_frame, width=30)
        self.message_entry.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

        # Bouton pour envoyer les messages
        send_button = tk.Button(text_channel_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Bouton pour quitter
        quit_button = tk.Button(text_channel_frame, text="Quit", command=self.quit_app)
        quit_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def send_message(self):
        message = self.message_entry.get()
        self.message_entry.delete(0, tk.END)
        if message:
            self.display_message("You", message, sent=True)

    def display_message(self, user, message, sent=False):
        timestamp = datetime.now().strftime("%H:%M:%S")
        date = datetime.now().strftime("%Y-%m-%d")
        formatted_message = f"[{date} {timestamp}] {user}: {message}\n"
        tag = "sent" if sent else "received"
        self.message_list.insert(tk.END, formatted_message)
        self.message_list.see(tk.END)

    def select_channel(self, event=None):
        selected_channel = self.channel_list.get(self.channel_list.curselection())
        self.message_list.delete(1.0, tk.END)
        self.display_message("System", f"You're now in {selected_channel} channel.")

    def receive_messages(self):
        # Placeholder: logique pour simuler la réception de messages
        messages = [("Sender", "Sample message")]
        for sender, message in messages:
            self.display_message(sender, message)
        # Planifier le prochain appel à receive_messages après un délai aléatoire

    def quit_app(self):
        self.root.destroy()  # Ferme la fenêtre principale
        #InterfaceConnexion()  # Lance l'interface de connexion

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
