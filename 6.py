from tkinter import *
root = Tk()
root.geometry("444x233")
root.title("GUI of Pawan")
label = Label(text="Hello, I am Pawan", bg="red", fg="white", font="comicsansms 19 bold",
              borderwidth=3, relief=SUNKEN, padx=113, pady=94)
label.pack(side=BOTTOM, anchor="nw", fill="x")    #or fill=X
root.mainloop()