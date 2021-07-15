import tkinter as tk
from tkinter import messagebox as mb
import database



def register():

    def registry():

        nickname = e1.get()
        password = e2.get()

        database.add_login(nickname, password)
        mb.showinfo(title="Sign Up", message="Signed Up")
        register.withdraw()
        


    register = tk.Tk()
    register.geometry("250x250")
    register.title("Password Manager")

    
    register.columnconfigure(0, weight = 1, minsize = 75)
    register.columnconfigure(1, weight = 1, minsize = 75)
    register.rowconfigure(0, weight = 1, minsize = 1)
    register.rowconfigure(1, weight = 1, minsize = 1)
    register.rowconfigure(2, weight = 1, minsize = 1)


    l1 = tk.Label(register, text = "Nickname")
    l1.grid(row = 0, column = 0)

    l2 = tk.Label(register, text = "Password")
    l2.grid(row = 1, column = 0)


    
    e1 = tk.Entry(register)
    e1.grid(row = 0, column = 1)

    e2 = tk.Entry(register)
    e2.grid(row = 1, column = 1)

    b1 = tk.Button(register, text = "Sign Up", command=registry)
    b1.grid(row = 2, column = 1, padx = 3, pady = 3)

    register.mainloop()


def login():

    login = tk.Tk()
    login.geometry("250x250")
    login.title("Password Manager")

    
    login.columnconfigure(0, weight = 1, minsize = 75)
    login.columnconfigure(1, weight = 1, minsize = 75)
    login.rowconfigure(0, weight = 1, minsize = 1)
    login.rowconfigure(1, weight = 1, minsize = 1)
    login.rowconfigure(2, weight = 1, minsize = 1)


    l1 = tk.Label(login, text = "Nickname")
    l1.grid(row = 0, column = 0)

    l2 = tk.Label(login, text = "Password")
    l2.grid(row = 1, column = 0)

    v1 = tk.StringVar()
    v2 = tk.StringVar()

    e1 = tk.Entry(login, textvariable = v1)
    e1.grid(row = 0, column = 1)

    e2 = tk.Entry(login, textvariable = v2)
    e2.grid(row = 1, column = 1)

    b1 = tk.Button(login, text = "Sign In")
    b1.grid(row = 2, column = 1, padx = 3, pady = 3)

    login.mainloop()

