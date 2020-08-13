from tkinter import *
import tkinter.filedialog
root = Tk()
root.title("Text Aditor")
frame=Frame(root, width=1920, height=1080)
frame.pack()
text=Text(frame, bg="black", fg="green", font="Monospace", width=1920, height=1080)
text.config(insertbackground = "White")
text.place(x=0, y=0)
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=tkinter.filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()
def load():
    global text
    loadfile=tkinter.filedialog.askopenfilename(parent=root)
    f = open(loadfile)
    text.insert(INSERT, f.read())
menubar = Menu(root)
fileMenu = Menu(menubar)
fileMenu.add_command(label = "Save", command=saveas)
fileMenu.add_command(label = "Load", command=load)
menubar.add_cascade(label="File", menu=fileMenu)
fm = Menu(menubar)
fm.add_command(label = "Arial", command=lambda : text.config(font="Arial"))
fm.add_command(label = "Monospace", command=lambda : text.config("Monospace"))
fm.add_command(label = "Helvetica", command= lambda : text.config(font="Helvetica"))
fm.add_command(label = "Courier", command= lambda : text.config(font="Courier"))
menubar.add_cascade(label="Font", menu=fm)
root.configure(menu=menubar)   
root.mainloop()

