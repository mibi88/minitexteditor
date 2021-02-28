#! /usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.scrolledtext as ScrolledText
from tkinter.filedialog import *

master = Tk()

st = ScrolledText.ScrolledText(master)
st.pack()
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


print( st.get(1.0, END) )
openfil = Button(master, text="Open", command=openf)
openfil.pack(side=LEFT)
saveasfil = Button(master, text="Save As", command=saveasf)
saveasfil.pack(side=RIGHT)
master.mainloop()