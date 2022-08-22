import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from graph import mainRT
from graph2 import mainHS
from inalert import altMain

# Configure main window
window = tk.Tk(className='greenhouse monitor')
window.geometry("1366x768")
window.configure(bg='#343434')

# Load images (hovered button #474747)
img1 = PhotoImage(file=r"./buttons/realtime.png")
img2 = PhotoImage(file=r"./buttons/historic.png")
img3 = PhotoImage(file=r"./buttons/alerts.png")
logo = PhotoImage(file=r"./buttons/logo.png")
leaf = PhotoImage(file=r"./buttons/leaf.png")

# Load hisWin images
titlehs = PhotoImage(file=r"./buttons/titlehs.png")
titleday = PhotoImage(file=r"./buttons/day.png")
titlemonth = PhotoImage(file=r"./buttons/month.png")
titleyear = PhotoImage(file=r"./buttons/year.png")
titlegraph = PhotoImage(file=r"./buttons/graficar.png")

# Load alertWin images
titleal = PhotoImage(file=r"./buttons/titleal.png")
titlename = PhotoImage(file=r"./buttons/name.png")
titleemail = PhotoImage(file=r"./buttons/email.png")
titlemin = PhotoImage(file=r"./buttons/min.png")
titlemax = PhotoImage(file=r"./buttons/max.png")
titlecreate = PhotoImage(file=r"./buttons/create.png")

# Configure logos
label1 = tk.Label(window, image=logo, bg="#343434")
label1.pack()
label1.place(x=567, y=1)

label2 = tk.Label(window, image=leaf, bg="#343434")
label2.pack()
label2.place(x=590, y=230)

# New windows
def hisWin():
    hiswd = Toplevel(window)
    hiswd.title("historic search")
    hiswd.geometry("500x668")
    hiswd.configure(bg='#343434')
 
    # hisWin labels
    hiswdlabel1 = tk.Label(hiswd, image=titlehs, bg="#343434")
    hiswdlabel1.pack()
    hiswdlabel1.place(x=22, y=26)
    
    hiswdlabel2 = tk.Label(hiswd, image=titleday, bg="#343434")
    hiswdlabel2.pack()
    hiswdlabel2.place(x=220, y=240)
    
    hiswdlabel3 = tk.Label(hiswd, image=titlemonth, bg="#343434")
    hiswdlabel3.pack()
    hiswdlabel3.place(x=215, y=330)
    
    hiswdlabel4 = tk.Label(hiswd, image=titleyear, bg="#343434")
    hiswdlabel4.pack()
    hiswdlabel4.place(x=218, y=420)
    
    # hisWin entries
    hiswdentry1 = tk.Entry(hiswd)
    hiswdentry1.place(x=165, y=210)
    
    hiswdentry2 = tk.Entry(hiswd)
    hiswdentry2.place(x=165, y=300)
    
    hiswdentry3 = tk.Entry(hiswd)
    hiswdentry3.place(x=165, y=390)
    
    # Functions
    def graph():
    	day = hiswdentry1.get()
    	month = hiswdentry2.get()
    	year = hiswdentry3.get()
    	mainHS(int(day), int(month), int(year))
    
    # Configure button
    def enterb1his(e):
    	B1i2 = PhotoImage(file="./buttons/graficarpress.png")
    	hisb1["image"] = B1i2
    	hisb1.image = B1i2
    	
    def leaveb1his(e):
    	B1i1 = PhotoImage(file="./buttons/graficar.png")
    	hisb1["image"] = B1i1
    	hisb1.image = B1i1
    	
    # Button
    hisb1 = tk.Button(hiswd, image=titlegraph, bg="#343434", activebackground="#343434", highlightthickness=0, bd=0, command=graph)
    hisb1.grid()
    hisb1.place(x=105, y=500)
    hisb1.bind("<Enter>", enterb1his)
    hisb1.bind("<Leave>", leaveb1his)
    
def alertWin():
	alwd = Toplevel(window)
	alwd.title("alerts")
	alwd.geometry("600x668")
	alwd.configure(bg='#343434')
	
	# alertWin labels
	alwdlabel1 = tk.Label(alwd, image=titleal, bg="#343434")
	alwdlabel1.pack()
	alwdlabel1.place(x=170, y=26)
	
	alwdlabel2 = tk.Label(alwd, image=titlename, bg="#343434")
	alwdlabel2.pack()
	alwdlabel2.place(x=120, y=240)
	
	alwdlabel3 = tk.Label(alwd, image=titleemail, bg="#343434")
	alwdlabel3.pack()
	alwdlabel3.place(x=390, y=240)
	
	alwdlabel4 = tk.Label(alwd, image=titlemin, bg="#343434")
	alwdlabel4.pack()
	alwdlabel4.place(x=105, y=400)
	
	alwdlabel5 = tk.Label(alwd, image=titlemax, bg="#343434")
	alwdlabel5.pack()
	alwdlabel5.place(x=353, y=400)
	
	# alertWin entries
	alwdentry1 = tk.Entry(alwd)
	alwdentry1.place(x=90, y=210)
	
	alwdentry2 = tk.Entry(alwd)
	alwdentry2.place(x=343, y=210)
	
	alwdentry3 = tk.Entry(alwd)
	alwdentry3.place(x=90, y=370)
	
	alwdentry4 = tk.Entry(alwd)
	alwdentry4.place(x=343, y=370)
	
	# Functions
	def inputal():
		name = alwdentry1.get()
		email = alwdentry2.get()
		tmin = alwdentry3.get()
		tmax = alwdentry4.get()
		altMain(name, email, int(tmin), int(tmax))
	
	# Configure button
	def enterb1al(e):
		B1i2 = PhotoImage(file="./buttons/createpress.png")
		alb1["image"] = B1i2
		alb1.image = B1i2
		
	def leaveb1al(e):
		B1i1 = PhotoImage(file="./buttons/create.png")
		alb1["image"] = B1i1
		alb1.image = B1i1
	
	# Button
	alb1 = tk.Button(alwd, image=titlecreate, bg="#343434", activebackground="#343434", highlightthickness=0, bd=0, command=inputal)
	alb1.grid()
	alb1.place(x=150, y=500)
	alb1.bind("<Enter>", enterb1al)
	alb1.bind("<Leave>", leaveb1al)

# Functions
def rtMonitor():
	mainRT()

# Configure buttons
def enterb1(e):
    B1i2 = PhotoImage(file="./buttons/realtimepress.png")
    b1["image"] = B1i2
    b1.image = B1i2

def leaveb1(e):
    B1i1 = PhotoImage(file="./buttons/realtime.png")
    b1["image"] = B1i1
    b1.image = B1i1
    
def enterb2(e):
    B1i2 = PhotoImage(file="./buttons/historicpress.png")
    b2["image"] = B1i2
    b2.image = B1i2

def leaveb2(e):
    B1i1 = PhotoImage(file="./buttons/historic.png")
    b2["image"] = B1i1
    b2.image = B1i1
    
def enterb3(e):
    B1i2 = PhotoImage(file="./buttons/alertspress.png")
    b3["image"] = B1i2
    b3.image = B1i2

def leaveb3(e):
    B1i1 = PhotoImage(file="./buttons/alerts.png")
    b3["image"] = B1i1
    b3.image = B1i1
    
b1 = tk.Button(window,image=img1, bg="#343434", activebackground="#343434", highlightthickness=0, bd=0, command=rtMonitor)
b1.grid()
b1.place(x=150, y=500)
b1.bind("<Enter>", enterb1)
b1.bind("<Leave>", leaveb1)

b2 = tk.Button(window,image=img2, bg="#343434", activebackground="#343434", highlightthickness=0, bd=0, command=hisWin)
b2.grid()
b2.place(x=550, y=500)
b2.bind("<Enter>", enterb2)
b2.bind("<Leave>", leaveb2)

b3 = tk.Button(window,image=img3, bg="#343434", activebackground="#343434", highlightthickness=0, bd=0, command=alertWin)
b3.grid()
b3.place(x=950, y=500)
b3.bind("<Enter>", enterb3)
b3.bind("<Leave>", leaveb3)

window.mainloop()
