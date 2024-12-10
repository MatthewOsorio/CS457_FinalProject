import tkinter as tk
from tkinter import ttk
import sv_ttk

def confirmLogin():
    print("username: " + username_var.get())
    print("password: " + password_var.get())

def createAccount():
    print("Creating new account")

root = tk.Tk()
root.title("OtakGPT")
root.geometry("800x600")

contentFrame= tk.Frame(root, height= 500, width= 400)
contentFrame.place(relx=0.5, rely= 0.5, anchor='center')

# Display Logo
logoFrame= tk.Frame(contentFrame, height= 300, width= 300)
logoFrame.place(relx=0.5, rely=0.35, anchor="center")
logoImage= tk.PhotoImage(file="logo.png")
logoLabel= tk.Label(logoFrame, image=logoImage)
logoLabel.pack(expand=True)

#username login
loginUsernameFrame= tk.Frame(contentFrame, height=70, width=300)
loginUsernameFrame.place(relx=0.50, rely=0.70, anchor="center")
usernameLabel=ttk.Label(loginUsernameFrame, text="Username", font=("Calibri", 12))
usernameLabel.place(relx=0.0, rely=0.0, anchor="nw")
username_var= tk.StringVar()
usernameEntry= ttk.Entry(loginUsernameFrame, textvariable= username_var, width=35)
usernameEntry.place(relx= 0.00, rely=0.3, anchor='nw')

#password login
loginPasswordFrame= tk.Frame(contentFrame, height=70, width=300)
loginPasswordFrame.place(relx=0.50, rely=0.81, anchor="center")
passwordLabel=ttk.Label(loginPasswordFrame, text="Password", font=("Calibri", 12))
passwordLabel.place(relx=0.0, rely=0.0, anchor="nw")
password_var= tk.StringVar()
passwordEntry= ttk.Entry(loginPasswordFrame, textvariable= password_var, width=35)
passwordEntry.place(relx= 0.00, rely=0.3, anchor='nw')

#submit buttom
subitButtomFrame = tk.Frame(contentFrame, height=50, width= 100)
subitButtomFrame.place(relx=0.80, rely= 0.90, anchor= 'center')
submitButton= ttk.Button(subitButtomFrame, text="Log in", command= confirmLogin)
submitButton.place(relx=0.5, rely=0.5, anchor='center')

#create account button
createAccountFrame = tk.Frame(contentFrame, height=50, width=120)
createAccountFrame.place(relx= 0.27, rely= 0.90, anchor= 'center')
createAccountButton= ttk.Button(createAccountFrame, text="Create account", command= createAccount)
createAccountButton.place(relx=0.5, rely=0.5, anchor='center')

sv_ttk.set_theme("dark")

root.mainloop()