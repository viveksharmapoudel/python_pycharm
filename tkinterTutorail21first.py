from tkinter import *

def get_data(event=None):
    print("string:",strVar.get())
    print("integer:",intVar.get())
    print("double:",dblVar.get())
    print("boolean:",boolVar.get())

def bind_button(event=None):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>",get_data)

root = Tk()

strVar= StringVar()
intVar=IntVar()
dblVar=DoubleVar()
boolVar=BooleanVar()


strVar.set("enter String")
intVar.set("enter Integer")
dblVar.set("enter Double")
boolVar.set(True)

strEntry=Entry(root,textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry=Entry(root,textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry=Entry(root,textvariable=dblVar)
dblEntry.pack(side=LEFT)

theCheckButton=Checkbutton(root,text="switch",variable=boolVar)
theCheckButton.bind("<Button-1>",bind_button)
theCheckButton.pack(side=LEFT)


##for the final or get data button
getDataButton=Button(root,text="Get Data")
getDataButton.bind("<Button-1>",get_data)       # get data button
getDataButton.pack(side=LEFT)


root.mainloop()


