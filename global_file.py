
from tkinter import *
from PIL import ImageTk, Image

def global_window(frame,frame_globe):
    global globe_welcome_Label
    global icon_backHome, icon_backHome1
    
    frame_globe.grid(column=0,row=0,sticky=N+S+W+E)
    frame.forget()
    globe_welcome_Label= Label(frame_globe, text="This is the global Data Window", font="Helvetica  25 bold",padx=100)
    globe_welcome_Label.grid(column=1,row=0)

    icon_backHome = Image.open("C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_globe, image=icon_backHome1, relief=RAISED)
    backHome_btn.grid(row=0, column=0,pady=5)

    