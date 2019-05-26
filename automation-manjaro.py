# !/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk	# import to can use ttk progressbar
import os
import subprocess # subprocess.getoutput from check output in linux terminal 
import platform # import from detect system

root = Tk()
root.iconbitmap('charging.ico')
root.title('by Vhartz')
root.resizable(False,False)
progressbar = ttk.Progressbar(length=200, mode='determinate')
progressbar.pack(side="top")
progressbar.start(20)
root.after(2000, root.destroy)
root.mainloop()

os = platform.system()
if os == 'Windows':
 	print('Are you using Windows')
 	root = Tk()
 	root.title('by Vhartz')
 	root.iconbitmap('favicon.ico')
 	root.resizable(False,False)
 	label = Label(text="You're using Windows. You do not have any settings for this platform.", font='Times 12 bold').pack(side=TOP, pady=5, padx=5) 	
 	def exit():
 		root.destroy()
 	bt = Button(text='OK', font='Times 11 bold', command = exit).pack(side=TOP, pady=5, padx=5)
 	root.after(3000, root.destroy) # after used to execute an instruction after a certain time
 	root.mainloop()
elif os == 'Linux':
	print('Are you using Linux')
	def os_Window():
		root = Tk()
		root.title('by Vhartz')
		root.iconbitmap('favicon.ico')
		root.resizable(False,False)
		label = Label(text="You're using linux, but its not your man-made distro.", font='Times 12 bold').pack(side=TOP, pady=5, padx=5)
		def exit():
			root.destroy()
		bt = Button(text='OK', font='Times 9 bold', command = exit).pack(side=TOP, pady=5, padx=5)
		root.mainloop()
	dist = subprocess.getoutput('cat /etc/*-release | grep ID=m')
	if distro =='ID=manjaro':
		os.system('xterm -e sudo pacman-mirrors --country Brazil && xterm -e sudo timedatectl set-timezone America/Sao_Paulo')
	else:
		root = Tk()
		root.title('by Vhartz')
		root.iconbitmap('favicon.ico')
		root.resizable(False,False)
		label = Label(text="You are not using any platform that already has a saved automation configuration.", font='Times 12 bold').pack(side=TOP, pady=5, padx=5)
		def exit():
			root.destroy()
		root.after(3000, root.destroy)
		root.mainloop()
		print('error 404, the distribution is not manjaro')
else:	
	print('system not found')