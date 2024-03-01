import tkinter as tk
from tkinter import Text, Button, Label, SUNKEN, END
from PIL import Image, ImageTk
from datetime import datetime

class InterfaceManga():
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.geometry("600x700")
        self.screen.title("MyDiscord")
        self.screen.resizable(False, False)
        self.background_image()
        self.add_title()
        self.conversation()
        self.column_saloon()
        self.input_text()
        self.btn_send()
        self.btn_sport()
        self.btn_movie()
        self.btn_manga()
        self.btn_disconnect()

    def background_image(self):
        canvas = tk.Canvas(self.screen, width=600, height=700)
        canvas.pack()
        self.image_background = Image.open("assets/background_manga.png")
        self.image_background = self.image_background.resize((600, 700), Image.LANCZOS)
        self.photo_background = ImageTk.PhotoImage(self.image_background)
        canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_background)

        # Ajouter un texte sur le canevas pour afficher les messages
        self.text_output = canvas.create_text(10, 10, anchor=tk.NW, text="", fill="white", font=("Comic sans MS", 10))

    def add_title(self):
        image_title = Image.open("assets/cieletoiles1.png")
        photo_title = ImageTk.PhotoImage(image_title)
        canvas = tk.Canvas(self.screen, borderwidth=0, highlightthickness=0, background="#343541", width=600, height=50)
        canvas.place(x=0, y=0)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo_title)
        canvas.create_text(200, 5, anchor=tk.NW, text="SALON MANGA", fill="#BC1A86", font=("ROGFonts-Regular", 25))
        canvas.update()
        canvas.image = photo_title

    def conversation(self):
        canvas1 = tk.Canvas(self.screen, borderwidth=0, highlightthickness=0, background="#343541", width=380, height=520)
        canvas1.place(x=180, y=70)
        

    def column_saloon(self):
        image = Image.open("assets/cieletoiles1.png")
        photo = ImageTk.PhotoImage(image)
        canvas = tk.Canvas(self.screen, borderwidth=0, highlightthickness=0, background="#343541", width=160, height=650)
        canvas.place(x=0, y=50)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.create_text(10, 10, anchor=tk.NW, text="Salons disponibles", fill="#BC1A86", font=("ROGFonts-Regular", 7))
        canvas.update()
        canvas.image = photo

    def input_text(self):
        self.text_input = Text(self.screen, width=40, height=5, relief=SUNKEN, background="#212121", foreground="white", font=("Comic sans MS", 10))
        self.text_input.place(x=180, y=600)

    def btn_send(self):
        btn_envoyer = Button(self.screen, text="Envoyer", background="#BC1A86", font=("ROGFonts-Regular", 8), command=self.send_message)
        btn_envoyer.place(x=510, y=630)

    def send_message(self):
        message = self.text_input.get("1.0", tk.END).strip()
        self.text_input.delete("1.0", tk.END)
        if message:
            self.display_message("You", message)

    def display_message(self, user, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {user}: {message}\n"
        self.text_input.insert(tk.END, formatted_message)

    def btn_sport(self):
        self.image_ballon = Image.open("assets/logo_sport.png")
        self.image_ballon = self.image_ballon.resize((50, 50), Image.LANCZOS)
        self.image_ballon = ImageTk.PhotoImage(self.image_ballon)
        btn_canalsport = Button(self.screen, image=self.image_ballon, text="Sport", compound=tk.LEFT, font=("ROGFonts-Regular", 10), foreground="#61008E", width=130, anchor=tk.W, bg="black", command=self.change_screen_sport)
        btn_canalsport.place(x=10, y=100)

    def btn_movie(self):
        self.image_bobine = Image.open("assets/logo_dvd.png")
        self.image_bobine = self.image_bobine.resize((50, 50), Image.LANCZOS)
        self.image_bobine = ImageTk.PhotoImage(self.image_bobine)
        btn_canalcinema = Button(self.screen, image=self.image_bobine, text="Cinema", compound=tk.LEFT, font=("ROGFonts-Regular", 10), foreground="#AC66FB", width=130, anchor=tk.W, bg="black", command=self.change_screen_movie)
        btn_canalcinema.place(x=10, y=180)

    def btn_manga(self):
        self.image_boule = Image.open("assets/logo_manga.png")
        self.image_boule = self.image_boule.resize((50, 50), Image.LANCZOS)
        self.image_boule = ImageTk.PhotoImage(self.image_boule)
        btn_canalmanga = Button(self.screen, image=self.image_boule, text="Manga", compound=tk.LEFT, font=("ROGFonts-Regular", 10), foreground="#BC1A86", width=130, anchor=tk.W, bg="black", command=self.change_screen_manga)
        btn_canalmanga.place(x=10, y=260)

    def btn_disconnect(self):
        btn_deconnexion = Button(self.screen, text="Deconnexion", font=("ROGFonts-Regular", 8), background="#BC1A86")
        btn_deconnexion.place(x=20, y=10)

    def change_screen_sport(self):
        self.screen.destroy()  
        #from InterfaceSport import ALL #import Interface_sport  
        
    def change_screen_manga(self):
        self.screen.destroy()
        #from InterfaceManga import ALL

    def change_screen_movie(self):
        self.screen.destroy()
        #from InterfaceMovie import ALL


interface_manga = InterfaceManga()
interface_manga.screen.mainloop()
# import tkinter as tk
# from tkinter import ttk
# from datetime import datetime
    # def change_screen_sport(self):
    #     self.screen.destroy()  # Fermer la première fenêtre
    #     from InterfaceSport import ALL #import Interface_sport  # Importer le deuxième fichier

    # def change_screen_manga(self):
    #     self.screen.destroy()
    #     from InterfaceManga import ALL

    # def change_screen_movie(self):
    #     self.screen.destroy()
    #     from InterfaceMovie import ALL
# class ChatApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chat App")
#         self.root.geometry("600x400")

#         self.message_list = tk.Text(self.root, wrap="word")
#         self.message_list.pack(fill="both", expand=True)

#         scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.message_list.yview)
#         scrollbar.pack(side="right", fill="y")
#         self.message_list.config(yscrollcommand=scrollbar.set)

#         self.message_entry = tk.Entry(self.root)
#         self.message_entry.pack(fill="x")

#         send_button = tk.Button(self.root, text="Send", command=self.send_message)
#         send_button.pack()

#         # Configuration des balises pour l'alignement du texte à droite
#         self.message_list.tag_configure("right", justify="right")

#     def send_message(self):
#         message = self.message_entry.get()
#         self.message_entry.delete(0, tk.END)
#         if message:
#             self.display_message("You", message, sent=True)

#     def display_message(self, user, message, sent=False):
#         timestamp = datetime.now().strftime("%H:%M:%S")
#         date = datetime.now().strftime("%Y-%m-%d")
#         formatted_message = f"[{date} {timestamp}] {user}: {message}\n"

#         if sent:
#             tag = "right"  # Utilisation de la balise "right" pour aligner le texte à droite
#         else:
#             tag = ""  # Pas de balise pour les messages reçus (alignement par défaut à gauche)
           

#         self.message_list.insert("end", formatted_message, tag)
#         self.message_list.see("end")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ChatApp(root)
#     root.mainloop()




# import tkinter as tk
# from tkinter import ttk
# from datetime import datetime

# class ChatApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Chat App")
#         self.root.geometry("600x400")

#         self.message_list = tk.Text(self.root, wrap="word")
#         self.message_list.pack(fill="both", expand=True)

#         scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.message_list.yview)
#         scrollbar.pack(side="right", fill="y")
#         self.message_list.config(yscrollcommand=scrollbar.set)

#         self.message_entry = tk.Entry(self.root)
#         self.message_entry.pack(fill="x")

#         send_button = tk.Button(self.root, text="Send", command=self.send_message)
#         send_button.pack()

#     def send_message(self):
#         message = self.message_entry.get()
#         self.message_entry.delete(0, tk.END)
#         if message:
#             self.display_message("You", message, sent=True)

#     def display_message(self, user, message, sent=False):
#         timestamp = datetime.now().strftime("%H:%M:%S")
#         date = datetime.now().strftime("%Y-%m-%d")
#         formatted_message = f"[{date} {timestamp}] {user}: {message}\n"

#         message_frame = tk.Frame(self.message_list)
#         message_frame.pack(fill="both", expand=True, padx=5, pady=2)  # Ajout de padding pour l'espace entre les messages

#         if sent:
#             background = "blue"
#         else:
#             background = "red"

#         message_label = tk.Label(message_frame, text=formatted_message, background=background, padx=5, pady=5, wraplength=500, justify="left" if not sent else "right")
#         message_label.pack(fill="both", expand=True)

#         self.message_list.window_create("end", window=message_frame)
#         self.message_list.insert("end", "\n")  # Nouvelle ligne pour afficher le message

#         self.message_list.see("end")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ChatApp(root)
#     root.mainloop()