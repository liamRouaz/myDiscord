from tkinter import Label, SUNKEN
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk


class SaloonInterface():
    # fenetre
    screen = tkinter.Tk()
    screen.geometry("600x700")
    screen.title("MyDiscord")
    screen.resizable(False, False)
    screen.configure(background="#343541")

    def title(self):
        title = Label(self.screen, borderwidth = 8, relief = SUNKEN,
                    text = "BIENVENUE {username} \r Veuillez choisir un salon", font = ("sans serif", 25),
                    background = "#000000", foreground = "#FFFAFA")
        title.place(x=0, y=50, width = 600, height = 100)

    def change_screen_sport(self):
        self.screen.destroy()  # Fermer la première fenêtre
        from src.SportInterface import ALL #import Interface_sport  # Importer le deuxième fichier

    def change_screen_manga(self):
        self.screen.destroy()
        from src.MangaInterface import ALL

    def change_screen_movie(self):
        self.screen.destroy()
        from src.MovieInterface import ALL

    def btn_sport(self):
        # bouton salon sport
        self.image_ballon = Image.open("assets/logo_sport.png")
        self.image_ballon = self.image_ballon.resize((50, 50), Image.LANCZOS)
        self.image_ballon = ImageTk.PhotoImage(self.image_ballon)
        btn_canalsport = Button(self.screen, image=self.image_ballon, text="Sport", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_sport)
        btn_canalsport.place(x=30, y=260)

        # description sous le bouton
        self.label_sport = Label(self.screen, borderwidth = 8, relief = SUNKEN,
        #             text = "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées, partagent des recommandations de lecture, discutent des derniers chapitres ou épisodes, et partagent leur fan art et leurs théories. Que vous soyez novice ou vétéran, venez vivre des discussions animées et une ambiance conviviale où la créativité et la passion des mangas sont à l'honneur.", font = ("sans serif", 10),
                     background = "#343541", foreground = "#FFFAFA")
        self.label_sport.place(x=10, y=320, width = 180, height = 350)
        self.description_sport = Text(self.label_sport, background = "#343541", foreground = "#FFFAFA", font = ("sans serif", 13))
        self.description_sport.insert(1.0, "Bienvenue dans notre salon de chat dédié aux sports ! \nQue vous soyez fan de football, de basketball, ou de tout autre sport, venez discuter des derniers matchs, partager des analyses, échanger des pronostics, ou tout simplement célébrer les performances des athlètes.")
        #self.description_sport.tag_configure()
        self.description_sport.place(x=10, y=320, width = 140, height = 350)
        self.description_sport.pack()    

    def btn_movie(self):
        #bouton salon cinéma
        self.image_bobine = Image.open("assets/logo_dvd.png")
        self.image_bobine = self.image_bobine.resize((50, 50), Image.LANCZOS)
        self.image_bobine = ImageTk.PhotoImage(self.image_bobine)
        btn_canalcinema = Button(self.screen, image=self.image_bobine, text="Cinéma", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_movie)
        btn_canalcinema.place(x=230, y=260)

        # description sous le bouton
        self.label_cinema = Label(self.screen, borderwidth = 8, relief = SUNKEN,
                    #text = "", font = ("sans serif", 10),
                    background = "#343541", foreground = "#FFFAFA")
        self.label_cinema.place(x=210, y=320, width = 180, height = 350)
        self.description_cinema = Text(self.label_cinema, background = "#343541", foreground = "#FFFAFA", font = ("sans serif", 13))
        self.description_cinema.insert(1.0, "Bienvenue dans notre salon dédié au cinéma ! \nPlongez dans un univers où les passionnés de films se réunissent pour discuter de tout ce qui touche au septième art. \nRejoignez-nous pour des discussions animées, des recommandations de films et des analyses approfondies.")
        #self.description_sport.tag_configure()
        self.description_cinema.place(x=210, y=320, width = 140, height = 350)
        self.description_cinema.pack()

    def btn_manga(self):
        # bouton salon manga
        self.image_boule = Image.open("assets/logo_manga.png")
        self.image_boule = self.image_boule.resize((50, 50),  Image.LANCZOS)
        self.image_boule = ImageTk.PhotoImage(self.image_boule)
        btn_canalmanga = Button(self.screen, image=self.image_boule, text="Manga", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_manga)
        btn_canalmanga.place(x=430, y=260)

        # description sous le bouton
        self.label_manga = Label(self.screen, borderwidth = 8, relief = SUNKEN,
                    #text = "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées et partagent des recommandations de lecture. Venez vivre des discussions animées et une ambiance conviviale où la passion des mangas est à l'honneur.", font = ("sans serif", 10),
                    background = "#343541", foreground = "#FFFAFA")
        self.label_manga.place(x=410, y=320, width = 180, height = 350)
        self.description_cinema = Text(self.label_manga, background = "#343541", foreground = "#FFFAFA", font = ("sans serif", 13))
        self.description_cinema.insert(1.0, "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées et partagent des recommandations de lecture. \nVenez vivre des discussions animées et une ambiance conviviale où la passion des mangas est à l'honneur.")
        #self.description_sport.tag_configure()
        self.description_cinema.place(x=410, y=320, width = 140, height = 350)
        self.description_cinema.pack()

    def btn_disconnect(self):
        # bouton déconnexion
        btn_deconnexion = Button(self.screen, text="Déconnexion")
        btn_deconnexion.place(x=10, y=10)


saloon_interface = SaloonInterface()
saloon_interface.btn_sport()
saloon_interface.btn_movie()
saloon_interface.btn_manga()
saloon_interface.btn_disconnect()
saloon_interface.title()
saloon_interface.screen.mainloop()



