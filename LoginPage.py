from tkinter import *
from PIL import Image, ImageTk

# from tkinter.ttk import *

root = Tk()
root.geometry("1098x725")
root.configure(bg="#F0F0F0")  # Set background color

logo = Image.open('logofin.png')
logoImage = logo.resize((100, 40))
logoImage = ImageTk.PhotoImage(logoImage)
logoLabel = Label(image=logoImage, bg="#F0F0F0")  # Set background color for logo label
logoLabel.grid(row=0, column=0, padx=20, pady=20, sticky="w")  # Increase padding and align to the left

headingLabel = Label(text="Munshi: Your Accounting Assistant", font=("Helvetica", 24, "bold"),
                     bg="#F0F0F0")  # Increase font size and set background color
headingLabel.grid(row=0, column=1, padx=30, pady=20, sticky="w")  # Increase padding and align to the left

UsernameLabel = Label(text="Enter your Username", font=("Comic Sans MS", 12),
                      bg="#F0F0F0")  # Increase font size and set background color
UsernameLabel.grid(row=1, column=1, pady=10, padx=(10, 0), sticky="w")  # Add horizontal spacing and align to the right

usernameEntry = Entry(root, font=("Comic Sans MS", 12))  # Create an Entry widget for username
usernameEntry.grid(row=1, column=2, padx=(5, 0))  # Add horizontal spacing and align to the left

passWordLabel = Label(text="Enter your Password", font=("Comic Sans MS", 12),
                      bg="#F0F0F0")  # Increase font size and set background color
passWordLabel.grid(row=2, column=1, pady=10, padx=(10, 5), sticky="w")  # Add horizontal spacing and align to the right

passwordEntry = Entry(root, font=("Comic Sans MS", 12), show="*")  # Create an Entry widget for password
passwordEntry.grid(row=2, column=2, padx=(5, 10), sticky="w")  # Add horizontal spacing and align to the left

AlertLabel = Label(font=("Comic Sans MS", 13), bg="#F0F0F0")


def login():
    if usernameEntry.get() == "jatin" and passwordEntry.get() == "jatin":
        print("Logged in")
        root.withdraw()
        root.destroy()
        import landingPage

    else:
        AlertLabel.configure(text='Wrong Username or Passoword', fg="#FF0000")
        AlertLabel.grid(row=4, column=2, pady=10)


btn = Button(root, text='Login!', command=login)
btn.grid(row=3, column=2, sticky="w", ipadx=20)

root.mainloop()
