# MacroSwitch for xkeybindings. A Profiler for xkeybinding by hiperbolt ( Tomás Simões, tomasimoes03@gmail.com ) Originally wrote at 21:43:43, on the Sunday of 10th of April, 2016.
# Import Modules
import sys
import subprocess
from subprocess import call
import tkinter
from tkinter import messagebox

# Set Profiles
def profile1():
	try:
		reply = subprocess.call("cp ~/.macroswitchprofiles/mc-wars.msp ~/ && cd ~/ && rm .xbindkeysrc && mv mc-wars.msp .xbindkeysrc && killall -s1 xbindkeys && xbindkeys", shell=True)
		if reply < 0:
			messagebox.showinfo("Profile was not selected", "Profile 'Mc-Wars' was not selected. Error Code : child_term")
		else:
			messagebox.showinfo("Profile Selected", "Profile 'Mc-Wars' has been selected")
	except OSError as e:
		messagebox.showinfo("Profile Selected", "Profile 'Mc-Wars' was not selected. Error Code : OSError")
def profile2():
	try:
		reply = subprocess.call("cp ~/.macroswitchprofiles/clear.msp ~/ && cd ~/ && rm .xbindkeysrc && mv clear.msp .xbindkeysrc && killall -s1 xbindkeys && xbindkeys", shell=True)
		if reply < 0:
			messagebox.showinfo("Profile was not selected", "Profile 'Clear' was not selected. Error Code : child_term")
		else:
			messagebox.showinfo("Profile Selected", "Profile 'Clear' has been selected")
	except OSError as e:
		messagebox.showinfo("Profile Selected", "Profile 'Clear' was not selected. Error Code : OSError")
# Set Vars
main = tkinter.Tk()
main.title("MacroSwitch for xkeybindings")
main.geometry("300x100")

button1 = tkinter.Button(main, text = "Profile Mc-Wars", command = profile1)
button2 = tkinter.Button(main, text = "Profile Clear", command = profile2)

# Pack and Execute
button1.pack()
button2.pack()
main.mainloop()
