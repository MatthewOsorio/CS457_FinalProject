import tkinter as tk

root = tk.Tk()
root.title("OtakuGPT")
root.geometry("800x600")

#Display Logo
logoFrame= tk.Frame(root, height= 300, width= 300)
logoFrame.place(relx=0.5, rely=0.35, anchor="center")
logoImage= tk.PhotoImage(file="logo.png")
logoLabel= tk.Label(logoFrame, image=logoImage)
logoLabel.pack(expand=True)

#username login
loginUsernameFrame= tk.Frame(root, height=50, width=400)
loginUsernameFrame.place(relx=0.5, rely=0.6, anchor="center")
usernameLabel=tk.Label(loginUsernameFrame, text="Username")
usernameLabel.place(relx=0.0, rely=0.0, anchor="nw")
username_var= tk.StringVar()
usernameEntry= tk.Entry(loginUsernameFrame, textvariable= username_var, width=43)
usernameEntry.place(relx= 0.0, rely=0.43, anchor='nw')

#Display password login
# loginUsernameFrame= tk.Frame(root, height=25, width=400, bg= 'blue')
# loginUsernameFrame.place(relx=0.5, rely=0.65, anchor= "center")

root.mainloop()
