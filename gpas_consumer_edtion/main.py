import customtkinter as tk
from customtkinter import *
from login import login_handler
from signin import signin_handler

class tkinterApp(tk.CTk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.CTk.__init__(self, *args, **kwargs)

        self.title("Graphical Authenticator")
        self.geometry("600x600")
        self.resizable(False,False)

        # creating a container
        container = tk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, LoginPage, SignUpPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        # Header with title "Graphical User Authentication System"
        header_label = CTkLabel(self, text="Graphical User Authentication System", font=("Arial", 20))
        header_label.pack(side=tk.TOP, pady=20)

        # Login and Sign In button
        login_button = CTkButton(self, text="Login", fg_color="#C850C0", font=("Arial", 15), corner_radius=5, width=300, height=40, command=lambda: controller.show_frame(LoginPage))
        login_button.pack(side=tk.TOP, padx=10, pady=10)


        signin_button = CTkButton(self, text="Sign Up", fg_color="#C850C0", font=("Arial", 15), corner_radius=5, width=300, height=40, command=lambda: controller.show_frame(SignUpPage))
        signin_button.pack(side=tk.TOP, padx=10, pady=10)

        # Button to exit the window
        button = CTkButton(self, text="Exit", fg_color="#C850C0", font=("Arial", 15), corner_radius=5, width=100, height=40, command=lambda: self.quit())
        button.place(relx=0.5, rely=0.8, anchor="center")


# second window frame page1
class LoginPage(tk.CTkFrame):

    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)
        label = CTkLabel(self, text="Login In", fg_color="transparent", font=("bold", 20))
        label.place(relx=0.2, rely=0.1)

        label1 = CTkLabel(self, text="Please enter your login information below", fg_color="transparent")
        label1.place(relx=0.2, rely=0.15)

        email = CTkEntry(self, placeholder_text="Enter Email", corner_radius=0, border_width=0)
        email.place(relx=0.2, rely=0.25)

        password = CTkEntry(self, placeholder_text="Password", corner_radius=0, border_width=0, show="*")
        password.place(relx=0.2, rely=0.375)

        checkbox = CTkCheckBox(self, text="Remember Me", onvalue="on", offvalue="off")
        checkbox.place(relx=0.2, rely=0.5)

        button = CTkButton(self, text="Log In", fg_color="#C850C0", corner_radius=5, width=300, height=40, command=lambda: (login_handler(self, email, password)))
        button.place(relx=0.5, rely=0.7, anchor="center")

        goBack = CTkButton(self, text="Go Back", fg_color="#C850C0", font=("Arial", 15), corner_radius=5, width=300, height=40, command=lambda: controller.show_frame(StartPage))
        goBack.place(relx=0.5, rely=0.8, anchor="center")

# third window frame page2
class SignUpPage(tk.CTkFrame):
    def __init__(self, parent, controller):
        tk.CTkFrame.__init__(self, parent)

        label = CTkLabel(self, text="Sign Up", fg_color="transparent", font=("bold", 20))
        label.place(relx=0.2, rely=0.1)

        label = CTkLabel(self, text="Please Sign up by entering your details below", fg_color="transparent",
                         font=("bold", 15))
        label.place(relx=0.2, rely=0.15)

        username_entry = CTkEntry(self, placeholder_text="Username", corner_radius=0, border_width=0)
        username_entry.pack()
        username_entry.place(relx=0.2, rely=0.25)

        email = CTkEntry(self, placeholder_text="Enter Email", corner_radius=0, border_width=0)
        email.pack()
        email.place(relx=0.2, rely=0.35)

        password_entry = CTkEntry(self, placeholder_text="Password", corner_radius=0, border_width=0, show="*")
        password_entry.pack()
        password_entry.place(relx=0.2, rely=0.45)

        password = CTkEntry(self, placeholder_text="Confirm Password", corner_radius=0, border_width=0, show="*")
        password.pack()
        password.place(relx=0.2, rely=0.55)

        button = CTkButton(self, text="Sign Up", fg_color="#C850C0", corner_radius=5, width=300, height=40, command=lambda: (signin_handler(email, password)))
        button.place(relx=0.5, rely=0.7, anchor="center")

        goBack = CTkButton(self, text="Go Back", fg_color="#C850C0", font=("Arial", 15), corner_radius=5, width=300, height=40, command=lambda: controller.show_frame(StartPage))
        goBack.place(relx=0.5, rely=0.8, anchor="center")


# Driver Code
app = tkinterApp()
app.mainloop()

