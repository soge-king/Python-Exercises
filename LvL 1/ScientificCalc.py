

from tkinter import *
import math as m

root=Tk()
root.title("PySci Calc")

#here i make the variable e as the "entry"
e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
e.grid(row=0, column=0,columnspan=5,padx=10,pady=15)
#pack is better than grid as grid allows you to size the window specifically how you want it
#instead of just using row and column, columnspan makes it simpler


lg = button(root, text="Log", )
lg.bind("<Button-1>", sc)  #sc function, basically scientific calculation
#bind set the funtion of the button
lg.grid(row=1, column=0)




zero = Button(root, text="0", relief=RIDGE, padx=10,pady=15, fg="Grey", bg="Black", command=lambda: click("0"))
zero.grid(row=7, column=2)



def click(to_print):
    old=e.get()
    e.delete(0, END)
    e.instert(0, old+to_print)
    return 

def sc(event):
    key=event.widget
    text=key['text']
    no=e.get()
    result=''
    if text=='deg':
        
