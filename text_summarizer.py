import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import *
from PreProcessData import clean_data


filename = ""
content = ""
summarize = ""

def create_summary_from_the_text(text, entry):
	tokens = clean_data(text, entry)


def OpenFile(entry):
	global filename
	global filepath
	global content
	global summarize
	filename = askopenfilename(filetypes=(("Text files", "*.txt"), ("CSV files", "*.csv"), ("All files", "*.*")),
		title="Choose a file"
		)

	infile = open(filename, 'r')
	content = infile.read()
	filepath= os.path.dirname(filename)
	entry.delete(0, END)
	entry.insert(0, filename)
	summarize = content

def ProcessFile(filename, textentry):
	infile = open(filename, 'r')
	content = infile.read()
	textentry.configure(state='normal')
	textentry.delete('1.0', END)
	textentry.insert('end', content)
	textentry.configure(state='disabled')

def center(app):
	app.update_idletasks()
	w = app.winfo_screenwidth()
	h = app.winfo_screenheight()
	size = tuple(int(i) for i in app.geometry().split('+')[0].split('x'))
	x = w//2-size[0]//2
	y = h//2 -size[1]//2
	app.geometry("%dx%d+%d+%d" % (size + (x, y)))

def createMenu(app):
	app.attributes('-alpha', 0.0)
	menubar = tk.Menu(app)
	filemenu = tk.Menu(menubar, tearoff=0)
	filemenu.add_command(label='Open', command=OpenFile)
	filemenu.add_command(label="Exit", command=app.destroy)
	menubar.add_cascade(label="File", menu=filemenu)
	app.config(menu=menubar)

def createTitle(app):
	app.title("Text Summarizer")
	app.minsize(600, 600)

def creatFrame(app):
	mf = Frame(app)
	mf.pack()
	f1 = Frame(mf, width=600, height=100)
	f1.pack(fill=tk.X)
	f2 = Frame(mf, width=600, height=100)
	f2.pack()
	f3 = Frame(mf, width=600, height=250)
	f3.pack()
	f4 = Frame(mf, width=600, height=100)
	f4.pack()

	Label(f1, text="Select Your File").grid(row=0, column=0, sticky='e')
	entry = Entry(f1, width=50)
	entry.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
	
	textEntry = Text(f3, state='disabled' ,width=600, height=10)
	textEntry.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
	
	# scrollbar = Scrollbar(textentry, borderw)

	Button(f1, text="Browse", command=lambda: OpenFile(entry)).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
	Button(f2, text="Process Now", width=32, command=lambda: ProcessFile(entry.get(), textEntry)).grid(sticky='ew', padx=10, pady=10)
	Button(f4, text="Summarize", width=32, command=lambda: create_summary_from_the_text(textEntry.get("1.0","end-1c"), textEntry)).grid(sticky='ew', padx=10, pady=10)


if __name__=='__main__':
	app = tk.Tk()
	createMenu(app)
	createTitle(app)
	center(app)
	creatFrame(app)
	app.mainloop()
