from tkinter import Label, SUNKEN
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

class InterfaceSport():
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
        self.image_background = Image.open("assets/background_sport.png")
        self.image_background = self.image_background.resize((600,  1000), Image.LANCZOS)  # Redimensionner l'image à la taille souhaitée
        self.photo_background = ImageTk.PhotoImage(self.image_background)  # Store the image object as an instance variable
        canvas.create_image(62,  50, anchor=tk.NW, image=self.photo_background)  # Use the instance variable here

    def add_title(self):
        # Charger l'image à utiliser comme arrière-plan du titre
        image_title = Image.open("assets/cieletoiles1.png")  # Assurez-vous que le format de l'image prend en charge la transparence (PNG)
        photo_title = ImageTk.PhotoImage(image_title)

        # Créer un canevas pour afficher l'image en arrière-plan
        canvas = Canvas(self.screen, borderwidth=0, highlightthickness=0, background="#343541", width=600, height=50)
        canvas.place(x=0, y=0)

        # Ajouter l'image en arrière-plan du canevas
        canvas.create_image(0, 0, anchor=tk.NW, image=photo_title)

        # Ajouter le texte sur le canevas avec un fond transparent
        canvas.create_text(200, 5, anchor=tk.NW, text="SALON SPORT", fill="#61008E", font=("ROGFonts-Regular", 25))

        # Rafraîchir le canevas pour afficher les changements
        canvas.update()

        # Gardez une référence à l'image pour éviter la garbage collection
        canvas.image = photo_title

    def column_saloon(self):
        # Charger l'image à utiliser comme arrière-plan
        image = Image.open("assets/cieletoiles1.png")  # Assurez-vous que le format de l'image prend en charge la transparence (PNG)
        photo = ImageTk.PhotoImage(image)

        # Créer le canevas avec l'image en arrière-plan
        canvas = Canvas(self.screen, borderwidth=0, highlightthickness=0, background="#343541", width=160, height=650)
        canvas.place(x=0, y=50)

        # Ajouter l'image en arrière-plan du canevas
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)

        # Ajouter le texte sur le canevas avec un fond transparent
        canvas.create_text(10, 10, anchor=tk.NW, text="Salons disponibles", fill="#FFFAFA", font=("ROGFonts-Regular", 7))

        # Rafraîchir le canevas pour afficher les changements
        canvas.update()

        # Gardez une référence à l'image pour éviter la garbage collection
        canvas.image = photo

    # def column_saloon(self):
    #     # Charger l'image à utiliser comme arrière-plan
    #     image_column = Image.open("assets/cieletoiles1.png")
    #     photo_column = ImageTk.PhotoImage(image_column)

    #     # Créer le label avec l'image en arrière-plan
    #     colonne = Label(self.screen, borderwidth=8, relief=SUNKEN,
    #                     text="Salons disponibles", font=("ROGFonts-Regular", 7),
    #                     background="#000000", foreground="#FFFAFA", image=photo_column, compound=tk.CENTER)
    #     colonne.image = photo_column  # Conserver une référence à l'image pour éviter la garbage collection
    #     colonne.place(x=0, y=50, width=160, height=650)
    #     colonne.config(anchor=tk.NW)

    # def column_saloon(self):
    #     # ajout colonne de gauche
    #     colonne = Label(self.screen, borderwidth = 8, relief = SUNKEN,
    #                     text = "Salons disponibles", font = ("ROGFonts-Regular", 7),
    #                     background = "#000000", foreground = "#FFFAFA")
    #     colonne.place(x=0, y=50, width=160, height=650)
    #     colonne.config(anchor=tk.NW)

    def input_text(self):
        # case de saisie de texte
        text_input=Text(self.screen, width=40, height=5, relief=SUNKEN, background="#212121", foreground="white", font=("Comic sans MS", 10))
        text_input.place(x=180, y=600)

    def change_screen_sport(self):
        self.screen.destroy()  # Fermer la première fenêtre
        from InterfaceSport import ALL #import Interface_sport  # Importer le deuxième fichier

    def change_screen_manga(self):
        self.screen.destroy()
        from InterfaceManga import ALL

    def change_screen_movie(self):
        self.screen.destroy()
        from InterfaceMovie import ALL

    def btn_send(self):
        # bouton envoyer
        btn_envoyer = Button(self.screen, text="Envoyer", background="#BC1A86", font = ("ROGFonts-Regular", 8))
        btn_envoyer.place(x=510, y=630)

    def btn_sport(self):
        # bouton salon sport
        self.image_ballon = Image.open("assets/logo_sport.png")
        self.image_ballon = self.image_ballon.resize((50, 50), Image.LANCZOS)
        self.image_ballon = ImageTk.PhotoImage(self.image_ballon)
        btn_canalsport = Button(self.screen, image=self.image_ballon, text="Sport", compound=tk.LEFT, font = ("ROGFonts-Regular", 10), foreground = "#61008E", width=130, anchor=tk.W, bg="black", command=self.change_screen_sport)
        btn_canalsport.place(x=10, y=100)

    def btn_movie(self):
        #bouton salon cinéma
        self.image_bobine = Image.open("assets/logo_dvd.png")
        self.image_bobine = self.image_bobine.resize((50, 50), Image.LANCZOS)
        self.image_bobine = ImageTk.PhotoImage(self.image_bobine)
        btn_canalcinema = Button(self.screen, image=self.image_bobine, text="Cinema", compound=tk.LEFT, font = ("ROGFonts-Regular", 10), foreground = "#AC66FB", width=130, anchor=tk.W, bg="black", command=self.change_screen_movie)
        btn_canalcinema.place(x=10, y=180)

    def btn_manga(self):
        # bouton salon manga
        self.image_boule = Image.open("assets/logo_manga.png")
        self.image_boule = self.image_boule.resize((50, 50),  Image.LANCZOS)
        self.image_boule = ImageTk.PhotoImage(self.image_boule)
        btn_canalmanga = Button(self.screen, image=self.image_boule, text="Manga", compound=tk.LEFT, font = ("ROGFonts-Regular", 10), foreground = "#BC1A86", width=130, anchor=tk.W, bg="black", command=self.change_screen_manga)
        btn_canalmanga.place(x=10, y=260)

    def btn_disconnect(self):
        # bouton déconnexion
        btn_deconnexion = Button(self.screen, text="Deconnexion", font = ("ROGFonts-Regular", 8), background="#BC1A86")
        btn_deconnexion.place(x=20, y=10)


interface_sport = InterfaceSport()
interface_sport.background_image()
interface_sport.add_title()
interface_sport.column_saloon()
interface_sport.input_text()
interface_sport.btn_send()
interface_sport.btn_sport()
interface_sport.btn_movie()
interface_sport.btn_manga()
interface_sport.btn_disconnect()
interface_sport.screen.mainloop() 


# from tkinter import Label, SUNKEN
# import tkinter
# from tkinter import *
# from PIL import Image, ImageTk
# import tkinter as tk

# class InterfaceMovie():
#     # fenetre
#     def __init__(self):
#         self.screen = tk.Tk()
#         self.screen.geometry("600x700")
#         self.screen.title("MyDiscord")
#         self.screen.resizable(False, False)
#         #fenetre.configure(background="#343541")
        
        
#     def background_image(self):
#         # Créer un Canvas pour afficher l'image
#         canvas = tk.Canvas(self.screen, width=600, height=700)
#         canvas.pack()

#         # Charger l'image et l'afficher dans le Canvas
#         self.image_background = Image.open("assets/background_cinema.png")
#         self.image_background = self.image_background.resize((600,  1000), Image.LANCZOS)  # Redimensionner l'image à la taille souhaitée
#         self.photo_background = ImageTk.PhotoImage(self.image_background)  # Store the image object as an instance variable
#         canvas.create_image(62,  50, anchor=tk.NW, image=self.photo_background)  # Use the instance variable here

#     def add_title(self):
#         # Charger l'image à utiliser comme arrière-plan du titre
#         image_title = Image.open("assets/cieletoiles1.png")  # Assurez-vous que le format de l'image prend en charge la transparence (PNG)
#         photo_title = ImageTk.PhotoImage(image_title)

#         # Créer un canevas pour afficher l'image en arrière-plan
#         canvas = Canvas(self.screen, borderwidth=0, highlightthickness=0, background="#343541", width=600, height=50)
#         canvas.place(x=0, y=0)

#         # Ajouter l'image en arrière-plan du canevas
#         canvas.create_image(0, 0, anchor=tk.NW, image=photo_title)

#         # Ajouter le texte sur le canevas avec un fond transparent
#         canvas.create_text(200, 5, anchor=tk.NW, text="SALON SPORT", fill="#AC66FB", font=("ROGFonts-Regular", 25))

#         # Rafraîchir le canevas pour afficher les changements
#         canvas.update()

#         # Gardez une référence à l'image pour éviter la garbage collection
#         canvas.image = photo_title

#     def column_saloon(self):
#         # Charger l'image à utiliser comme arrière-plan
#         image = Image.open("assets/cieletoiles1.png")  # Assurez-vous que le format de l'image prend en charge la transparence (PNG)
#         photo = ImageTk.PhotoImage(image)

#         # Créer le canevas avec l'image en arrière-plan
#         canvas = Canvas(self.screen, borderwidth=0, highlightthickness=0, background="#343541", width=160, height=650)
#         canvas.place(x=0, y=50)

#         # Ajouter l'image en arrière-plan du canevas
#         canvas.create_image(0, 0, anchor=tk.NW, image=photo)

#         # Ajouter le texte sur le canevas avec un fond transparent
#         canvas.create_text(10, 10, anchor=tk.NW, text="Salons disponibles", fill="#FFFAFA", font=("ROGFonts-Regular", 7))

#         # Rafraîchir le canevas pour afficher les changements
#         canvas.update()

#         # Gardez une référence à l'image pour éviter la garbage collection
#         canvas.image = photo

#     # def column_saloon(self):
#     #     # Charger l'image à utiliser comme arrière-plan
#     #     image_column = Image.open("assets/cieletoiles1.png")
#     #     photo_column = ImageTk.PhotoImage(image_column)

#     #     # Créer le label avec l'image en arrière-plan
#     #     colonne = Label(self.screen, borderwidth=8, relief=SUNKEN,
#     #                     text="Salons disponibles", font=("ROGFonts-Regular", 7),
#     #                     background="#000000", foreground="#FFFAFA", image=photo_column, compound=tk.CENTER)
#     #     colonne.image = photo_column  # Conserver une référence à l'image pour éviter la garbage collection
#     #     colonne.place(x=0, y=50, width=160, height=650)
#     #     colonne.config(anchor=tk.NW)

#     # def column_saloon(self):
#     #     # ajout colonne de gauche
#     #     colonne = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#     #                     text = "Salons disponibles", font = ("ROGFonts-Regular", 7),
#     #                     background = "#000000", foreground = "#FFFAFA")
#     #     colonne.place(x=0, y=50, width=160, height=650)
#     #     colonne.config(anchor=tk.NW)

#     def input_text(self):
#         # case de saisie de texte
#         text_input=Text(self.screen, width=40, height=5, relief=SUNKEN, background="#212121", foreground="white", font=("Comic sans MS", 10))
#         text_input.place(x=180, y=600)

#     def change_screen_sport(self):
#         self.screen.destroy()  # Fermer la première fenêtre
#         from InterfaceSport import ALL #import Interface_sport  # Importer le deuxième fichier

#     def change_screen_manga(self):
#         self.screen.destroy()
#         from InterfaceManga import ALL

#     def change_screen_movie(self):
#         self.screen.destroy()
#         from InterfaceMovie import ALL

#     def btn_send(self):
#         # bouton envoyer
#         btn_envoyer = Button(self.screen, text="Envoyer", background="#BC1A86", font = ("ROGFonts-Regular", 8))
#         btn_envoyer.place(x=510, y=630)

#     def btn_sport(self):
#         # bouton salon sport
#         self.image_ballon = Image.open("assets/logo_sport.png")
#         self.image_ballon = self.image_ballon.resize((50, 50), Image.LANCZOS)
#         self.image_ballon = ImageTk.PhotoImage(self.image_ballon)
#         btn_canalsport = Button(self.screen, image=self.image_ballon, text="Sport", compound=tk.LEFT, font = ("ROGFonts-Regular", 10), foreground = "#61008E", width=130, anchor=tk.W, bg="black", command=self.change_screen_sport)
#         btn_canalsport.place(x=10, y=100)

#     def btn_movie(self):
#         #bouton salon cinéma
#         self.image_bobine = Image.open("assets/logo_dvd.png")
#         self.image_bobine = self.image_bobine.resize((50, 50), Image.LANCZOS)
#         self.image_bobine = ImageTk.PhotoImage(self.image_bobine)
#         btn_canalcinema = Button(self.screen, image=self.image_bobine, text="Cinema", compound=tk.LEFT, font = ("ROGFonts-Regular", 10), foreground = "#AC66FB", width=130, anchor=tk.W, bg="black", command=self.change_screen_movie)
#         btn_canalcinema.place(x=10, y=180)

#     def btn_manga(self):
#         # bouton salon manga
#         self.image_boule = Image.open("assets/logo_manga.png")
#         self.image_boule = self.image_boule.resize((50, 50),  Image.LANCZOS)
#         self.image_boule = ImageTk.PhotoImage(self.image_boule)
#         btn_canalmanga = Button(self.screen, image=self.image_boule, text="Manga", compound=tk.LEFT, font = ("ROGFonts-Regular", 10), foreground = "#BC1A86", width=130, anchor=tk.W, bg="black", command=self.change_screen_manga)
#         btn_canalmanga.place(x=10, y=260)

#     def btn_disconnect(self):
#         # bouton déconnexion
#         btn_deconnexion = Button(self.screen, text="Deconnexion", font = ("ROGFonts-Regular", 8), background="#BC1A86")
#         btn_deconnexion.place(x=20, y=10)


# movie_interface = InterfaceMovie()
# movie_interface.background_image()
# movie_interface.add_title()
# movie_interface.column_saloon()
# movie_interface.input_text()
# movie_interface.btn_send()
# movie_interface.btn_sport()
# movie_interface.btn_movie()
# movie_interface.btn_manga()
# movie_interface.btn_disconnect()
# movie_interface.screen.mainloop() 


# from tkinter import Label, SUNKEN
# import tkinter
# from tkinter import *
# from PIL import Image, ImageTk
# import tkinter as tk

# class InterfaceSport():
#     # fenetre
#     def __init__(self):
#         self.screen = tk.Tk()
#         self.screen.geometry("600x700")
#         self.screen.title("MyDiscord")
#         self.screen.resizable(False, False)
#         #fenetre.configure(background="#343541")
        
        
#     def background_image(self): 
#         # Créer un Canvas pour afficher l'image
#         canvas = tk.Canvas(self.screen, width=600, height=700)
#         canvas.pack()

#         # Charger l'image et l'afficher dans le Canvas
#         self.image_background = Image.open("assets/background_sport.png")
#         self.image_background = self.image_background.resize((600,  1000), Image.LANCZOS)  # Redimensionner l'image à la taille souhaitée
#         self.photo_background = ImageTk.PhotoImage(self.image_background)  # Store the image object as an instance variable
#         canvas.create_image(62,  50, anchor=tk.NW, image=self.photo_background)  # Use the instance variable here

#     def ajouter_titre(self):
#         #ajouter le titre
#         title = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#                     text = "SALON SPORT", font = ("sans serif", 25),
#                     background = "#000000", foreground = "#FFFAFA")
#         title.place(x=0, y=0, width = 600, height = 50)

#     def column_saloon(self):
#         # ajout colonne de gauche
#         column = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#                         text = "Salons disponibles", font = ("sans serif", 12),
#                         background = "#000000", foreground = "#FFFAFA")
#         column.place(x=0, y=50, width=160, height=650)
#         column.config(anchor=tk.NW)

#     def input_text(self):
#         # case de saisie de texte
#         text_input=Text(self.screen, width=40, height=5, relief=SUNKEN)
#         text_input.place(x=180, y=600)

#     def change_screen_sport(self):
#         self.screen.destroy()  # Fermer la première fenêtre
#         from InterfaceSport import ALL #import Interface_sport  # Importer le deuxième fichier

#     def change_screen_manga(self):
#         self.screen.destroy()
#         from InterfaceManga import ALL

#     def change_screen_movie(self):
#         self.screen.destroy()
#         from InterfaceMovie import ALL

#     def btn_send(self):
#         # bouton envoyer
#         btn_envoyer = Button(self.screen, text="Envoyer")
#         btn_envoyer.place(x=520, y=630)

#     def btn_sport(self):
#         # bouton salon sport
#         self.image_ballon = Image.open("assets/logo_sport.png")
#         self.image_ballon = self.image_ballon.resize((50, 50), Image.LANCZOS)
#         self.image_ballon = ImageTk.PhotoImage(self.image_ballon)
#         btn_canalsport = Button(self.screen, image=self.image_ballon, text="Sport", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_sport)
#         btn_canalsport.place(x=10, y=100)

#     def btn_movie(self):
#         #bouton salon cinéma
#         self.image_bobine = Image.open("assets/logo_dvd.png")
#         self.image_bobine = self.image_bobine.resize((50, 50), Image.LANCZOS)
#         self.image_bobine = ImageTk.PhotoImage(self.image_bobine)
#         btn_canalcinema = Button(self.screen, image=self.image_bobine, text="Cinéma", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_movie)
#         btn_canalcinema.place(x=10, y=180)

#     def btn_manga(self):
#         # bouton salon manga
#         self.image_boule = Image.open("assets/logo_manga.png")
#         self.image_boule = self.image_boule.resize((50, 50),  Image.LANCZOS)
#         self.image_boule = ImageTk.PhotoImage(self.image_boule)
#         btn_canalmanga = Button(self.screen, image=self.image_boule, text="Manga", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_manga)
#         btn_canalmanga.place(x=10, y=260)

#     def btn_disconnect(self):
#         # bouton déconnexion
#         btn_deconnexion = Button(self.screen, text="Déconnexion")
#         btn_deconnexion.place(x=30, y=10)


# sport_interface = InterfaceSport()
# sport_interface.background_image()
# sport_interface.ajouter_titre()
# sport_interface.column_saloon()
# sport_interface.input_text()
# sport_interface.btn_send()
# sport_interface.btn_sport()
# sport_interface.btn_movie()
# sport_interface.btn_manga()
# sport_interface.btn_disconnect()

# sport_interface.screen.mainloop() 