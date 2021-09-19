from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
 
 
root = Tk()
root.title("Abraham learning tKinter")
 
# below are the types of message boxes that one can show in a screen
 
# messagebox.showerror : this returns ok
# messagebox.showinfo : this returns ok too
# messagebox.showwarning: this returns ok too
# messagebox.askquestion: this returns yes or no
# messagebox.askokcancel : this returns one or zero
# messagebox.askretrycancel : this returns one or zero 
# messagebox.askyesno : this returns one or zero
 
# The errors come with a audio sound same as that of computer
 
 
def popup():
    response =  messagebox.askyesno("This is my popup!", "Hello world")
    Label(root, text=response).pack()
    # we store the response of the message box
 
    if response == "yes":
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked No").pack()
 
 
    # if response == 1:
    #     Label(root, text="You clicked yes").pack()
    # else:
    #     Label(root, text="You clicked No").pack()
 
 
# the first part appears at the top of the pop up
# the second part is the actual message that is displayed by the popup
Button(root, text="popup", command=popup).pack()
 
mainloop()
