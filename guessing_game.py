from tkinter import *
from tkinter import messagebox
from tkinter import font
import random
w=Tk()
count=0
w.geometry('900x500+300+200')
w.configure(bg='white')
w.title("Guessing_Game")
x=random.randint(0,10)
f1=font.Font(w,family="Microsoft JhengHei UI",size=20)
f2=font.Font(w,family="Calibri",size=15)
e2=Entry(w,width=50,font=f2,bd=0)
e3=Entry(w,width=50,font=f2,bd=0)
def guess():
    global count
    b=e1.get()
    if len(b)==0 or b.isalpha():
        messagebox.showinfo('game','Enter the number')
    else:
        a=int(b)
        count+=1
        if(a==x):
            b=str(count)
            messagebox.showinfo("game","Congratulation! You Won the Game ")
            e2.place(x=100,y=275)
            e2.delete(0,END)
            e2.insert(0,"Number of attempts took to win the game")
            e3.place(x=475,y=275)
            e3.insert(0,b)
        elif(a>x):
            e2.place(x=100,y=275)
            e2.delete(0,END)
            e2.insert(0,"Your Cuurent Number is Greater than Guess number")            
        else:
            e2.place(x=100,y=275)
            e2.delete(0,END)
            e2.insert(0,"Your Current Number is Lesser than guess number")
            
def quit():
    w.destroy()

def clear():
    e2.delete(0,END)
    e3.delete(0,END)
    e1.delete(0,END)
Label(w,text="Guessing Game",font=f1,fg='blue',bg='white').place(x=250,y=50)
Label(w,text="Guess the number between 0 to 10",font=f2,fg='black',bg='white').place(x=100,y=100)
e1=Entry(w,width=30,font=f2,bd=0,justify=CENTER)
e1.place(x=100,y=150)
e1.focus_set()
nfrm=Frame(height=3,width=300,bg='black')
nfrm.place(x=100,y=175)
Button(w,text="Guess",font=f2,width=10,fg='white',bg='blue',command=guess,bd=0).place(x=150,y=400)
Button(w,text="Quit",font=f2,width=10,fg='white',bg='green',command=quit,bd=0).place(x=550,y=400)
Button(w,text="Clear",font=f2,width=10,fg='white',bg='red',command=clear,bd=0).place(x=350,y=400)
w.mainloop()
