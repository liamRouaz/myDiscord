from tkinter import Tk
import tkinter

root = tkinter.Tk()
frames = [ tkinter.Frame(root, width=100, height=100, bg=color) for color in ('red', 'green', 'blue')]
index = 0
def show_next():
     global index
     frames[index].grid_forget()
     index = (index + 1) % len(frames)
     frames[index].grid(row=0)

show_next()