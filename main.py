import tkinter
from tkinter import*
from tkinter  import messagebox
def login():
    username=username_entry .get()
    password=password_entry .get()
    if(username=="" and password==""):
        messagebox .showinfo("" , 'emptyblocks not allowed')
    elif (username=='vamsi' and password=='12345'):
        messagebox .showinfo("", 'login success')
        root.destroy()
    else:
        messagebox .showinfo("",'incorrect details')

root=tkinter.Tk()
root.title("welcome to instragram")
root. geometry("300x300")
global e1
global e2
label=Label (root,text="login to instragram",font= "ariel 20 bold",bg="red",fg="black").pack(fill='both')
label =Label (root,text="username",font='10').place (x=10,y=60)
label=Label(root,text="password",font="20").place(x=10,y=90)
username_entry=Entry(root,font="40")
username_entry.place(x=90,y=60)
password_entry=Entry(root,font="40")
password_entry .place(x=90,y=90)
b=Button (root,text="login",font= 90, command=login, bg= "white",fg= "black")
b.place(x=140,y=120)
root.mainloop()

