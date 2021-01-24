from tkinter import *
import Accounting3

def login(event):
    if username_input.get() == "admin" and password_input.get() == "admin":
        Accounting3.order_menu()
    else:
        print("Wrong username or password")


accounting_window = Tk()
accounting_window.title("Bill calculator")
username_label = Label(accounting_window, text='Username :').grid(row=1, column=0)
password_label = Label(accounting_window, text='Password :').grid(row=2, column=0)
username_input = Entry(accounting_window)
username_input.grid(row=1, column=1)
password_input = Entry(accounting_window)
password_input.grid(row=2, column=1)
login_button = Button(accounting_window, text="Login")
login_button.bind('<1>', login)
login_button.grid(row=3, column=1)
accounting_window.mainloop()
