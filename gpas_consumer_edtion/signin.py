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