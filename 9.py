from tkinter import *
root = Tk()
root.geometry("655x333")

def hello():
    print("Hello Tkinter Button")

def name():
    print("My name is Pawan")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Print now", command=hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="Tell me now")
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red", text="Print now", command=name)
b3.pack(side=LEFT, padx=23)

root.mainloop()