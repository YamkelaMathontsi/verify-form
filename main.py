from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Info")
root.geometry("700x700")
root.config(bg="orange")

def clear_text():
    username_ent.delete(0, END)
    password_ent.delete(0, END)

def destroy():
    msg_box = messagebox.askquestion("Closing Programing, Are You Sure")
    root.destroy()

# Labels

username = Label(root, text="Username:")
username.place(x=20, y=70)
password = Label(root, text="Password:")
password.place(x=20, y=100)

#Entries

username_ent = Entry(root, text="")
username_ent.place(x=100, y=70)
password_ent = Entry(root, text="")
password_ent.place(x=100, y=100)


def user_pass_search():

    user_pass = {'Jayden': 'jaydenmay', 'Brent Lee': 'yourstepbro', 'Jason': 'faketaxi@17',
             'Yamkela': '@merclife'}

    if username_ent.get() in user_pass:
        if password_ent.get() == user_pass[username_ent.get()]:
            root.destroy()
            # import newwindow
        else:
            messagebox.showerror(message="Username and password does not match")
    else:
        messagebox.showerror(message="Username does not exist")

verify = Button(root, text='Verify', bg="pink", command=user_pass_search )
verify.place(x=20, y=150)
clear_btn = Button(root, text='Clear', bg="pink", command=clear_text)
clear_btn.place(x=120, y=150)
exit = Button(root, text='Exit', bg="pink", command=destroy)
exit.place(x=220, y=150)


root.mainloop()


