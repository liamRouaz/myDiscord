import tkinter as tk
from tkinter import ttk
from datetime import datetime

from ChatClient import ChatClient
from Channel import Channel

class ChatApp:
    def __init__(self, root, chat_client, channels):
        self.root = root
        self.chat_client = chat_client
        self.channels = channels
        self.active_channel_id = None
        self.root.title("My Discord")
        self.root.geometry("600x700")

        # Create the list of channels
        self.channel_list = tk.Listbox(self.root)
        self.channel_list.pack(side="left", fill="y")
        for channel_name in self.channels.keys():
            self.channel_list.insert(tk.END, channel_name)

        # Changer la couleur d'écriture pour tous les éléments de la liste
        for i, channel_name in enumerate(self.channels.keys()):
            color = ["white", "#AC66FB", "#2ecc71", "#FF5733"][i]
            self.channel_list.itemconfigure(i, {'fg': color})

        # Changer la couleur de fond de la liste des canaux
        self.channel_list.configure(bg="#212121")

        # Création de la liste des messages
        self.message_list = tk.Text(self.root, wrap="word")
        self.message_list.pack(side="top", fill="both", expand=True)
        self.message_list.configure(bg="#303134")

        # Frame pour le champ de saisie et le bouton d'envoi
        text_channel_frame = ttk.Frame(self.root, style="Custom.TFrame")
        self.root.style = ttk.Style()
        self.root.style.configure("Custom.TFrame", background="#212121")
        text_channel_frame.pack(side="bottom", fill="x")

        # Champ de saisie pour le message
        self.message_entry = tk.Entry(text_channel_frame, width=30, bg="#5F655B")
        self.message_entry.pack(side=tk.LEFT, padx=5, pady=20, fill=tk.X, expand=True)

        # Bouton pour quitter
        quit_button = tk.Button(text_channel_frame, text="Quitter", command=self.quit_app)
        quit_button.pack(side=tk.RIGHT, padx=5, pady=5)
        quit_button.configure(bg="#61008E", font=('ROGFonts-Regular', 10))

        # Bouton pour envoyer les messages
        send_button = tk.Button(text_channel_frame, text="Envoyer", command=self.send_message)
        send_button.pack(side=tk.RIGHT, padx=5, pady=5)
        send_button.configure(bg="#BC1A86", font=('ROGFonts-Regular', 10))

    def send_message(self):
        message = self.message_entry.get()
        self.message_entry.delete(0, tk.END)
        if message:
            # Envoi du message au serveur via le client
            self.chat_client.insert_message(message, self.active_channel_id)
            
            # Affichage du message dans l'interface utilisateur
            self.display_message("Vous" , message, sent=True)

    def display_message(self, user, message, sent=False):
        timestamp = datetime.now().strftime("%H:%M:%S")
        date = datetime.now().strftime("%Y-%m-%d")
        formatted_message = f"[{date} {timestamp}] {user}: {message}\n"
        tag = "sent" if sent else "received"
        self.message_list.insert(tk.END, formatted_message)
        self.message_list.see(tk.END)

    def receive_messages(self):
        messages = [("Sender", "Sample message")]
        for sender, message in messages:
            self.display_message(sender, message)

    def select_channel(self, event=None):
        if self.channel_list.curselection():
            selected_channel_index = self.channel_list.curselection()[0]
            selected_channel_name = self.channel_list.get(selected_channel_index)
            self.active_channel_id = self.channels[selected_channel_name].id  # Définition de active_channel_id
            self.message_list.delete(1.0, tk.END)
            self.display_message("System", f"You're now in {selected_channel_name} channel.")
        else:
            print("No channel selected.")

    def quit_app(self):
        self.chat_client.close_connection()
        self.root.destroy()

if __name__ == "__main__":
    HOST = "10.10.0.38"
    PORT = 5000

    client = ChatClient(HOST, PORT)  

    root = tk.Tk()
    channels = Channel.get_channels() 
    app = ChatApp(root, client, channels)
    
    client.connect_to_server('email', 'password', 'user_id')
    
    root.mainloop()
