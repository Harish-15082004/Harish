from tkinter import *
from tkinter import font
from tkinter import messagebox
w=Tk()
w.geometry('950x500+300+200')
w.resizable(False,False)
w.configure(bg='white')

def convert():
    a=e1.get()
    if len(e1.get())==0:
        messagebox.showinfo("warning","Enter the Temperature") 
    elif(a.isnumeric()):
        d=int(a)
        F=((9/5)*d)+32
        f=str(F)
        e2.insert(0,f)
        K=d+273.15
        k=str(K)
        e3.insert(0,k)
    else:
        messagebox.showinfo("warning","Enter the digits")

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

f1=font.Font(w,family="Microsoft JhengHei UI",size=20)
f2=font.Font(w,family="Calibri",size=14)

Label(w,text="Temperture Convertor",font=f1,fg="blue",bg="white").place(x=250,y=50)
e1=Entry(w,font=f2,width=20,bd=0)
e1.place(x=100,y=150)
e1.focus_set()
Label(w,text="Celsius",font=f2,fg="black",bg="white").place(x=315,y=150)
nfrm=Frame(w,height=3,width=200,bg='black')
nfrm.place(x=100,y=175)
e2=Entry(w,font=f2,bd=0,width=20)
e2.place(x=100,y=200)
Label(w,text="Fahrenheit",font=f2,fg="black",bg="white").place(x=315,y=200)
nfrm1=Frame(w,height=3,width=200,bg='black')
nfrm1.place(x=100,y=225)
e3=Entry(w,font=f2,width=20,bd=0)
e3.place(x=100,y=250)
Label(w,text="Kelvin",font=f2,fg="black",bg="white").place(x=315,y=250)
nfrm2=Frame(w,height=3,width=200,bg='black')
nfrm2.place(x=100,y=275)

Button(w,text="Convert",fg="white",bg="blue",font=f2,width=10,bd=0,command=convert).place(x=100,y=325)
Button(w,text="Clear",fg="blue",bg="white",font=f2,width=10,bd=0,command=clear).place(x=300,y=325)


w.mainloop()
