from customtkinter import *
import tkinter as tk
from tkinter import *
import requests
from CTkMessagebox import CTkMessagebox
import random
import numpy as np
from mainContent import maincontent
from PIL import Image, ImageTk
import emailhandler
number_counter = 0
i=0
a = []
global image
image = ["./temp/image1.jpg","./temp/image2.jpg","./temp/image3.jpg","./temp/image4.jpg","./temp/image5.jpg"]

def store_patterns(rows,columns):
    print(f"Pattern {rows},{columns}")
    global a
  
    a.append([rows,columns])
    global b
    b = np.array(a)
    print(b)

def login_handler(email,password_entry):
    # check if email and password_entry widgets still exist
    if email.winfo_exists() and password_entry.winfo_exists():
        email_value = email.get()
        password_value = password_entry.get()
        print(email_value)
   
        input_data = {
            "email": email_value,
            "password": password_value,
            "returnSecureToken": True
        }
        response = requests.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyB71NwXNVhO5k3RDKrKfEPhcsGbaWEQxVg",json=input_data)

        response_data = response.json()

        if response.status_code==200:
            token = response_data["idToken"]
            # CTkMessagebox(icon="check", message="Login successful")
            # print("Login successfull")
            bkndrandom_choices()
            # emailhandler.email_trigger(random_selected,email_value)
            create_authenticate()
            selection_matching(a,random_selected)
        else:
            error_message = response_data["error"]["message"]
            print(response_data["error"]["message"])
            CTkMessagebox(icon="cancel", message=error_message)
    else:
        # handle the case when the widgets do not exist
        print("The widgets have been destroyed or do not exist")
        CTkMessagebox(icon="warning", message="The widgets have been destroyed or do not exist")

def bkndrandom_choices():
    avalablechoices_arr = [[0,0],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    length = random.randint(1,5)
    print(length)

    random_selections = (random.sample(avalablechoices_arr, length))

    for i in range (len(random_selections),5):
        random_selections.append([0,0])
    print(f"Randomly selected items: {random_selections}")
     
    global random_selected
    random_selected = (random_selections)
    
    print(len(random_selected))

def selection_matching(b, random_selected):
    match_no = 0
    print(random_selected)
    print(len(b))

    if(len(random_selected) == len(b)):
        for i in range(0, len(random_selected)):
            if(b[i] == random_selected[i]):
                match_no = match_no+1
            else:
                print("not similar seq")
                CTkMessagebox(title="LOGIN FAILED", message="selected choices did not match with authentication otp")
                return ValueError
    else:
        print("the array does not match this is not the right combination")
        CTkMessagebox(title="LOGIN FAILED", message="ERROR WHILE AUTHONTICATING")
        return ValueError
    if(match_no ==len(random_selected)):
        maincontent()

def create_authenticate():
    global i
    global image
    
    new_window = CTkToplevel()
    new_window.title("Authenticate")
    new_window.grab_set()
    new_window.lift()  
    new_window.geometry('700x600')

   
      
    def on_button_click(row, col):
        global i 
        # i=0
        # global image
        # image = ["image.jpg","image1.jpg","image2.jpg","image3.jpg","image4.jpg"]

        global image
        image = ["./temp/image1.jpg","./temp/image2.jpg","./temp/image3.jpg","./temp/image4.jpg","./temp/image5.jpg"]
        print(f"Clicked on grid: {row}, {col}")
        store_patterns(row,col)
        new_window.destroy()       
        if i < len(image)-1 :
            i = i+1
            create_authenticate()  
        else:
            print("All images processed")
            # store_user(b)
    
    image_path = image[i]
    image = Image.open(image_path)
    width, height = image.size

    fixed_window_width = 600
    fixed_window_height = 600

    scale_factor = min(fixed_window_width / width, fixed_window_height / height)
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    image = image.resize((new_width, new_height))
    # photo = ImageTk.PhotoImage(image)

    frame = Frame(new_window, width=fixed_window_width, height=fixed_window_height)
    frame.pack_propagate(False)  

    buttons = [[None for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            x1 = col * (new_width // 3)
            y1 = row * (new_height // 3)
            x2 = x1 + (new_width // 3)
            y2 = y1 + (new_height // 3)
        
            button_image = image.crop((x1, y1, x2, y2))
            button_photo = ImageTk.PhotoImage(button_image)
        
            button = Button(frame, image=button_photo, command=lambda row=row, col=col: on_button_click(row+1, col+1))
            button.image = button_photo
            button.grid(row=row, column=col, sticky="nsew")
            buttons[row][col] = button
            
    skip = CTkButton(new_window, text="Skip",fg_color="#C850C0" ,corner_radius=5,width=200,height=40,command=lambda row=0, col=0: on_button_click(row, col))
    skip.place(relx=0.6,rely=0.9)
    frame.pack()
    
    new_window.wait_window()
    # new_window.destroy()

def login_success_handler():
     new_window = CTkToplevel()
     new_window.title("LogedIn")
     new_window.grab_set()
     new_window.lift()  
     new_window.geometry('500x500')
     
     label = CTkLabel(new_window, text="Login In Successful! Enjoy Free Cookies! 🍪🍪🍪🍪", fg_color="transparent",font=("bold",20))
     label.place(relx=0.1,rely=0.5)

     new_window.wait_window()