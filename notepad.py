from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()
root.geometry("700x600")
root.title("Notepad")

# functions...

def newFile():
    global file
    root.title("Unitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file =="":
        file = None

    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        
        else:
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()

            root.title(os.path.basname(file) + " - Notepad")

    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def help():
    msg.showinfo("Help", "Email us: Contact@notepad.com")

def about():
    msg.showinfo("About", "This is notepad")

# functions end...

# root.wm_iconbitmap("notepad.ico")
root.config(bg="gray")

#add text area
textArea = Text(root, font="arial, 20",)
file = None
textArea.pack(fill=BOTH, expand=True)


# dropdown mainmenu
mainMenu = Menu(root)

# file menu start
fileMenu = Menu(mainMenu, tearoff=0)
# menu options
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="New Window",)
fileMenu.add_separator()
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Save As",)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.destroy)
root.config(menu=mainMenu)
# all option handle by which option.
mainMenu.add_cascade(label="File", menu=fileMenu)
#file menu end



# Edit menu start
editMenu = Menu(mainMenu, tearoff=0)
# menu options
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)
root.config(menu=mainMenu)
# all option handle by which option.
mainMenu.add_cascade(label="Edit", menu=editMenu)
#edit menu end


# Help menu start
helpMenu = Menu(mainMenu, tearoff=0)
# menu options
helpMenu.add_command(label="Help", command=help)
helpMenu.add_command(label="About Notepad", command=about)
root.config(menu=mainMenu)
# all option handle by which option.
mainMenu.add_cascade(label="Help", menu=helpMenu)
#help menu end

# add scrolbar
scroll = Scrollbar(textArea)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=textArea.yview)
textArea.config(yscrollcommand=scroll.set)



root.mainloop()