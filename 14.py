from tkinter import *
root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

def pawan(event):
    print(f"you have clicked on the button at {event.x}, {event.y}")

widget = Button(root, text="Click me please")
widget.pack()

widget.bind("<Button-1>", pawan)
widget.bind("<Double-1>", quit)

root.mainloop()