from tkinter import Label, SUNKEN
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

# fenetre
fenetre = tkinter.Tk()
fenetre.geometry("600x700")
fenetre.title("MyDiscord")
fenetre.resizable(False, False)
#fenetre.configure(background="#343541")

# Créer un Canvas pour afficher l'image
canvas = tk.Canvas(fenetre, width=600, height=700)
canvas.pack()

# Charger l'image et l'afficher dans le Canvas
image_background = Image.open("background_cinema.png")
image_background = image_background.resize((600, 1000), Image.LANCZOS)  # Redimensionner l'image à la taille souhaitée
photo_background = ImageTk.PhotoImage(image_background)
canvas.create_image(62, 50, anchor=tk.NW, image=photo_background)  # Positionner l'image dans le Canvas

#ajouter le titre
titre = Label(fenetre, borderwidth = 8, relief = SUNKEN,
              text = "SALON CINEMA", font = ("sans serif", 25),
              background = "#000000", foreground = "#FFFAFA")
titre.place(x=0, y=0, width = 600, height = 50)

# ajout colonne de gauche
colonne = Label(fenetre, borderwidth = 8, relief = SUNKEN,
                text = "Salons disponibles", font = ("sans serif", 12),
                background = "#000000", foreground = "#FFFAFA")
colonne.place(x=0, y=50, width=160, height=650)
colonne.config(anchor=tk.NW)


# case de saisie de texte
text_input=Text(fenetre, width=40, height=5, relief=SUNKEN)
text_input.place(x=180, y=600)

# bouton envoyer
btn_envoyer = Button(fenetre, text="Envoyer")
btn_envoyer.place(x=520, y=630)

def changer_fenetre_sport():
    fenetre.destroy()  # Fermer la première fenêtre
    from interface_sport import ALL #import Interface_sport  # Importer le deuxième fichier
    #interface_sport = Interface_sport()
    #interface_sport.afficher_interface_sport()  # Appeler la fonction pour afficher la deuxième fenêtre

def changer_fenetre_manga():
    fenetre.destroy()
    from interface_manga import ALL

def changer_fenetre_cinema():
    fenetre.destroy()
    from interface_cinema import ALL

# bouton salon sport
image_ballon = Image.open("logo_sport.png")
image_ballon = image_ballon.resize((50, 50), Image.LANCZOS)
image_ballon = ImageTk.PhotoImage(image_ballon)
btn_canalsport = Button(fenetre, image=image_ballon, text="Sport", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=changer_fenetre_sport)
btn_canalsport.place(x=10, y=100)

#bouton salon cinéma
image_bobine = Image.open("logo_dvd.png")
image_bobine = image_bobine.resize((50, 50), Image.LANCZOS)
image_bobine = ImageTk.PhotoImage(image_bobine)
btn_canalcinema = Button(fenetre, image=image_bobine, text="Cinéma", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=changer_fenetre_cinema)
btn_canalcinema.place(x=10, y=180)

# bouton salon manga
image_boule = Image.open("logo_manga.png")
image_boule = image_boule.resize((50, 50),  Image.LANCZOS)
image_boule = ImageTk.PhotoImage(image_boule)
btn_canalmanga = Button(fenetre, image=image_boule, text="Manga", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=changer_fenetre_manga)
btn_canalmanga.place(x=10, y=260)

# bouton déconnexion
btn_deconnexion = Button(fenetre, text="Déconnexion")
btn_deconnexion.place(x=30, y=10)



fenetre.mainloop() #boucle principale 