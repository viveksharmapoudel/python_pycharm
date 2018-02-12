from tkinter import *
from tkinter import ttk


def get_sum(event):
    num1=int(num1Entry.get())
    num2=int(num2Entry.get())

    answerEntry.delete(0,"end")
    answerEntry.insert(0,(num1+num2))


def get_sub(event):
    num1=int(num1Entry.get())
    num2=int(num2Entry.get())

    answerEntry.delete(0,"end")
    answerEntry.insert(0,(num1-num2))

def get_mul(event):
    num1=int(num1Entry.get())
    num2=int(num2Entry.get())

    answerEntry.delete(0,"end")
    answerEntry.insert(0,(num1*num2))

def get_div(event):
    num1=int(num1Entry.get())
    num2=int(num2Entry.get())

    answerEntry.delete(0,"end")
    answerEntry.insert(0,(num1/num2))


root =Tk()

#first Number Entry
Label(root,text="First Number").grid(row=0,column=0,sticky=W,padx=4)
num1Entry=Entry(root)
num1Entry.grid(row=1,column=0,sticky=W,padx=4)

#second Number Entry
Label(root,text="second Number").grid(row=0,column=1,sticky=W,padx=4)
num2Entry=Entry(root)
num2Entry.grid(row=1,column=1,sticky=W,padx=4)

#operation button label
Label(root,text="Operations").grid(row=2,column=0,sticky=W,padx=4)




#operation buttons sum
equalButton_sum=Button(root,text="+")
equalButton_sum.bind("<Button-1>",get_sum)
equalButton_sum.grid(row=3,column=0,sticky=W)

#operation buttons sub
equalButton_sub=Button(root,text="-")
equalButton_sub.bind("<Button-1>",get_sub)
equalButton_sub.grid(row=4,column=0,sticky=W)


#operation buttons mul
equalButton_mul=Button(root,text="*")
equalButton_mul.bind("<Button-1>",get_mul)
equalButton_mul.grid(row=5,column=0,sticky=W)

#operation buttons div
equalButton_div=Button(root,text="/")
equalButton_div.bind("<Button-1>",get_div)
equalButton_div.grid(row=6,column=0,sticky=W)









# label of answer
Label(root,text="Answer").grid(row=7,column=1,sticky=W,padx=4)
answerEntry=Entry(root)
answerEntry.grid(row=8,column=1,sticky=W,padx=4)





mainloop()
