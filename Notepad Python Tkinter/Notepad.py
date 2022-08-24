# Building Notepad by GUI
import os
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,  asksaveasfilename

# root = Tk()
# root.geometry("733x434")
# root.title("Untitled - Notepad by Rohan")
# root.wm_iconbitmap("notepad.ico")

# root.mainloop()

# The below are preset rules to code Reusability
# You can run either this or that


def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
                                 ("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:
            f = open(file, "w")
            # here 1.0 is 1st coulumn and 0th row
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file)+" - Notepad")
            print("File saved Successfully.. as", file)
    else:
        f = open(file, "w")
        # here 1.0 is 1st coulumn and 0th row
        f.write(textarea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()


def cut():
    textarea.event_generate(("<<Cut>>"))


def copy(): 
    textarea.event_generate(("<<Copy>>"))


def paste():
    textarea.event_generate(("<<Paste>>"))


def about():
    tmsg.showinfo("About", "NotePad by Rohan")


if __name__ == '__main__':
    root = Tk()
    root.geometry("733x434")
    root.title("Untitled - Notepad by Rohan")
    root.wm_iconbitmap("notepad.ico")

    # Adding TextArea
    textarea = Text(root, font="Helvetica 15")
    file = None
    textarea.pack(fill=BOTH, expand=True)

    # Menu Bar
    menubar = Menu(root)

    # File Menu Start
    filemenu = Menu(menubar, tearoff=0)

    # Open file
    filemenu.add_command(label="New", command=newfile)

    # open already existing file
    filemenu.add_command(label="Open", command=openfile)

    # to save
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quitapp)
    menubar.add_cascade(label="File", menu=filemenu)
    # cascade puts above filemenu inside sth
    # File Menu End

    # Edit Menu start
    editmenu = Menu(menubar, tearoff=0)

    #cut, copy, paste
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=editmenu)
    # Edit Menu End

    # Help starts
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About Notepad", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
    # Help ends
    root.config(menu=menubar)

    # Adding Scrollbar
    scroll = Scrollbar(textarea, cursor="hand2")
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)

    root.mainloop()