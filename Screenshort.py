import tkinter as tk
import pyautogui
import os,uuid

def filename():

		cdate=str(uuid.uuid4())+"pic.png"
		return os.path.join(os.getcwd(),cdate)
win=tk.Tk()
win.title("Take screenshot")
win.geometry('250x250')

def takescrennshot():
	screenshot=pyautogui.screenshot()
	filenameobj=filename()
	screenshot.save(filenameobj)
	#screenshot.save('C:\\Users\\Suraj\\Desktop\\New folder\\ss.png')

button=tk.Button(win,text="capture screenshot",command=takescrennshot)
button.pack()

win.mainloop() 