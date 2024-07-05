from customtkinter import *
import requests
from CTkMessagebox import CTkMessagebox
from tkinter import *

def signin_handler(email,password_entry):
    # global email_value
    email_value = email.get()
    password_value = password_entry.get()
    print(email_value)
   
    input_data = {
        "email": email_value,
        "password": password_value,
        "returnSecureToken": True
    }
    response = requests.post("https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyB71NwXNVhO5k3RDKrKfEPhcsGbaWEQxVg",json=input_data)

    response_data = response.json()

    if response.status_code==200:
        token = response_data["idToken"]
        CTkMessagebox(icon="check", message="Sign in successful")
        print("Sign in successfull")
        
        # bkndrandom_choices()
    else:
        error_message = response_data["error"]["message"]
        print(response_data["error"]["message"])
        CTkMessagebox(icon="cancel", message=error_message)



def create_window():
    global username_entry, password_entry, email
    new_window = CTkToplevel()
    new_window.geometry("500x500")
    new_window.title("Sign Up")
    new_window.grab_set() 
    new_window.lift()  
    
    label = CTkLabel(new_window, text="Sign Up", fg_color="transparent",font=("bold",20))
    label.place(relx=0.2,rely=0.1)
    label = CTkLabel(new_window, text="Please Sign up by entering your details below", fg_color="transparent",font=("bold",15))
    label.place(relx=0.2,rely=0.15)
    username_entry = CTkEntry(new_window,placeholder_text="Username",corner_radius=0,border_width=0)
    username_entry.pack()
    username_entry.place(relx=0.2,rely=0.25)
    email = CTkEntry(new_window,placeholder_text="Enter Email",corner_radius=0,border_width=0)
    email.pack()
    email.place(relx=0.2,rely=0.35)
    password_entry = CTkEntry(new_window,placeholder_text="Password",corner_radius=0,border_width=0,show="*")
    password_entry.pack()
    password_entry.place(relx=0.2,rely=0.45)
    password = CTkEntry(new_window,placeholder_text="Confirm Password",corner_radius=0,border_width=0,show="*")
    password.pack()
    password.place(relx=0.2,rely=0.55)


    # authenticate = CTkButton(new_window, text="Authenticate",fg_color="#C850C0" ,corner_radius=5,width=300,height=40,command=create_authenticate)
    # authenticate.place(relx=0.5,rely=0.8,anchor="center")
    button = CTkButton(new_window, text="Sign Up",fg_color="#C850C0" ,corner_radius=5,width=300,height=40,command=lambda: (signin_handler(email, password_entry),(store_user(username_entry))))
    button.place(relx=0.5,rely=0.7,anchor="center")
    new_window.wait_window()

create_window()