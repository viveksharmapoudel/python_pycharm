from tkinter import *
from tkinter import ttk


root= Tk()

Label(root,text="Description").grid(row=0,column=0,sticky=W)
Entry(root,width=50).grid(row=0,column=1)
Button(root,text="submit").grid(row=0,column=8)

Label(root,text="Quality").grid(row=1,column=0,sticky=W)
Radiobutton(root,text="New",value=1).grid(row=2,column=0,sticky=W)
Radiobutton(root,text="Good",value=2).grid(row=3,column=0,sticky=W)
Radiobutton(root,text="poor",value=3).grid(row=4,column=0,sticky=W)
Radiobutton(root,text="Damaged",value=4).grid(row=5,column=0,sticky=W)

Label(root,text="Benefits").grid(row=1,column=1,sticky=W)
Checkbutton(root,text="free shipping").grid(row=2,column=1,sticky=W)
Checkbutton(root,text="Festival Bonus").grid(row=3,column=1,sticky=W)

mainloop()