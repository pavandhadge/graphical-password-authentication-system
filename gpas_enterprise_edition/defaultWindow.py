from customtkinter import *
from registerWindow import LoginWindow
from registerWindow import SignUpWindow
import tkinter as tk
# import imagefetch

def clear_window(root):
    # Destroy all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()

def DisplayLoginWindow(root):
    LoginWindow(root)

#default display function
def defaultDisplay(root):


    

    # Header with title "Quizzle"
    header_label = CTkLabel(root, text="Graphical Authenticator", font=("Arial", 20))
    header_label.pack(side=tk.TOP, pady=20)

    # Login and Sign In button
    login_button = CTkButton(root, text="Login", fg_color="#C850C0", font=("Arial", 15), corner_radius=5, width=300, height=40, command = lambda: LoginWindow(root))
    login_button.pack(side=tk.TOP, padx=10, pady=10)

    signin_button = CTkButton(root, text="Sign Up", fg_color="#C850C0", font=("Arial", 15), corner_radius=5, width=300, height=40, command = lambda: SignUpWindow(root))
    signin_button.pack(side=tk.TOP, padx=10, pady=10)

    # Button to exit the window
    button = CTkButton(root, text="Exit", fg_color="#C850C0", font=("Arial", 15), corner_radius=5, width=100, height=40, command=lambda: root.quit())  
    button.place(relx=0.5, rely=0.8, anchor="center")