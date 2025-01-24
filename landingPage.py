import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


def pop_window(dummy_event):
    data = optionBox.get(optionBox.curselection()[0])
    # top = tk.Toplevel(mk)

    print(data)
    if data == "Create Company":
        mk.destroy()
        import createPage


mk = Tk()
mk.geometry("1098x725")
mk.configure(bg="#F0F0F0")
logo = Image.open('logofin.png')
logoImage = logo.resize((100, 40))
logoImage = ImageTk.PhotoImage(logoImage)
logoLabel = Label(image=logoImage, bg="#F0F0F0")  # Set background color for logo label
logoLabel.grid(row=0, column=0, padx=20, pady=20, sticky="w")  # Increase padding and align to the left

headingLabel = Label(text="Munshi: Your Accounting Assistant", font=("Helvetica", 24, "bold"),
                     bg="#F0F0F0")  # Increase font size and set background color
headingLabel.grid(row=0, column=1, padx=30, pady=20, sticky="w")  # Increase padding and align to the left
listLabel = Label(text="List of companies", font=("Helvetica", 14, "bold"))
listLabel.grid(row=2, column=1)

optionBox = tk.Listbox(mk)
optionBox.insert(1, "Create Company")
optionBox.insert(2, "Select Company")
optionBox.insert(3, "quit")
optionBox.bind("<Double-Button-1>", pop_window)
optionBox.grid(row=3, column=3, ipadx=100, ipady=200)

mk.mainloop()
