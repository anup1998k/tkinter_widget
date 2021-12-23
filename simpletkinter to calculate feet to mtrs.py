import tkinter as tk
from tkinter import  IntVar, StringVar, ttk
from tkinter.constants import E, N, S, W



def Clicked(*args):
    x = float(entr.get())
    ans = x*0.305
    labl4.configure(text=ans)
    txt.set(0)
    





root = tk.Tk()
root.title('Feet to Meters')
sa = ttk.Style()
sa.configure('TFrame',background ='black')

fram = ttk.Frame(root,width = 7,padding= '4 4 12 12',style='TFrame')
fram.grid(column=0,row=0,sticky='N S E W')


txt = IntVar()
txt.set('you_can_enter_here')



entr =ttk.Entry(fram,textvariable=txt, ) 
entr.grid(column=1,row=0)

labl = ttk.Label(fram,text='feet',font=(24),foreground='white',background='blue')
labl.grid(column=2,row=0,pady=10,padx=30)


labl2 = ttk.Label(fram,text='is equivalent to ',font =(24) ,foreground='white',background='blue')
labl2.grid(column=0,row=1,pady=10)


labl3 = ttk.Label(fram,text='meters',font=(24),foreground='white',background='blue')
labl3.grid(column=2,row=1,pady=10,padx = 20)

text_lbl = IntVar().initialize(0)

 
labl4 = ttk.Label(fram,text=text_lbl,font = 25,foreground='blue',background='cyan')
labl4.grid(column=1,row=1,pady=10,padx = 20)

sa.configure('TButton',background = 'purple')

btn = ttk.Button(fram,text='Calculate/Clear',command=Clicked)
btn.grid(column=2,row=2,padx=10,pady=20)

btn = ttk.Button(fram,text='off',command=root.destroy)
btn.grid(column=0,row=2,padx=10,pady=20)

root.mainloop()