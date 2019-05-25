# !/usr/bin/python3

from tkinter import *
import os
import subprocess # subprocess.getoutput from check output in linux terminal 
import platform # import from detect system

os = platform.system()

if os == 'Windows':
 	print('Are you using Windows')
 	root = Tk()
 	root.iconbitmap('favicon.ico')
 	label = Label(text='Are you using Windows', font='Times 12 bold').pack(side=TOP)
 	def exit():
 		root.destroy()
 	bt = Button(text='OK', font='Times 11 bold', command = exit).pack(side=TOP)
 	root.mainloop()
elif os == 'Linux':
	print('Are you using Linux')
	root = Tk()
	root.iconbitmap('favicon.ico')
	label = Label(text='Are you using Linux', font='Times 12 bold').pack(side=TOP)
	def exit():
		root.destroy()
	bt = Button(text='OK', font='Times 9 bold', command = exit).pack(side=TOP)
	root.mainloop()
	dist = subprocess.getoutput('cat /etc/*-release | grep ID=m')
	if distro =='ID=manjaro':
		os.system('xterm -e sudo pacman-mirrors --country Brazil && xterm -e sudo timedatectl set-timezone America/Sao_Paulo')
	else:
		print('error 404, the distribution is not manjaro')
else:	
	print('system not found')