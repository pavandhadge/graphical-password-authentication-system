from customtkinter import *
from tkinter import *

def clear_window(root):
    # Destroy all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()

def maincontent(root):
    clear_window(root)

    label = CTkLabel(root, text="Login In Successful! Enjoy Free Cookies! 🍪🍪🍪🍪", fg_color="transparent", font=("bold", 20))
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = CTkButton(root, text="Log Out", fg_color="#C850C0", font=("Arial", 15), corner_radius=5, width=100, height=40, command=lambda: root.quit())
    button.place(relx=0.5, rely=0.8, anchor="center")

def tryAgain(root):
    clear_window(root)

    label = CTkLabel(root, text="Login Failed! Please Try Again", fg_color="transparent", font=("bold", 20))
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = CTkButton(root, text="Exit", fg_color="#C850C0", font=("Arial", 15), corner_radius=5, width=100, height=40, command=lambda: root.quit())
    button.place(relx=0.5, rely=0.8, anchor="center")
