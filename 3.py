# Displaying Images using Label:
from tkinter import *
root = Tk()
root.geometry("2000x2000")
photo = PhotoImage(file="pic.png")
label = Label(image=photo)
label.pack()
root.mainloop()