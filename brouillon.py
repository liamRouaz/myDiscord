import tkinter as tk
import cv2
from PIL import Image, ImageTk

class VideoBackgroundApp:
    def __init__(self, window, video_source=0):
        self.window = window
        self.window.title("Video Background")
        
        # Créez un canevas pour afficher la vidéo
        self.canvas = tk.Canvas(window, width=800, height=600)
        self.canvas.pack()

        # Chargez la vidéo avec OpenCV
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Impossible d'ouvrir la vidéo")

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # Calculez les coordonnées pour centrer la vidéo dans le canevas
        self.x = (800 - self.width) // 2
        self.y = (600 - self.height) // 2

        # Affichez la première image de la vidéo sur le canevas
        self.photo = None
        self.update()

    def update(self):
        # Lisez une image à partir de la vidéo
        ret, frame = self.vid.read()
        if ret:
            # Convertissez l'image en format compatible avec tkinter
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            # Affichez l'image centrée dans le canevas
            self.canvas.create_image(self.x, self.y, anchor=tk.NW, image=self.photo)
        self.window.after(20, self.update)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Créez une fenêtre tkinter
root = tk.Tk()
app = VideoBackgroundApp(root, 'assets/etoiles.mp4')
root.mainloop()