import tkinter as tk
from tkinter import *
ck =Tk()
ck.geometry("1098x725")

nameLabel = Label(text="Name :")
address = Label(text="Address :")
state = Label(text="State :")
pinCode = Label(text="PIN code :")
telephoneno = Label(text="Telephone :")
email = Label(text="E-mail :")
currency = Label(text="Currency Symbol :")
financialyearfrom = Label(text="Financial year begins from :")
booksbeginingDate = Label(text="Books begining from :")
nameLabel.grid(row=1, column=1,ipady=20)
address.grid(row=2, column=1,ipady=20)
state.grid(row=3, column=1,ipady=20)
pinCode.grid(row=4, column=1,ipady=20)
telephoneno.grid(row=5, column=1,ipady=20)
email.grid(row=6, column=1,ipady=20)
currency.grid(row=7, column=1,ipady=20)
financialyearfrom.grid(row=8, column=1,ipady=20)
booksbeginingDate.grid(row=9, column=1,ipady=20)

nameEntry = Entry(ck,font=("Comic Sans MS", 12)).grid()
addressEntry = Entry(ck,font=("Comic Sans MS", 12)).grid()
stateEntry = Entry(ck,font=("Comic Sans MS", 12)).grid()
pinCodeEntry = Entry(ck,font=("Comic Sans MS", 12)).grid()
telephonenoEntry = Entry(ck,font=("Comic Sans MS", 12)).grid()
emailEntry = Entry(ck,font=("Comic Sans MS", 12)).grid()
currencyentry = Entry(ck,font=("Comic Sans MS", 12)).grid()
financialyearfromEntry =  Entry(ck,font=("Comic Sans MS", 12)).grid()
booksbeginingDateEntry =  Entry(ck,font=("Comic Sans MS", 12)).grid()



def submit_button():
    # pass

    # ck.withdraw()
    flagger = 1
    if flagger == 1:
        print("Quitting")
        ck.withdraw()
        ck.destroy()
    # import landingPage


submit = Button(ck,text="Save",command=submit_button).grid(row=10,column=1,ipady=20)
ck.mainloop()