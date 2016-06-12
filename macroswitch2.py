from tkinter import *
from tkinter import messagebox
from sys import exit
from tkinter.filedialog import askopenfilename
import os
from os import listdir
from os.path import isfile, join
from subprocess import call

# Set your home directory here:
# Example - /home/hiperbolt
home = ""

# ----------------------------------------------------------------------------------------------------------------------
__author__ = 'hiperbolt'
mypath = home + "/macroswitchprofile"

class Root_Window:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1000x800")
        self.window.title("MacroSwitch2 - xbindkeys")
        self.frame1 = Frame(self.window)
        self.frame2 = Frame(self.window)
        self.frame3 = Frame(self.window)
        self.label1 = Label(self.frame1, text="Welcome to MacroSwitch 2 by hiperbolt.", font=(5))
        self.label2 = Label(self.frame2, text='What do you want to do?', font=(5), height=(13))
        self.button1 = Button(self.frame3, text='Choose Profile', width='15', command=lambda: self.new_window(Choose_Profile))
        self.button2 = Button(self.frame3, text='Edit Profile', width='15', command=lambda: self.new_window(Edit_Profile))
        self.button3 = Button(self.frame3, text='Add Profile', width='15', command=lambda: Add_Profile())
        self.button4 = Button(self.frame3, text='Credits', width='15', command=lambda: messagebox.showinfo("Credits" , "Originally Made by: hiperbolt / Tomás Simões (tomasimoes03@gmail.com)"))
        self.button5 = Button(self.frame3, text='Exit', width='15', command=lambda: exit())
        self.frame1.pack(anchor='nw')
        self.frame2.pack(anchor='center')
        self.frame3.pack(anchor='center')
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.label1.pack()
        self.label2.pack()

    def new_window(self, newwindowname):
        self.newwindowname = newwindowname
        self.newwindowname(Toplevel(self.window))


class Choose_Profile:

    def __init__(self, window):
        self.window = window
        self.window.title("Choose Profile")
        self.files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for availablefiles in self.files:
            button = Button(self.window, text=availablefiles, command=lambda availablefiles=availablefiles: self.choose(availablefiles))
            button.pack()

    def choose(self, selectedprofile):
        self.selectedprofile = selectedprofile
        call('cp ~/macroswitchprofile/%s ~/ && cd ~/ && rm .xbindkeysrc && mv %s .xbindkeysrc && killall -s1 xbindkeys && xbindkeys' % (selectedprofile, selectedprofile), shell=True)

    def close_window(self):
        self.window.destroy()


class Add_Profile:
    def __init__(self):
        self.filename = askopenfilename(initialdir='~')
        print(self.filename)
        call('cp %s %s' % (self.filename, mypath), shell=True)
        messagebox.showinfo("Profile Added", "The profile %s has been added." % self.filename)


class Edit_Profile:
    def __init__(self, window):
        self.window = window
        self.window.title("Edit Profile")
        self.files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for availablefiles in self.files:
            button = Button(self.window, text=availablefiles, command=lambda availablefiles=availablefiles: self.edit(availablefiles))
            button.pack()

    def edit(self, selectedprofile):
        self.selectedprofile = selectedprofile
        call('gedit %s/%s' % (mypath, selectedprofile), shell=True)


def main():
    root = Tk()
    Root_Window(root)
    root.mainloop()

a = 1
while a == 1:
    if os.path.exists(mypath):
        call('xbindkeys', shell=True)
        main()
        a = None
    else:
        call('xbindkeys', shell=True)
        call('mkdir %s' % mypath, shell=True)
        main()
        a = None
