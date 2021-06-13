from tkinter import *
root = Tk()
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(0, 0, 800, 200)
can_widget.create_rectangle(50, 50, 400, 400, fill="blue")
can_widget.create_text(400, 200, text="PAWAN")
can_widget.create_oval(344, 233, 244, 355, fill="red")

root.mainloop()