from tkinter import *
from tkinter import messagebox
from tkinter import font

w=Tk()
w.title('Sudoku')
w.configure(bg="white")
w.resizable(False,False)
f1=font.Font(w,family="Microsoft JhengHei UI",size=20)
f2=font.Font(w,family="Calibri",size=18)
frm=Frame(w)
for i in range(9):
    for j in range(9):
        e1=Entry(frm,width=3,bd=2,font=f2)
        e1.grid(row=j,column=i)
frm.grid()
Button(w,text="Solve",fg="white",bg="blue",font=f2,width=32,bd=0).grid(row=1,column=0)


w.mainloop()
