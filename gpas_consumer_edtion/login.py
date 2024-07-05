from customtkinter import *
import tkinter as tk
from tkinter import *
import requests
from CTkMessagebox import CTkMessagebox
import random
import numpy as np
from mainContent import maincontent, tryAgain
from PIL import Image, ImageTk
import requests
from io import BytesIO
import emailhandler

i = 0
a = []
# image = ["image.jpg","image1.jpg","image2.jpg","image3.jpg","image4.jpg"]
# # image = []
image_urls = []

def fetch_multiple_image_urls(num_images):
    for _ in range(num_images):
        random_image_url = get_random_image(400, 400)  # Assuming get_random_image function is defined elsewhere
        response = requests.get(random_image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        image_urls.append(random_image_url)
    return image_urls


def login_handler(root, email, password_entry):
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
        response = requests.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyB71NwXNVhO5k3RDKrKfEPhcsGbaWEQxVg", json=input_data)

        response_data = response.json()

        fetch_multiple_image_urls(5)

        if response.status_code == 200:
            # token = response_data["idToken"]
            bkndrandom_choices()
            # emailhandler.email_trigger(random_selected, email_value)
            graphicalAuthenticatoin(root, a, random_selected)
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
    # print(length)

    random_selections = (random.sample(avalablechoices_arr, length))

    for i in range (len(random_selections),5):
        random_selections.append([0,0])
    print(f"Randomly selected items: {random_selections}")

    global random_selected
    random_selected = (random_selections)
    print(len(random_selected))

def store_patterns(rows,columns):
    print(f"Pattern {rows},{columns}")
    global a

    a.append([rows,columns])
    b = np.array(a)
    print(b)

def get_random_image(width, height):
    url = f"https://picsum.photos/{width}/{height}"
    response = requests.get(url)
    return response.url

def graphicalAuthenticatoin(root, a, random_selected):

    def clear_window():
        # Destroy all widgets in the window
        for widget in root.winfo_children():
            widget.destroy()

    clear_window()

    fixed_window_width = 500
    fixed_window_height = 500

    frame = Frame(root, width=fixed_window_width, height=fixed_window_height)
    frame.pack_propagate(False)

    imageArrNum = 0

    def setImgGrid(imgPath):
        # random_image_url = get_random_image(400, 400)
        random_image_url = imgPath
        response = requests.get(random_image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))

        width, height = img.size

        scale_factor = min(fixed_window_width / width, fixed_window_height / height)
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)

        img = img.resize((new_width, new_height))

        buttons = [[None for _ in range(3)] for _ in range(3)]

        for rowArr in range(3):
            for colArr in range(3):
                x1 = colArr * (new_width // 3)
                y1 = rowArr * (new_height // 3)
                x2 = x1 + (new_width // 3)
                y2 = y1 + (new_height // 3)

                button_image = img.crop((x1, y1, x2, y2))
                button_photo = ImageTk.PhotoImage(button_image)

                button = Button(frame, image=button_photo, command = lambda row = rowArr, col = colArr: onBtnClick(row+1, col+1))
                button.image = button_photo
                button.grid(row=rowArr, column=colArr, sticky="nsew")
                buttons[rowArr][colArr] = button

    frame.pack()

    def clear_frame():
        for widgets in frame.winfo_children():
            widgets.destroy()

    def onBtnClick(row, col):
        nonlocal imageArrNum
        print(f"Clicked on grid: {row}, {col}")
        # store_patterns(row,col)
        print("Image Array Number", imageArrNum)
        print("Length", len(image_urls))
        store_patterns(row, col)
        clear_frame()
        imageArrNum += 1
        if imageArrNum < len(image_urls):
            setImgGrid(image_urls[imageArrNum])
        else:
            print("All images processed")
            selection_matching(root, a, random_selected)

    setImgGrid(image_urls[imageArrNum])

    skip = CTkButton(root, text="Skip", fg_color="#C850C0", corner_radius=5, width=200, height=40, command = lambda: onBtnClick(0, 0))
    skip.place(relx=0.6, rely=0.9)
    # root.wait_window()

def selection_matching(root, b, random_selected):
    match_no = 0

    print(b)
    print(random_selected)

    if (len(random_selected) == len(b)):
        for i in range(0, len(random_selected)):
            if (b[i] == random_selected[i]):
                match_no = match_no + 1
            else:
                print("not similar sequence")
                tryAgain(root)
    else:
        print("The array does not match this is not the right combination")
        tryAgain(root)

    if(match_no == len(random_selected)):
        print("MATCH")
        maincontent(root)