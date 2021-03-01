#! /usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.scrolledtext as ScrolledText
from tkinter.filedialog import *
from tkinter.messagebox import *

master = Tk()
master.title("MiniTextEditor")
#commands
def openf():
    filename = askopenfilename(title="Open a text file ...",filetypes=[('txt files','.txt'),('all files','.*')])
    fichier = open(filename, "r")
    content = fichier.read()
    content = str(content)
    st.delete("1.0", END)
    st.insert(INSERT, content)
def saveasf():
    file = asksaveasfile(title="Save your file ...", mode='w', defaultextension=".txt")
    text = str(st.get(1.0, END))
    file.write(text)
    file.close()
def aboutmen():
    showinfo("About", "About\n________________________\nMiniTextEditor\nby mibi88\n________________________\n Thank you for using\nthis text editor !")
def newf():
    if askyesno("New file ...", "If you create a new file, you can lose content.\nDo you want to create a new file ?"):
        st.delete("1.0", END)
    else:
        showinfo("New file ...", "Your content wasn't deleted")
#---
#def undoa():
#    st.edit_undo()
#def redoa():
#    st.edit_redo()
#---
#def updatefont():
#    fontsiz = fontsize.get()
#    st.set(font = ("Liberation Serif", fontsiz)
#---
#fontsiz = 12
#---
commands = LabelFrame(master, text="File")
commands.pack(fill="both", expand="yes")
#===
newfil = Button(commands, text="New file", command=newf)
newfil.pack(side=LEFT)
#===
openfil = Button(commands, text="Open", command=openf)
openfil.pack(side=LEFT)
#===
saveasfil = Button(commands, text="Save As", command=saveasf)
saveasfil.pack(side=LEFT)
#---
#undo = Button(commands, text="Undo", command=undoa)
#undo.pack(side=LEFT)
#redo = Button(commands, text="Redo", command=redoa)
#redo.pack(side=LEFT)
#---
#value = DoubleVar()
#fontsize = Scale(commands, orient='horizontal', variable=value)
#fontsize.pack(side=LEFT)
#updatefont = Button(commands, text="Apply the selected font size", command=updatefont)
#updatefont.pack(side=LEFT)
#fontsiz = fontsize.get()
aboutmen = Button(commands, text="About", command=aboutmen)
aboutmen.pack(side=RIGHT)
#===
st = ScrolledText.ScrolledText(master)
#st = ScrolledText.ScrolledText(master, font = ("Liberation Serif", fontsiz))
st.pack(expand='yes', side=BOTTOM)

print( st.get(1.0, END) )
master.mainloop()