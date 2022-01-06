from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
import time

from win32com.client import Dispatch
speak=Dispatch('SAPI.SpVoice')






root=Tk()
root.title('Calculator')
root.geometry('270x385')
root.minsize(270,385)
root.maxsize(270,385)
root.wm_iconbitmap('icons.ico')

root.configure(bg='black')
# root.minsize(272,450)
# root.maxsize(272,450)



sc_value=StringVar()
sc_value.set('Haider')



screen=Entry(root,textvar=sc_value,font='Lucida 30 normal')
screen.pack(side=TOP,fill=X,pady=10,ipadx=30)
screen.focus()

# Button Frame

btn_frame=Frame(root,bg='black')



# Buttons

def click(event):
    global sc_value
    text=event.widget.cget('text')
    if sc_value.get()=='Haider':
        # time.sleep()
        sc_value.set('')

        screen.update()
    if text=='='  and  sc_value.get()=='':
        sc_value.set('No Entry!')
        screen.update()
    elif text=='=' and sc_value.get()[0]=='0':
        sc_value.set(f"{sc_value.get()[1:]}")
        screen.update()
        value=eval(sc_value.get())
        sc_value.set(value)
        screen.update()

    elif text=='=':
        if sc_value.get().isdigit():
            value=int(sc_value.get())
        else:
            try:
                value=eval(sc_value.get())
            except Exception as e:
                value='Error '
        sc_value.set(value)
        screen.update()
    elif text=='C':
        sc_value.set('')
        screen.update()
        speak.Speak('clear')
    else:
        sc_value.set(sc_value.get() + text)
        screen.update()
 



btn1=Button(btn_frame,text='7',bg='white',fg='black',font='Arial 15 bold',width=3)
btn1.grid(row=0,column=0,pady=10,padx=10)
btn1.bind("<Button-1>",click)

btn2=Button(btn_frame,text='8',bg='white',fg='black',font='Arial 15 bold',width=3)
btn2.grid(row=0,column=1,pady=10,padx=10)
btn2.bind("<Button-1>",click)

btn3=Button(btn_frame,text='9',bg='white',fg='black',font='Arial 15 bold',width=3)
btn3.grid(row=0,column=2,pady=10,padx=10)
btn3.bind("<Button-1>",click)

btn4=Button(btn_frame,text='C',bg='white',fg='black',font='Arial 15 bold',width=3)
btn4.grid(row=0,column=3,pady=10,padx=10)
btn4.bind('<Button-1>',click)

btn5=Button(btn_frame,text='4',bg='white',fg='black',font='Arial 15 bold',width=3)
btn5.grid(row=1,column=0,pady=10,padx=10)
btn5.bind("<Button-1>",click)

btn6=Button(btn_frame,text='5',bg='white',fg='black',font='Arial 15 bold',width=3)
btn6.grid(row=1,column=1,pady=10,padx=10)
btn6.bind("<Button-1>",click)

btn7=Button(btn_frame,text='6',bg='white',fg='black',font='Arial 15 bold',width=3)
btn7.grid(row=1,column=2,pady=10,padx=10)
btn7.bind("<Button-1>",click)

btn8=Button(btn_frame,text='*',bg='white',fg='black',font='Arial 15 bold',width=3)
btn8.grid(row=1,column=3,pady=10,padx=10)
btn8.bind("<Button-1>",click)

btn9=Button(btn_frame,text='1',bg='white',fg='black',font='Arial 15 bold',width=3)
btn9.grid(row=2,column=0,pady=10,padx=10)
btn9.bind("<Button-1>",click)


btn0=Button(btn_frame,text='2',bg='white',fg='black',font='Arial 15 bold',width=3)
btn0.grid(row=2,column=1,pady=10,padx=10)
btn0.bind("<Button-1>",click)

btn_plus=Button(btn_frame,text='3',bg='white',fg='black',font='Arial 15 bold',width=3)
btn_plus.grid(row=2,column=2,pady=10,padx=10)
btn_plus.bind("<Button-1>",click)

btn_minus=Button(btn_frame,text='/',bg='white',fg='black',font='Arial 15 bold',width=3)
btn_minus.grid(row=2,column=3,pady=10,padx=10)
btn_minus.bind('<Button-1>',click)

btn_product=Button(btn_frame,text='0',bg='white',fg='black',font='Arial 15 bold',width=3)
btn_product.grid(row=3,column=0,pady=10,padx=10)
btn_product.bind("<Button-1>",click)

btn_divide=Button(btn_frame,text='.',bg='white',fg='black',font='Arial 15 bold',width=3)
btn_divide.grid(row=3,column=1,pady=10,padx=10)
btn_divide.bind("<Button-1>",click)

btn_equal=Button(btn_frame,text='00',bg='white',fg='black',font='Arial 15 bold',width=3)
btn_equal.grid(row=3,column=2,pady=10,padx=10)
btn_equal.bind("<Button-1>",click)

btn_sq=Button(btn_frame,text='+',bg='white',fg='black',font='Arial 15 bold',width=3)
btn_sq.grid(row=3,column=3,pady=10,padx=10)
btn_sq.bind("<Button-1>",click)

btn_product=Button(btn_frame,text='%',bg='white',fg='black',font='Arial 15 bold',width=3)
btn_product.grid(row=4,column=0,pady=10,padx=10)
btn_product.bind("<Button-1>",click)

btn_divide=Button(btn_frame,text='**',bg='white',fg='black',font='Arial 15 bold',width=3)
btn_divide.grid(row=4,column=1,pady=10,padx=10)
btn_divide.bind("<Button-1>",click)

btn_equal=Button(btn_frame,text='=',bg='white',fg='black',font='Arial 15 bold',width=3)
btn_equal.grid(row=4,column=2,pady=10,padx=10)
btn_equal.bind("<Button-1>",click)

btn_sq=Button(btn_frame,text='-',bg='white',fg='black',font='Arial 15 bold',width=3)
btn_sq.grid(row=4,column=3,pady=10,padx=10)
btn_sq.bind("<Button-1>",click)



btn_frame.pack(side=TOP,fill=Y)


def bind_serving(event):
    
    win=Tk()
    win.title('HELP')
    win.geometry('522x142')
    win.maxsize(522,142)
    win.configure(bg='light blue')
    Label(win,text='Calculator Is Made By\nHaider Ali Jutt',font='Courier 30 bold',bg='light blue').pack()
    Label(win,text='Coding in Python',font='Gabriola 20 normal',bg='light blue').pack()
    speak.Speak('History')
    win.mainloop()

# def new(event=None):
#     speak.Speak('You are quite the calculator why ?')
#     root.destroy()


# root.bind('<Control-q>',quit)
root.bind('<Control-h>',bind_serving)




root.mainloop()
speak.Speak('Exit')

