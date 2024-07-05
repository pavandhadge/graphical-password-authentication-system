from customtkinter import *
import requests
from CTkMessagebox import CTkMessagebox
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import random
# import main
def maincontent():
    app_window = CTkToplevel()
    app_window.title("LogedIn")
    app_window.grab_set()
    app_window.lift()  
    app_window.geometry('600x600')
    app_label = CTkLabel(app_window, text="YOU HAVE SUCCESSFULLY LOGED IN", fg_color="transparent",font=("bold",24))
    app_label.place(relx=0.2,rely=0.2)
    logout = CTkButton(app_window, text="LOGOUT", fg_color="#C850C0", corner_radius=5, width=200, height=40,command=lambda: app_window.destroy())
    logout.place(relx=0.8, rely=0.6, anchor="center")