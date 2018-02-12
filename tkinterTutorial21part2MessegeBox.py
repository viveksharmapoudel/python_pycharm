from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def open_msz_box():
    messagebox.showwarning(
        "event Triggered","Button Clicked"
    )

root= Tk()
root.geometry("400*400+300+300")
root.resizable(width=False,height=False)
frame=Frame(root)

style= ttk.Style()

style.configure("TButton",foreground="midnight blue",
                font="Times 20 bold italic",padding=20)




