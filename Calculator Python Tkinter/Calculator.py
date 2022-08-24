#Building Calculator in GUI
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("298x500")
root.wm_iconbitmap("calc.ico")
root.title("Calculator by Rohan")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

scvalue = StringVar()
scvalue.set("")    

screen= Entry(root, textvariable=scvalue, font="Helvetica 25 bold")
screen.pack(fill=X, ipadx=6, pady=6, padx=8)

f = Frame(root, bg="grey")
b = Button(f, text="7",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="8",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="9",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="4",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="5",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="6",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="1",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="2",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="3",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="0",padx=23, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="+",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="-",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="*",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="%",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="//",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="C",padx=22, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text=".",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="=",padx=20, pady=12, font="lucida 14 bold", cursor="hand2")
b.pack(side=LEFT, padx=12, pady=6)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()