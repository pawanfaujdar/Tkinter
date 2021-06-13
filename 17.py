from tkinter import *
root = Tk()

root.geometry("733x566")
root.title("Pycharm")

def myfun():
    print("Bye")

mymenu = Menu(root)
mymenu.add_command(label="File", command=myfun)
mymenu.add_command(label="Exit", command=quit)

root.configure(menu=mymenu)

root.mainloop()