from tkinter import *
from PIL import ImageTk, Image

root = Tk()
image = Image.open("button1.png")
image = image.resize((25, 25), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
button = Button(root, image=img)
button.pack()
root.mainloop()