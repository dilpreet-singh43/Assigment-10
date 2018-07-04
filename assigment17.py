#1.
import tkinter
from tkinter import *
import sys
def exit():
    sys.exit()

root=Tk()
root.title("My app")
root.geometry("400x400")
root.resizable(False,False)
a=Label(root,text="HELLO WORLD !",width=150)
a.pack()
b=Button(root,text="click!",command=exit)
b.pack()

root.mainloop()




#2.
import tkinter
from tkinter import *

def show():
    print("Hey Hacker!")

root= Tk()
root.geometry("250x250")
b=Button(root,text="click",bg="cyan",fg="black",command=show)
b.pack()

root.mainloop()









#3.import tkinter
from tkinter import *
import sys

def exit():
    sys.exit()


def click():
    a.config(text="WELCOME!")


root=Tk()
root.geometry("400x400")

a=Label(root,text="HELLO WORLD !",width=150,fg="red")
a.pack()
f1=Frame(root)
f1.pack(side=TOP)

b1=Button(f1,width=30,text="exit!",bg="blue",command=exit)
b1.pack()

b2=Button(f1,width=30,text="label",bg="black",command=click)
b2.pack()

root.mainloop()








#4.
import tkinter
from tkinter import *

def show():
    print(entry.get())

root=Tk()
root.geometry("400x400")


entry=Entry(root,width=40)
entry.pack()
b=Button(root,text="click",width=20,bg="orange",command=show)
b.pack(side= TOP)

root.mainloop()
