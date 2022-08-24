from tkinter import *
from time import strftime

print("Digital Clock")

root=Tk()
root.title("Digital Clock")

root.resizable(0,0)

def time():
    str = strftime('%H:%M:%S %p')
    lbl.config(text=str)
    lbl.after(1000, time)

lbl = Label(root, font=('Helvetica', 50, 'bold'), background='black', foreground='red')
lbl.pack(anchor='center')

time()
mainloop()