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