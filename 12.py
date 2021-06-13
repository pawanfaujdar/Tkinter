from tkinter import *
root = Tk()
root.geometry("644x344")

def getvals():
    print("Submitting Form")
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentModevalue.get(), foodservicevalue.get() }")

    with open("record.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentModevalue.get(), foodservicevalue.get()}\n")

Label(root, text="WELCOME TO PAWAN'S TRAVELS", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#text
name = Label(root, text="name")
phone = Label(root, text="Phone")
gender = Label(root, text="gender")
emergency = Label(root, text="emergency Contact")
paymentMode = Label(root, text="Payment Mode")

#pack
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentMode.grid(row=5, column=2)

#variable
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentModevalue = StringVar()
foodservicevalue =IntVar()

#entries
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentModeentry = Entry(root, textvariable=paymentModevalue)

#pack
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentModeentry.grid(row=5, column=3)

#checkbox
foodservice = Checkbutton(text="want to prebook your meals", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

#Button
Button(text="Submit to Pawan Travels", command=getvals).grid(row=7, column=3)

root.mainloop()