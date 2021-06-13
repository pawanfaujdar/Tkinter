from tkinter import *
root = Tk()
root.geometry("733x566")
root.title("PyCharm")

def myfun():
    print("Bye")

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="Save", command=myfun)
m1.add_separator()
m1.add_command(label="Save as", command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

root.mainloop()