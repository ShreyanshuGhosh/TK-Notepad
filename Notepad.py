from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newfile():
    global file
    root.title('Untitled')
    file = None
    inp_area.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[('All files', '*.*'), ('Text Documents', '*.txt')])
    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + '- Notepad')
        inp_area.delete(1.0, END)
        f = open(file, 'r')
        inp_area.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                 filetypes=[('All files', '*.*'), ('Text Documents', '*.txt')])
        if file == '':
            file = None

        else:
            # Save as a new file
            f = open(file, 'w')
            f.write(inp_area.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + '- Notepad')
            print('saved')
    else:
        # Save the new file
        f = open(file, 'w')
        f.write(inp_area.get(1.0, END))
        f.close()


def Cut():
    inp_area.event_generate('<<Cut>>')


def Copy():
    inp_area.event_generate('<<Copy>>')


def Paste():
    inp_area.event_generate('<<Paste>>')


def about():
    showinfo('Notepad', 'NOTEPAD by SG')


root = Tk()

if __name__ == '__main__':
    # main window
    root.geometry('700x400')
    root.wm_iconbitmap('notepad.ico')
    root.title('Untitled-NOTE')

    # Entry area
    inp_area = Text(root, font='Times 14')
    file = None
    inp_area.pack(expand=True, fill=BOTH)

    # Menu bar
    mymenu = Menu(root)

    m1 = Menu(mymenu, tearoff=0)
    m1.add_command(label='New', command=newfile)
    m1.add_command(label='Open', command=openfile)
    m1.add_command(label='Save', command=savefile)
    m1.add_separator()
    m1.add_command(label='Exit', command=quit)
    mymenu.add_cascade(label='File', menu=m1)

    m2 = Menu(mymenu, tearoff=0)
    m2.add_command(label='Cut', command=Cut)
    m2.add_command(label='Copy', command=Copy)
    m2.add_command(label='Paste', command=Paste)
    mymenu.add_cascade(label='Edit', menu=m2)

    m3 = Menu(mymenu, tearoff=0)
    m3.add_command(label='About', command=about)
    mymenu.add_cascade(label='Help', menu=m3)

    root.config(menu=mymenu)

    # Scrollbar
    scroll = Scrollbar(inp_area)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=inp_area.yview)
    inp_area.config(yscrollcommand=scroll.set)

root.mainloop()
