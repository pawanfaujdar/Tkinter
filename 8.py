from tkinter import *
root = Tk()
root.geometry("655x133")

f1 = Frame(root, bg="red", borderwidth=3)
f1.pack(side=LEFT)

label = Label(f1, text="Project")
label.pack()

root.mainloop()