from tkinter import Label, SUNKEN
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

class InterfaceSaloon:
    def __init__(self):
        self.screen2 = Tk()
        self.screen2.geometry("600x700")
        self.screen2.title("MyDiscord")
        self.screen2.resizable(False, False)
        self.screen2.configure(background="#343541")
        

 
    # def title(self):
    #     title = Label(self.screen, borderwidth=8, relief=SUNKEN,
    #                   text="BIENVENUE {username} \r Veuillez choisir un salon", font=("sans serif", 25),
    #                   background="#000000", foreground="#FFFAFA")
    #     title.place(x=0, y=50, width=600, height=100)
    def background_image(self):
        # Créer un Canvas pour afficher l'image
        canvas = tk.Canvas(self.screen2, width=600, height=700, bg="#343541", borderwidth=0, highlightthickness=0)
        canvas.pack()

        # Charger l'image et l'afficher dans le Canvas
        self.image_background = tk.PhotoImage(file="assets/cieletoiles4.png")
        canvas.create_image(0, 0, anchor=tk.NW, image=self.image_background) 

        self.description_label = Text(self.screen2, borderwidth=8, relief=SUNKEN, background="#343541", foreground="#FFFAFA", wrap=WORD, font=('Agency FB', 20))
        self.description_label.place(x=40, y=400, width=500, height=250)

        self.description_manga = "Rejoignez une communaute passionnee ou les fans echangent sur leurs series preferees et partagent des recommandations de lecture. \nVenez vivre des discussions animees et une ambiance conviviale ou la passion des mangas est a l honneur."
        self.description_cinema = "Bienvenue dans notre salon dedie au cinema ! \nPlongez dans un univers ou les passionnes de films se reunissent pour discuter de tout ce qui touche au septieme art. \nRejoignez nous pour des discussions animees, des recommandations de films et des analyses approfondies."
        self.description_sport = "Rejoignez une communaute passionnee ou les fans echangent sur leurs series preferees, partagent des recommandations de lecture, discutent des derniers chapitres ou episodes, et partagent leur fan art et leurs theories. Que vous soyez novice ou veteran, venez vivre des discussions animees et une ambiance conviviale ou la creativite et la passion des mangas sont a l honneur."
   
    def change_screen_sport(self):
        self.screen2.destroy()  # Fermer la première fenêtre
        from InterfaceSport import ALL  # Importer le deuxième fichier

    def change_screen_manga(self):
        self.screen2.destroy()
        from InterfaceManga import ALL

    def change_screen_movie(self):
        self.screen2.destroy()
        from InterfaceMovie import ALL

    def on_enter_manga(self, event=None):
        # Mettre à jour la description lorsque la souris survole le bouton
        self.description_label.delete(1.0, END)  # Efface le contenu précédent
        self.description_label.insert(END, self.description_manga)

    def on_leave_manga(self, event=None):
        # Effacer la description lorsque la souris quitte le bouton
        self.description_label.delete(1.0, END)

    def on_enter_sport(self, event=None):
        # Mettre à jour la description lorsque la souris survole le bouton
        self.description_label.delete(1.0, END)  # Efface le contenu précédent
        self.description_label.insert(END, self.description_sport)

    def on_leave_sport(self, event=None):
        # Effacer la description lorsque la souris quitte le bouton
        self.description_label.delete(1.0, END)

    def on_enter_cinema(self, event=None):
        # Mettre à jour la description lorsque la souris survole le bouton
        self.description_label.delete(1.0, END)  # Efface le contenu précédent
        self.description_label.insert(END, self.description_cinema)

    def on_leave_cinema(self, event=None):
        # Effacer la description lorsque la souris quitte le bouton
        self.description_label.delete(1.0, END)

    def btn_sport(self):
        # salon sport
        self.image_ballon = Image.open("assets/logo_sport.png")
        self.image_ballon = self.image_ballon.resize((50, 50), Image.LANCZOS)
        self.image_ballon = ImageTk.PhotoImage(self.image_ballon)
        self.btn_canalsport = Button(self.screen2, image=self.image_ballon, text="Sport", compound="left",
                                     font=('ROGFonts-Regular', 11), foreground="#FFFAFA", width=130, anchor="w",
                                     bg="black", command=self.change_screen_sport)
        self.btn_canalsport.place(x=30, y=260)

        # Lier les événements de survol et de sortie de la souris aux méthodes correspondantes
        self.btn_canalsport.bind("<Enter>", self.on_enter_sport)
        self.btn_canalsport.bind("<Leave>", self.on_leave_sport)

    def btn_cinema(self):
        # bouton salon cinéma
        self.image_bobine = Image.open("assets/logo_dvd.png")
        self.image_bobine = self.image_bobine.resize((50, 50), Image.LANCZOS)
        self.image_bobine = ImageTk.PhotoImage(self.image_bobine)
        self.btn_canalcinema = Button(self.screen2, image=self.image_bobine, text="Cinema", compound="left",
                                      font=('ROGFonts-Regular', 11), foreground="#FFFAFA", width=130, anchor="w",
                                      bg="black", command=self.change_screen_movie)
        self.btn_canalcinema.place(x=230, y=260)
        
        # Lier les événements de survol et de sortie de la souris aux méthodes correspondantes
        self.btn_canalcinema.bind("<Enter>", self.on_enter_cinema)
        self.btn_canalcinema.bind("<Leave>", self.on_leave_cinema)

    def btn_manga(self):
        # bouton salon manga
        self.image_boule = Image.open("assets/logo_manga.png")
        self.image_boule = self.image_boule.resize((50, 50), Image.LANCZOS)
        self.image_boule = ImageTk.PhotoImage(self.image_boule)
        self.btn_canalmanga = Button(self.screen2, image=self.image_boule, text="Manga", compound="left",
                                     font=('ROGFonts-Regular', 11), foreground="#FFFAFA", width=130, anchor="w",
                                     bg="black", command=self.change_screen_manga)
        self.btn_canalmanga.place(x=430, y=260)

        # Lier les événements de survol et de sortie de la souris aux méthodes correspondantes
        self.btn_canalmanga.bind("<Enter>", self.on_enter_manga)
        self.btn_canalmanga.bind("<Leave>", self.on_leave_manga)

    def btn_disconnect(self):
        # bouton déconnexion
        self.btn_deconnexion = Button(self.screen2, text="Déconnexion")
        self.btn_deconnexion.place(x=10, y=10)

saloon_interface = InterfaceSaloon()
saloon_interface.background_image()
saloon_interface.btn_sport()
saloon_interface.btn_cinema()
saloon_interface.btn_manga()
saloon_interface.btn_disconnect()

#saloon_interface.screen2.mainloop()



        # self.description_manga = "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées et partagent des recommandations de lecture. \nVenez vivre des discussions animées et une ambiance conviviale où la passion des mangas est à l'honneur."
        # self.description_cinema = "Bienvenue dans notre salon dédié au cinéma ! \nPlongez dans un univers où les passionnés de films se réunissent pour discuter de tout ce qui touche au septième art. \nRejoignez-nous pour des discussions animées, des recommandations de films et des analyses approfondies."
        # self.description_sport = "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées, partagent des recommandations de lecture, discutent des derniers chapitres ou épisodes, et partagent leur fan art et leurs théories. Que vous soyez novice ou vétéran, venez vivre des discussions animées et une ambiance conviviale où la créativité et la passion des mangas sont à l'honneur."
# from tkinter import Label, SUNKEN
# import tkinter
# from tkinter import *
# from PIL import Image, ImageTk
# import tkinter as tk


# class InterfaceSaloon():
#     # fenetre
#     def __init__(self):
#         self.screen = tkinter.Tk()
#         self.screen.geometry("600x700")
#         self.screen.title("MyDiscord")
#         self.screen.resizable(False, False)
#         self.screen.configure(background="#343541")
#         self.description_label = Label(self.screen, borderwidth = 8, relief = SUNKEN, background = "#343541", foreground = "#FFFAFA")
#         self.description_label.place(x=10, y=320, width=420, height=350)
#         self.description_manga = "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées et partagent des recommandations de lecture. \nVenez vivre des discussions animées et une ambiance conviviale où la passion des mangas est à l'honneur."

#     def title(self):
#         title = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#                     text = "BIENVENUE {username} \r Veuillez choisir un salon", font = ("sans serif", 25),
#                     background = "#000000", foreground = "#FFFAFA")
#         title.place(x=0, y=50, width = 600, height = 100)

#     def change_screen_sport(self):
#         self.screen.destroy()  # Fermer la première fenêtre
#         from InterfaceSport import ALL #import Interface_sport  # Importer le deuxième fichier

#     def change_screen_manga(self):
#         self.screen.destroy()
#         from InterfaceManga import ALL

#     def change_screen_movie(self):
#         self.screen.destroy()
#         from InterfaceMovie import ALL
        
#     def label_description(self):
#         # Création du label pour la description
#         self.description_label = Label(self.screen, borderwidth=8, relief=SUNKEN, background="#343541", foreground="#FFFAFA")
#         self.description_label.place(x=10, y=320, width=420, height=350)

#     def on_enter_manga(self, event=None):
#         # Mettre à jour la description lorsque la souris survole le bouton
#         self.description_label.delete(1.0, END)  # Efface le contenu précédent
#         self.description_label.insert(END, self.description_manga)

#     def on_leave_manga(self, event=None):
#         # Effacer la description lorsque la souris quitte le bouton
#         self.description_label.delete(1.0, END)

#     # def on_enter_manga(self, event=None):
#     #     # Mettre à jour la description lorsque la souris survole le bouton
#     #     self.description_label.config(text=self.description_manga.get(1.0, "end"))

#     # def on_leave_manga(self, event=None):
#     #     # Effacer la description lorsque la souris quitte le bouton
#     #     self.description_label.config(text="")

#     #     # évènement de passage de souris sur les boutons 
#     # def on_enter_manga(self):
#     #     self.description_label.config(text=self.description_manga.get(1.0, "end"))

#     # def on_leave_manga(self):
#     #     self.description_label.config(text="")

#     # def on_enter_cinema(self):
#     #     self.description_label.config(text=self.description_cinema.get(1.0, "end"))

#     # def on_leave_cinema(self):
#     #     self.description_label.config(text="")

#     # def on_enter_sport(self):
#     #     self.description_label.config(text=self.description_sport.get(1.0, "end"))

#     # def on_leave_sport(self):
#     #     self.description_label.config(text="")

#     def label_description(self):
#                 # Création du widget Text pour afficher la description
#         self.description_label = Text(self.screen, borderwidth=8, relief=SUNKEN, background="#343541", foreground="#FFFAFA", wrap=WORD)
#         self.description_label.place(x=10, y=320, width=420, height=350)
#         # self.description_label = Label(self.screen, borderwidth = 8, relief = SUNKEN, background = "#343541", foreground = "#FFFAFA")
#         # self.description_label.place(x=0, y=320, width=600, height=350)

#     def btn_sport(self):
#         #  salon sport
#         self.image_ballon = Image.open("assets/logo_sport.png")
#         self.image_ballon = self.image_ballon.resize((50, 50), Image.LANCZOS)
#         self.image_ballon = ImageTk.PhotoImage(self.image_ballon)
#         self.btn_canalsport = Button(self.screen, image=self.image_ballon, text="Sport", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_sport)
#         self.btn_canalsport.place(x=30, y=260)

#         # description sous le bouton
#         # self.label_sport = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#         # #             text = "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées, partagent des recommandations de lecture, discutent des derniers chapitres ou épisodes, et partagent leur fan art et leurs théories. Que vous soyez novice ou vétéran, venez vivre des discussions animées et une ambiance conviviale où la créativité et la passion des mangas sont à l'honneur.", font = ("sans serif", 10),
#         #              background = "#343541", foreground = "#FFFAFA")
#         ## self.label_sport.place(x=10, y=320, width = 180, height = 350)
#         # self.description_sport = Text(self.screen, background = "#343541", foreground = "#FFFAFA", font = ("sans serif", 13))
#         # self.description_sport.insert(1.0, "Bienvenue dans notre salon de chat dédié aux sports ! \nQue vous soyez fan de football, de basketball, ou de tout autre sport, venez discuter des derniers matchs, partager des analyses, échanger des pronostics, ou tout simplement célébrer les performances des athlètes.")
#         # self.description_sport.place(x=10, y=320, width = 140, height = 350)
        

#     def btn_movie(self):
#         #bouton salon cinéma
#         self.image_bobine = Image.open("assets/logo_dvd.png")
#         self.image_bobine = self.image_bobine.resize((50, 50), Image.LANCZOS)
#         self.image_bobine = ImageTk.PhotoImage(self.image_bobine)
#         self.btn_canalcinema = Button(self.screen, image=self.image_bobine, text="Cinéma", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_movie)
#         self.btn_canalcinema.place(x=230, y=260)

#         # description sous le bouton
#         # self.label_cinema = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#         #             background = "#343541", foreground = "#FFFAFA")
#         ## self.label_cinema.place(x=210, y=320, width = 180, height = 350)
#         # self.description_cinema = Text(self.screen, background = "#343541", foreground = "#FFFAFA", font = ("sans serif", 13))
#         # self.description_cinema.insert(1.0, "Bienvenue dans notre salon dédié au cinéma ! \nPlongez dans un univers où les passionnés de films se réunissent pour discuter de tout ce qui touche au septième art. \nRejoignez-nous pour des discussions animées, des recommandations de films et des analyses approfondies.")
#         # self.description_cinema.place(x=210, y=320, width = 140, height = 350)
    
#     def btn_manga(self):
#     # bouton salon manga
#         self.image_boule = Image.open("assets/logo_manga.png")
#         self.image_boule = self.image_boule.resize((50, 50), Image.LANCZOS)
#         self.image_boule = ImageTk.PhotoImage(self.image_boule)
        
#         self.btn_canalmanga = Button(self.screen, image=self.image_boule, text="Manga", compound=tk.LEFT, font=("sans serif", 15), foreground="#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_manga)
#         self.btn_canalmanga.place(x=430, y=260)

#         # Lier les événements de survol et de sortie de la souris aux méthodes correspondantes
#         self.btn_canalmanga.bind("<Enter>", self.on_enter_manga)
#         self.btn_canalmanga.bind("<Leave>", self.on_leave_manga)

#         # Créer et placer le label de description après avoir lié les événements de survol et de sortie de la souris
#         self.label_description()

#     # def btn_manga(self):
#     #     # bouton salon manga
#     #     self.image_boule = Image.open("assets/logo_manga.png")
#     #     self.image_boule = self.image_boule.resize((50, 50),  Image.LANCZOS)
#     #     self.image_boule = ImageTk.PhotoImage(self.image_boule)
#     #     self.btn_canalmanga = Button(self.screen, image=self.image_boule, text="Manga", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_manga)
#     #     self.btn_canalmanga.place(x=430, y=260)

#         # description sous le bouton
#         # self.label_manga = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#         #             background = "#343541", foreground = "#FFFAFA")
#         ## self.label_manga.place(x=410, y=320, width = 180, height = 350)
#         self.description_manga = Text(self.description_label, background = "#343541", foreground = "#FFFAFA", font = ("sans serif", 23))
#         #self.description_manga.insert(1.0, "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées et partagent des recommandations de lecture. \nVenez vivre des discussions animées et une ambiance conviviale où la passion des mangas est à l'honneur.")
#         self.description_manga.place(x=10, y=20, width = 140, height = 350)

#         self.btn_canalmanga.bind("<Enter>", self.on_enter_manga)
#         self.btn_canalmanga.bind("<Leave>", self.on_leave_manga)

#     def btn_disconnect(self):
#         # bouton déconnexion
#         self.btn_deconnexion = Button(self.screen, text="Déconnexion")
#         self.btn_deconnexion.place(x=10, y=10)


# saloon_interface = InterfaceSaloon()
# saloon_interface.btn_sport()
# saloon_interface.btn_movie()
# saloon_interface.btn_manga()
# saloon_interface.btn_disconnect()
# saloon_interface.title()
# #saloon_interface.label_description()
# saloon_interface.screen.mainloop()

# import tkinter
# from tkinter import *
# from PIL import Image, ImageTk
# import tkinter as tk


# class SaloonInterface():
#     # fenetre
#     screen = tkinter.Tk()
#     screen.geometry("600x700")
#     screen.title("MyDiscord")
#     screen.resizable(False, False)
#     screen.configure(background="#343541")

#     def title(self):
#         title = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#                     text = "BIENVENUE {username} \r Veuillez choisir un salon", font = ("sans serif", 25),
#                     background = "#000000", foreground = "#FFFAFA")
#         title.place(x=0, y=50, width = 600, height = 100)

#     def change_screen_sport(self):
#         self.screen.destroy()  # Fermer la première fenêtre
#         from src.SportInterface import ALL #import Interface_sport  # Importer le deuxième fichier

#     def change_screen_manga(self):
#         self.screen.destroy()
#         from src.MangaInterface import ALL

#     def change_screen_movie(self):
#         self.screen.destroy()
#         from src.MovieInterface import ALL

#     def btn_sport(self):
#         # bouton salon sport
#         self.image_ballon = Image.open("assets/logo_sport.png")
#         self.image_ballon = self.image_ballon.resize((50, 50), Image.LANCZOS)
#         self.image_ballon = ImageTk.PhotoImage(self.image_ballon)
#         self.btn_canalsport = Button(self.screen, image=self.image_ballon, text="Sport", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_sport)
#         self.btn_canalsport.place(x=30, y=260)

#         # description sous le bouton
#         self.label_sport = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#         #             text = "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées, partagent des recommandations de lecture, discutent des derniers chapitres ou épisodes, et partagent leur fan art et leurs théories. Que vous soyez novice ou vétéran, venez vivre des discussions animées et une ambiance conviviale où la créativité et la passion des mangas sont à l'honneur.", font = ("sans serif", 10),
#                      background = "#343541", foreground = "#FFFAFA")
#         self.label_sport.place(x=10, y=320, width = 180, height = 350)
#         self.description_sport = Text(self.label_sport, background = "#343541", foreground = "#FFFAFA", font = ("sans serif", 13))
#         self.description_sport.insert(1.0, "Bienvenue dans notre salon de chat dédié aux sports ! \nQue vous soyez fan de football, de basketball, ou de tout autre sport, venez discuter des derniers matchs, partager des analyses, échanger des pronostics, ou tout simplement célébrer les performances des athlètes.")
#         #self.description_sport.tag_configure()
#         self.description_sport.place(x=10, y=320, width = 140, height = 350)
#         self.description_sport.pack()    

#     def btn_movie(self):
#         #bouton salon cinéma
#         self.image_bobine = Image.open("assets/logo_dvd.png")
#         self.image_bobine = self.image_bobine.resize((50, 50), Image.LANCZOS)
#         self.image_bobine = ImageTk.PhotoImage(self.image_bobine)
#         self.btn_canalcinema = Button(self.screen, image=self.image_bobine, text="Cinéma", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_movie)
#         self.btn_canalcinema.place(x=230, y=260)

#         # description sous le bouton
#         self.label_cinema = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#                     #text = "", font = ("sans serif", 10),
#                     background = "#343541", foreground = "#FFFAFA")
#         self.label_cinema.place(x=210, y=320, width = 180, height = 350)
#         self.description_cinema = Text(self.label_cinema, background = "#343541", foreground = "#FFFAFA", font = ("sans serif", 13))
#         self.description_cinema.insert(1.0, "Bienvenue dans notre salon dédié au cinéma ! \nPlongez dans un univers où les passionnés de films se réunissent pour discuter de tout ce qui touche au septième art. \nRejoignez-nous pour des discussions animées, des recommandations de films et des analyses approfondies.")
#         #self.description_sport.tag_configure()
#         self.description_cinema.place(x=210, y=320, width = 140, height = 350)
#         self.description_cinema.pack()

#     def btn_manga(self):
#         # bouton salon manga
#         self.image_boule = Image.open("assets/logo_manga.png")
#         self.image_boule = self.image_boule.resize((50, 50),  Image.LANCZOS)
#         self.image_boule = ImageTk.PhotoImage(self.image_boule)
#         self.btn_canalmanga = Button(self.screen, image=self.image_boule, text="Manga", compound=tk.LEFT, font = ("sans serif", 15), foreground = "#FFFAFA", width=130, anchor=tk.W, bg="black", command=self.change_screen_manga)
#         self.btn_canalmanga.place(x=430, y=260)

#         # description sous le bouton
#         self.label_manga = Label(self.screen, borderwidth = 8, relief = SUNKEN,
#                     #text = "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées et partagent des recommandations de lecture. Venez vivre des discussions animées et une ambiance conviviale où la passion des mangas est à l'honneur.", font = ("sans serif", 10),
#                     background = "#343541", foreground = "#FFFAFA")
#         self.label_manga.place(x=410, y=320, width = 180, height = 350)
#         self.description_cinema = Text(self.label_manga, background = "#343541", foreground = "#FFFAFA", font = ("sans serif", 13))
#         self.description_cinema.insert(1.0, "Rejoignez une communauté passionnée où les fans échangent sur leurs séries préférées et partagent des recommandations de lecture. \nVenez vivre des discussions animées et une ambiance conviviale où la passion des mangas est à l'honneur.")
#         #self.description_sport.tag_configure()
#         self.description_cinema.place(x=410, y=320, width = 140, height = 350)
#         self.description_cinema.pack()

#     def btn_disconnect(self):
#         # bouton déconnexion
#         self.btn_deconnexion = Button(self.screen, text="Déconnexion")
#         self.btn_deconnexion.place(x=10, y=10)


# saloon_interface = SaloonInterface()
# saloon_interface.btn_sport()
# saloon_interface.btn_movie()
# saloon_interface.btn_manga()
# saloon_interface.btn_disconnect()
# saloon_interface.title()
# saloon_interface.screen.mainloop()



