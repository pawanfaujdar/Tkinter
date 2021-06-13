from tkinter import *
root = Tk()
root.geometry("655x333")

f1 = Frame(root, bg="grey", borderwidth="3", relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, bg="grey", borderwidth="3", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l1 = Label(f1, text="Project")
l1.pack(pady=98)

l2 = Label(f2, text="Welcome")
l2.pack()

root.mainloop()