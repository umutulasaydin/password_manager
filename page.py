import generation as gn
import tkinter as tk
from tkinter import messagebox as mb
import database as db

def page():


    def make_menu(w):
        global the_menu
        the_menu = tk.Menu(page, tearoff = 0)
        the_menu.add_command(label='Copy')
        the_menu.add_command(label='Paste')


    def show_menu(e):
        w=e.widget
        the_menu.entryconfigure('Copy', command=lambda: w.event_generate('<<Copy>>'))
        the_menu.entryconfigure('Paste', command=lambda: w.event_generate('<<Paste>>'))
        the_menu.tk.call('tk_popup', the_menu, e.x_root, e.y_root)

    def delete_all():
        db.delete_all_pass()
        liste.delete(0, "end")

    def take_adding():

        name = e1.get()
        password = e2.get()
        note = e3.get()

        if name == "" or password == "":
            mb.showerror(title="Password Manager", message="Please fill name and password!")
            e1.delete(0, "end")
            e2.delete(0, "end")
            e3.delete(0, "end")

        else:
            db.add_pass(name, password, note)
            e1.delete(0, "end")
            e2.delete(0, "end")
            e3.delete(0, "end")  
            mb.showinfo(title="Password Manager", message="Password is added!")
        
        refresh()

    def deleted():
        value = liste.get("active")
        db.delete(value)
        liste.deleete("active")

    def generate():
        password = gn.generate()
        v4.set(password)

    def save():
        v3.set(e4.get())
        
    def refresh():
        a = db.read_all_pass()
        liste.insert("end", a[-1])

    
    page = tk.Tk()
    page.geometry("450x400")
    page.title("Password Manager")
    make_menu(page)


    main = tk.LabelFrame(page)
    page.grid()

    head = tk.Label(page, text = 'PASSWORD MANAGER\n Umut Ulaş Aydın\n umut200134@gmail.com')
    head.grid(row=0, column=0)

    restart = tk.Frame(page)
    restart.grid(row=0, column=1)
    

    
    res = tk.Button(restart, text = "Delete ALL Paswords", command = delete_all)
    res.grid()


    frame = tk.LabelFrame(page, text = "Add Password")
    frame.grid(row=1, column=0)

    l1 = tk.Label(frame, text = "Name: ")
    l1.grid(row=1, column=0)

    e1 = tk.Entry(frame)
    e1.grid(row=1, column=1)

    l2 = tk.Label(frame, text = "Password: ")
    l2.grid(row=2, column=0)

    e2 = tk.Entry(frame)
    e2.grid(row=2, column=1)

    l3 = tk.Label(frame, text = "Note: ")
    l3.grid(row=3, column=0)

    v3 = tk.StringVar()

    e3 = tk.Entry(frame, textvariable=v3)
    e3.grid(row=3, column=1)

    b1 = tk.Button(frame, text = "Add", command = take_adding)
    b1.grid(columnspan=2, rowspan=2)




    frame2 = tk.LabelFrame(page, text="Passwords")
    frame2.grid(row=1, column=1)

    sc = tk.Scrollbar(frame2, orient="vertical")
    sc.pack(fill="y", side="right")


    liste = tk.Listbox(frame2, width=40, yscrollcommand=sc)
    veriler = db.read_all_pass()

    for i in range(len(veriler)):
        liste.insert(i, veriler[i])
    liste.config(yscrollcommand= sc.set)
    sc.config(command = liste.yview)
    liste.pack()

    b2 = tk.Button(frame2, text = "Delete", command = deleted)
    b2.pack()



    frame3 = tk.LabelFrame(page, text = "Generate")
    frame3.grid(row=2, column=0)

    v4 = tk.StringVar()

    l4 = tk.Label(frame3, text="Click generate to see password.")
    l4.grid(row=0, column=0)

    e4 = tk.Entry(frame3, state = "readonly", textvariable=v4)
    e4.grid(row=1, column=0)
    e4.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

    b4 = tk.Button(frame3, text="Generate", command = generate)
    b4.grid(row=2, column=0)

    b5 = tk.Button(frame3, text="Save", command=save)
    b5.grid(row=2, column=1)
    


    page.mainloop()



page()
