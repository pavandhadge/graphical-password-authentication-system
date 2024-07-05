from customtkinter import *
import tkinter as tk
from defaultWindow import defaultDisplay
import imgfetch
import multiprocessing

def function1():
    try:
        imgfetch.del_json()
        imgfetch.deleteimg()
    except Exception as e :
        print(f"exception at img delete = \n",e)
    try:
        imgfetch.image_fetch()
    except Exception as e :
        print(f"exception at img fetch = \n",e)
    print("Function 1 executed")

def function2():
    root = CTk()
    root.title("Graphical Authenticator")
    root.geometry("600x600")
    root.resizable(False,False)
    defaultDisplay(root)
    root.mainloop()
    print("Function 2 executed")

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=function1)
    process2 = multiprocessing.Process(target=function2)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both functions executed concurrently")
