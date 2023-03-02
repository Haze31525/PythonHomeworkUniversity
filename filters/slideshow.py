from PIL import Image, ImageTk
import tkinter as tk
import os
import time
import random


class Slideshow:
    def __init__(self, images, duration):
        self.images = images
        self.duration = duration
        self.current_image_index = 0

        self.root = tk.Tk()
        self.root.title("Slideshow")
        self.root.geometry("500x500")

        self.label = tk.Label(self.root)
        self.label.pack()

        self.start_slideshow()

        self.root.mainloop()

    def start_slideshow(self):
        image_path = self.images[self.current_image_index]
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo

        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.root.after(self.duration * 1000, self.start_slideshow)


def run_slideshow(image_paths, duration):
    slideshow = Slideshow(image_paths, duration)



