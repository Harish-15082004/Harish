from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
import csv
import pandas as pd
import os

w=Tk()
w.geometry('800x600')
w.title('contact')
w.resizable(False,False)
w.configure(bg='white')
frm1=Frame(w)
frm2=Frame(w)
frm3=Frame(w)
f1=font.Font(w,family='Microsoft JhengHei UI',size=20)
f2=font.Font(w,family='Calibri',size=14)
def write():
    global fields
    fields=['Name','Phone','Email']
    if(os.path.exists('data.txt')):
        with open('data.txt','a') as file:
            writer=csv.DictWriter(file,fieldnames=fields)
            writer.writerows(mydict)
    else:
        with open('data.txt','w',newline='\n') as file:
            writer=csv.DictWriter(file,fieldnames=fields)
            writer.writeheader()
            writer.writerows(mydict)
def load():
    tree.delete(*tree.get_children())
    with open('data.txt') as file:
        reader = csv.reading(file)
        header=next(reader)
        for row in reader:
            tree.insert('','end',values=row)
def add():
    e2.focus_set()
    frm1.grid_forget()
    frm2.grid()

def back():
    res=messagebox.askyesno("Exit","Do you want to Exit")
    if res==True:
        frm2.grid_forget()
        frm1.grid()
    else:
        return

def edit():
    x=tree.selection()
    if x==False:
        message.showinfo("edit","Select the contact First")
    else:
        frm1.grid_forget()
        frm3.grid()
        values=tree.item(x,'values')
        if values:
            e6.insert(0,values[0])
            e7.insert(0,values[1])
            e8.insert(0,values[2])
            e6.focus_set()

def back1():
    res=messagebox.askyesno("Exit","Do you want to Exit")
    if res==True:
        frm3.grid_forget()
        frm1.grid()
    else:
        return
def save():
    global mydict
    mydict=[{'Name':e2.get(),'Phone':e3.get(),'Email':e4.get()}]
    write()
    for item in tree.get_children():
        tree.delete(item)
    with open('data.txt', 'r',newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            phone = row['Phone']
            email = row['Email']
            tree.insert('', 'end', values=(name,phone,email))
    messagebox.showinfo("save","Contact Saved Successfully")
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    frm2.grid_forget()
    frm1.grid()

def delete():
    res=messagebox.askyesno("delete","Are you Sure to delete the contact")
    if res==True:
        x=tree.selection()[0]
        xvalues=tree.item(x,'values')
        with open('data.txt','r') as file:
            rows=list(csv.DictReader(file))
        with open('data.txt','w',newline='\n') as file:
            writer=csv.DictWriter(file,fieldnames=fields)
            writer.writeheader()
            for row in rows:
                if not (row['Name']==xvalues[0] and  row['Phone']==xvalues[1] and row['Email']==xvalues[2]):
                    writer.writerow(row)
        tree.delete(x)
        messagebox.showinfo("delete","contact deleted Successfully")
    else:
        return

def save1():
    fields=['Name','Phone','Email']
    x=tree.selection()[0]
    xvalues=tree.item(x,'values')
    with open('data.txt','r') as file:
        rows=list(csv.DictReader(file))
    with open('data.txt','w',newline='\n') as file:
        writer=csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        for row in rows:
            if not (row['Name']==xvalues[0] and  row['Phone']==xvalues[1] and row['Email']==xvalues[2]):
                writer.writerow(row)
    tree.delete(x)
    mydic=[{'Name':e6.get(),'Phone':e7.get(),'Email':e8.get()}]
    with open('data.txt','a') as file:
        writer=csv.DictWriter(file,fieldnames=fields)
        writer.writerows(mydic)

    for item in tree.get_children():
        tree.delete(item)
    with open('data.txt', 'r',newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            phone = row['Phone']
            email = row['Email']
            tree.insert('', 'end', values=(name,phone,email))

    messagebox.showinfo("save","contact changed successfully")

    frm3.grid_forget()
    frm1.grid()



    #Frame1----------------------------------------
        
nfrm1=Frame(frm1,height=100,width=800,bg='white')
nfrm1.grid(row=0,column=0)
Label(nfrm1,text='Contacts',fg='blue',bg='white',font=f1).place(x=10,y=10)
Button(nfrm1,text='Add Contacts',fg='black',bg='white',font=f2,bd=0,command=add).place(x=675,y=55)
nfrm2=Frame(frm1,height=500,width=800,bg='white')
nfrm2.grid(row=1,column=0)
bfrm=Frame(nfrm2,height=1,width=800,bg='black')
bfrm.place(x=0,y=10)
Label(nfrm2,text="Contact list",fg='black',bg='white',font=f2).place(x=10,y=20)
tree=ttk.Treeview(nfrm2,selectmode='browse')
tree.place(x=0,y=50,height=350)
vscrl=ttk.Scrollbar(nfrm2,orient="vertical",command=tree.yview)
vscrl.place(x=775,y=50,height=350)
tree.configure(yscrollcommand=vscrl.set)
tree['columns']=("Name","Phone","Email ID")
tree['show']='headings'
tree.column("Name",width=220,anchor=W)
tree.column("Phone",width=300,anchor=CENTER)
tree.column("Email ID",width=253,anchor=W)
tree.heading("Name",text='Name')
tree.heading("Phone",text='Phone NO ')
tree.heading("Email ID",text='Email ID')
Button(nfrm1,text='EDIT',fg='white',bg='blue',font=f2,bd=0,width=10,command=edit).place(x=300,y=60)
Button(nfrm1,text='DELETE',fg='white',bg='grey',font=f2,bd=0,width=10,command=delete).place(x=500,y=60)


frm1.grid()

    #Frame2--------------------------------Create Contact-------------------------

nfrm3=Frame(frm2,height=600,width=800,bg='white')
nfrm3.grid(row=0,column=0)
Label(nfrm3,text="Creating New Contact",fg='blue',bg='white',font=f1).place(x=50,y=10)
Label(nfrm3,text="Name",fg='black',bg='white',font=f2).place(x=50,y=100)
Label(nfrm3,text="Phone NO ",fg='black',bg='white',font=f2).place(x=50,y=150)
Label(nfrm3,text="Email ID ",fg='black',bg='white',font=f2).place(x=50,y=200)
e2=Entry(nfrm3,width=30,bd=2,font=f2)
e2.place(x=200,y=100)
e3=Entry(nfrm3,width=30,bd=2,font=f2)
e3.place(x=200,y=150)
e4=Entry(nfrm3,width=30,bd=2,font=f2)
e4.place(x=200,y=200)
Button(nfrm3,text='BACK',fg='blue',bg='white',font=f2,bd=0,command=back).place(x=100,y=300)
Button(nfrm3,text='SAVE',fg='white',bg='blue',font=f2,bd=0,width=10,command=save).place(x=350,y=300)

    #Frame3--------------------------------Edit Contact--------------------------

nfrm4=Frame(frm3,height=600,width=800,bg='white')
nfrm4.grid(row=0,column=0)
Label(nfrm4,text="Edit Exsisting Contact",fg='blue',bg='white',font=f1).place(x=50,y=10)
Label(nfrm4,text="Name",fg='black',bg='white',font=f2).place(x=50,y=100)
Label(nfrm4,text="Phone NO ",fg='black',bg='white',font=f2).place(x=50,y=150)
Label(nfrm4,text="Email ID ",fg='black',bg='white',font=f2).place(x=50,y=200)
e6=Entry(nfrm4,width=30,bd=2,font=f2)
e6.place(x=200,y=100)
e7=Entry(nfrm4,width=30,bd=2,font=f2)
e7.place(x=200,y=150)
e8=Entry(nfrm4,width=30,bd=2,font=f2)
e8.place(x=200,y=200)
Button(nfrm4,text='BACK',fg='blue',bg='white',font=f2,bd=0,command=back1).place(x=100,y=300)
Button(nfrm4,text='SAVE',fg='white',bg='blue',font=f2,bd=0,width=10,command=save1).place(x=350,y=300)
try:
    with open('data.txt', 'r',newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            phone = row['Phone']
            email = row['Email']
            tree.insert('', 'end', values=(name,phone,email))

except FileNotFoundError:
    pass
w.mainloop()
