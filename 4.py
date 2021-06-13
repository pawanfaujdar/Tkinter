from tkinter import *
root = Tk()
from PIL import Image, ImageTk
image = Image.open("pic2.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()
root.mainloop()