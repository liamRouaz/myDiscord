from tkinter import Label, SUNKEN
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

class Interface_sport():
    # fenetre
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.geometry("600x700")
        self.screen.title("MyDiscord")
        self.screen.resizable(False, False)
        #fenetre.configure(background="#343541")
        
        
    def background_image(self): 
        # Créer un Canvas pour afficher l'image
        canvas = tk.Canvas(self.screen, width=600, height=700)
        canvas.pack()

        # Charger l'image et l'afficher dans le Canvas
        self.image_background = Image.open("background_sport.png")
        self.image_background = self.image_background.resize((600,  1000), Image.LANCZOS)  # Redimensionner l'image à la taille souhaitée
        self.photo_background = ImageTk.PhotoImage(self.image_background)  # Store the image object as an instance variable
        canvas.create_image(62,  50, anchor=tk.NW, image=self.photo_background)  # Use the instance variable here

    def ajouter_titre(self):
        #ajouter le titre
        titre = Label(self.screen, borderwidth = 8, relief = SUNKEN,
                    text = "SALON SPORT", font = ("sans serif", 25),
                    background = "#000000", foreground = "#FFFAFA")
        titre.place(x=0, y=0, width = 600, height = 50)

    def colonne_salon(self):
        # ajout colonne de gauche
        colonne = Label(self.screen, borderwidth = 8, relief = SUNKEN,
                        text = "Salons disponibles", font = ("sans serif", 12),
                        background = "#000000", foreground = "#FFFAFA")
        colonne.place(x=0, y=50, width=160, height=650)
        colonne.config(anchor=tk.NW)

    def case_texte(self):
        # case de saisie de texte
        text_input=Text(self.screen, width=40, height=5, relief=SUNKEN)
        text_input.place(x=180, y=600)

    def changer_fenetre_sport(self):
        self.screen.destroy()  # Fermer la première fenêtre
        from interface_sport import ALL #import Interface_sport  # Importer le deuxième fichier

    def changer_fenetre_manga(self):
        self.screen.destroy()
        from interface_manga import ALL

    def changer_fenetre_cinema(self):
        self.screen.destroy()
        from interface_cinema import ALL

    def btn_send(self):
        # bouton envoyer
        btn_envoyer = Button(self.screen, text="Envoyer")
        btn_envoyer.place(x=520, y=630)

    def btn_sport(self):
        # bouton salon sport
        self.image_ballon = Image.open("logo_sport.png")
        self.image_ballon = self.image_ballon.resize((50, 50), Image.LANCZOS)
        self.image_ballon = ImageTk.PhotoImage(self.image_ballon)
        btn_canalsport = Button(self.screen, image=self.image_ballon, text="Sport", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.changer_fenetre_sport)
        btn_canalsport.place(x=10, y=100)

    def btn_cinema(self):
        #bouton salon cinéma
        self.image_bobine = Image.open("logo_dvd.png")
        self.image_bobine = self.image_bobine.resize((50, 50), Image.LANCZOS)
        self.image_bobine = ImageTk.PhotoImage(self.image_bobine)
        btn_canalcinema = Button(self.screen, image=self.image_bobine, text="Cinéma", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.changer_fenetre_cinema)
        btn_canalcinema.place(x=10, y=180)

    def btn_manga(self):
        # bouton salon manga
        self.image_boule = Image.open("logo_manga.png")
        self.image_boule = self.image_boule.resize((50, 50),  Image.LANCZOS)
        self.image_boule = ImageTk.PhotoImage(self.image_boule)
        btn_canalmanga = Button(self.screen, image=self.image_boule, text="Manga", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.changer_fenetre_manga)
        btn_canalmanga.place(x=10, y=260)

    def btn_disconnect(self):
        # bouton déconnexion
        btn_deconnexion = Button(self.screen, text="Déconnexion")
        btn_deconnexion.place(x=30, y=10)


interface_sport = Interface_sport()
interface_sport.background_image()
interface_sport.ajouter_titre()
interface_sport.colonne_salon()
interface_sport.case_texte()
interface_sport.btn_send()
interface_sport.btn_sport()
interface_sport.btn_cinema()
interface_sport.btn_manga()
interface_sport.btn_disconnect()

interface_sport.screen.mainloop() 