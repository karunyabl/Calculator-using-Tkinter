from tkinter import *
import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#c8a2c8")
eq=""

def show (value):
    global eq
    eq+=value
    label_result.gonfig(text=eq)

def clear():
    global eq
    eq=""
    label_result.config(text=eq)

def cal():
    global eq
    result=""
    if eq!="":
        try:
            result=eval(eq)
        except:
            result="error"
            eq=""
    label_result.config(test=result)

label_result= Label(root, width=25, height=2, text="", font=("Times",30))
label_result.pack()

Button(root,text="C", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#6495ED",command=lambda: clear()).place(x=10,y=100)
Button(root,text="/", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#6495ED",command=lambda: show("/")).place(x=150,y=100)
Button(root,text="%", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#6495ED",command=lambda: show("%")).place(x=290,y=100)
Button(root,text="*", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#6495ED",command=lambda: show("*")).place(x=430,y=100)

Button(root,text="7", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#F88379",command=lambda: show("7")).place(x=10,y=200)
Button(root,text="8", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#F88379",command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#F88379",command=lambda: show("9")).place(x=290,y=200)
Button(root,text="-", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#B284BE",command=lambda: show("-")).place(x=430,y=200)



Button(root,text="4", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#F88379",command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#F88379",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#F88379",command=lambda: show("6")).place(x=290,y=300)
Button(root,text="+", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#B284BE",command=lambda: show("+")).place(x=430,y=300)


Button(root,text="1", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#F88379",command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#F88379",command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#F88379",command=lambda: show("3")).place(x=290,y=400)
Button(root,text="0", width=11,height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#B284BE",command=lambda: show("0")).place(x=10,y=500)


Button(root,text=".", width=5, height=1,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#588BAE",command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=", width=5, height=3,font=("Times",30,"bold"),bd=1,fg="#fff",bg="#95CADB",command=lambda: calculate()).place(x=430,y=400)
