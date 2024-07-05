from customtkinter import *
from mainContent import maincontent
# from config2 import login_handler
from config import login_handler

def clear_window(root):
    # Destroy all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()

def LoginWindow(root):
    clear_window(root)
    label0 = CTkLabel(root, text="enter email on place of password and password in place of email", fg_color="transparent",font=("bold",20))
    label0.place(relx=0.0,rely=0.0)
    label = CTkLabel(root, text="Login In", fg_color="transparent",font=("bold",20))
    label.place(relx=0.2,rely=0.1)
   
    label1 = CTkLabel(root, text="Please enter your login information below", fg_color="transparent")
    label1.place(relx=0.2,rely=0.15)

    email = CTkEntry(root, placeholder_text="Enter Password",corner_radius=0,border_width=0)
    email.place(relx=0.2,rely=0.25)

    password = CTkEntry(root, placeholder_text="Enter Email",corner_radius=0,border_width=0,show="*")
    password.place(relx=0.2,rely=0.375)
    
    checkbox = CTkCheckBox(root, text="Remember Me", onvalue="on", offvalue="off")
    checkbox.place(relx=0.2,rely=0.5)
    
    button = CTkButton(root, text="Login",fg_color="#C850C0" ,corner_radius=5,width=300,height=40,command=lambda: (login_handler(email, password)))
    button.place(relx=0.5,rely=0.7,anchor="center")

def SignUpWindow(root):
    clear_window(root)
    
    label = CTkLabel(root, text="Sign Up", fg_color="transparent",font=("bold",20))
    label.place(relx=0.2,rely=0.1)

    label = CTkLabel(root, text="Please Sign up by entering your details below", fg_color="transparent", font=("bold",15))
    label.place(relx=0.2,rely=0.15)
    
    username_entry = CTkEntry(root,placeholder_text="Username",corner_radius=0,border_width=0)
    username_entry.pack()
    username_entry.place(relx=0.2,rely=0.25)
    
    email = CTkEntry(root,placeholder_text="Enter Email",corner_radius=0,border_width=0)
    email.pack()
    email.place(relx=0.2,rely=0.35)
    
    password_entry = CTkEntry(root,placeholder_text="Password",corner_radius=0,border_width=0,show="*")
    password_entry.pack()
    password_entry.place(relx=0.2,rely=0.45)
    
    password = CTkEntry(root,placeholder_text="Confirm Password",corner_radius=0,border_width=0,show="*")
    password.pack()
    password.place(relx=0.2,rely=0.55)

    button = CTkButton(root, text="Sign Up",fg_color="#C850C0" ,corner_radius=5,width=300,height=40,command=lambda: (login_handler(email, password)))
    button.place(relx=0.5,rely=0.7,anchor="center")