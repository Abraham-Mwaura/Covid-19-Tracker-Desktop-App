from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

#these are for the api
import requests
import json


#creating an instance of root
root = Tk()
root.title("Covid1-19 Tracker and predictions")
root.geometry("1000x700")


#creating the first frame
frame = Frame(root)
frame.grid( row=0, column=0,sticky=N+S+W+E)


try:
    api_request= requests.get("https://covid-api.mmediagroup.fr/v1/cases")
    #converts the Data into a json file
    api=json.loads(api_request.text)
except Exception as e:
    api="Error"



       

#mounting the image on the frame
my_img = ImageTk.PhotoImage(Image.open("enlightened.ico"))
my_icon = Label(frame, image=my_img)
my_icon.grid(row=0, column=0, rowspan=14, sticky="NSEW",pady=100,padx=100)


label_haveAccount = Label(frame, text="Already have an account?", anchor=W)
label_haveAccount.grid(row=1, column=1, sticky="NSEW")

label_username = Label(frame, text="username", anchor=W)
label_username.grid(row=3, column=1, sticky='NSEW')
enter_username = Entry(frame, width=30)
enter_username .grid(row=4, column=1, sticky='NSEW')


label_password = Label(frame, text="Password", anchor=W)
label_password.grid(row=8, column=1, sticky='NSEW')
enter_password = Entry(frame, width=30)
enter_password .grid(row=9, column=1, sticky='NSEW')

def logOut():
    
    global response
    response =messagebox.askyesno("log-out window", "Do you want to log out")

    if response == 1:
        root.destroy()
    else:
        return

def global_window():
    global globe_welcome_Label
    global icon_backHome, icon_backHome1
    frame_globe= Frame(root)
    frame_globe.grid(column=0,row=0,sticky=N+S+W+E)
    frame.forget()
    globe_welcome_Label= Label(frame_globe, text="This is the global Data Window", font="Helvetica  25 bold",padx=100)
    globe_welcome_Label.grid(column=1,row=0)

    icon_backHome = Image.open("C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_globe, image=icon_backHome1, relief=RAISED,command=home_button)
    backHome_btn.grid(row=0, column=0,pady=5)


def yourHealth_window():
    global health_welcLabel
    global icon_backHome, icon_backHome1

    frame_health= Frame(root)
    frame_health.grid(column=0,row=0,sticky=N+S+W+E)
    frame.forget()

    health_welcLabel= Label(frame_health, text="This is the Customers Health Window", font="Helvetica  25 bold",padx=100)
    health_welcLabel.grid(column=1,row=0)

    icon_backHome = Image.open("C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_health, image=icon_backHome1, relief=RAISED,command=home_button)
    backHome_btn.grid(row=0, column=0,pady=5)


def yourInfo_window():
    global info_welcLabel
    global icon_backHome, icon_backHome1

    frame_info= Frame(root)
    frame_info.grid(column=0,row=0,sticky=N+S+W+E)
    frame.forget()

    info_welcLabel= Label(frame_info, text="This is the Customers Personal Information Window", font="Helvetica  25 bold",padx=100)
    info_welcLabel.grid(column=1,row=0)

    icon_backHome = Image.open("C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_info, image=icon_backHome1, relief=RAISED,command=home_button)
    backHome_btn.grid(row=0, column=0,pady=5)

def developer_window():
    global dev_welcLabel
    global icon_backHome, icon_backHome1

    frame_dev= Frame(root)
    frame_dev.grid(column=0,row=0,sticky=N+S+W+E)
    frame.forget()

    dev_welcLabel= Label(frame_dev, text="We like coding, coding is the best thing that happened to us", font="Helvetica  25 bold",padx=100)
    dev_welcLabel.grid(column=1,row=0)

    icon_backHome = Image.open("C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_dev, image=icon_backHome1, relief=RAISED,command=home_button)
    backHome_btn.grid(row=0, column=0,pady=5)


def home_button():
    # root, options) one can also include some options here
    frame1 = Frame(root)
   # We fill up the screen for expansion, then forget previous frame
    frame1.grid(column=0, row=0, sticky=N+S+W+E)
    #Dismounts the previous frame
    frame.forget()


    #This are the sidebar Menu icons
    global icon_menu, icon_globe, icon_programmer, icon_heartbeat, icon_info
    global menu_btn, globe_btn,programmer_btn, heartbeat_btn,info_btn
    global icon_menu1, icon_globe1, icon_programmer1, icon_heartbeat1, icon_info1

    #antialias is used to resize here
    icon_menu = Image.open("C:/Users/use/Desktop/Covid-19 Group project/menu_icon.png")
    icon_menu = icon_menu.resize((50, 50), Image.ANTIALIAS)
    icon_menu1 = ImageTk.PhotoImage(icon_menu)
    menu_btn = Button(frame1, image=icon_menu1, relief=RAISED)
    menu_btn.grid(row=0, column=0,pady=5)

    icon_globe = Image.open("C:/Users/use/Desktop/Covid-19 Group project/globe_icon.png")
    icon_globe= icon_globe.resize((50, 50), Image.ANTIALIAS)
    icon_globe1 = ImageTk.PhotoImage(icon_globe)
    globe_btn = Button(frame1, image=icon_globe1, relief=RAISED,command=global_window)
    globe_btn.grid(row=1, column=0,pady=5)

    icon_heartbeat = Image.open("C:/Users/use/Desktop/Covid-19 Group project/heartbeat_icon.png")
    icon_heartbeat = icon_heartbeat.resize((50, 50), Image.ANTIALIAS)
    icon_heartbeat1 = ImageTk.PhotoImage(icon_heartbeat)
    heartbeat_btn = Button(frame1, image=icon_heartbeat1, relief=RAISED,command=yourHealth_window)
    heartbeat_btn.grid(row=2, column=0,pady=5)

    icon_info= Image.open("C:/Users/use/Desktop/Covid-19 Group project/info_icon.png")
    icon_info = icon_info.resize((50, 50), Image.ANTIALIAS)
    icon_info1 = ImageTk.PhotoImage(icon_info)
    info_btn = Button(frame1, image=icon_info1, relief=RAISED,command=yourInfo_window)
    info_btn.grid(row=3, column=0,pady=5)

    icon_programmer = Image.open("C:/Users/use/Desktop/Covid-19 Group project/programmer_icon.png")
    icon_programmer = icon_programmer.resize((50, 50), Image.ANTIALIAS)
    icon_programmer1 = ImageTk.PhotoImage(icon_programmer)
    programmer_btn = Button(frame1, image=icon_programmer1, relief=RAISED,command=developer_window)
    programmer_btn.grid(row=4, column=0,pady=5)

    #Mounting the welcome label
    global welcome_label, feel_label
    welcome_label= Label(frame1, text="Welcome", font="Helvetica  25 bold",padx=100)
    welcome_label.grid(row=0, column=1,sticky=N+S+W+E,columnspan= 4,pady=20 )
      #how are you feel
    welcome_label= Label(frame1, text="How are you feeling today?", font="Helvetica  10 bold",padx=100)
    welcome_label.grid(row=2, column=1,sticky=N+S+W+E,columnspan= 3,pady=5 )
  

    #emoji Icons
    global icon_great, icon_bad, icon_notSure
    global great_btn, bad_btn,notSure_btn
    global icon_great1, icon_bad1, icon_notSure1


    icon_great = Image.open("C:/Users/use/Desktop/Covid-19 Group project/great_icon.png")
    icon_great = icon_great.resize((60, 60), Image.ANTIALIAS)
    icon_great1 = ImageTk.PhotoImage(icon_great)
    great_btn = Button(frame1, image=icon_great1, text='Great !', relief=FLAT,compound= TOP,font="Helvetica  8 bold")
    great_btn.grid(row=3, column=1,pady=5)


    icon_notSure = Image.open("C:/Users/use/Desktop/Covid-19 Group project/notSure_icon.png")
    icon_notSure= icon_notSure.resize((60, 60), Image.ANTIALIAS)
    icon_notSure1 = ImageTk.PhotoImage(icon_notSure)
    notSure_btn = Button(frame1, image=icon_notSure1, text="Not sure", compound= TOP,font="Helvetica  8 bold",relief=FLAT)
    notSure_btn.grid(row=3, column=2,pady=5)

  

    icon_bad = Image.open("C:/Users/use/Desktop/Covid-19 Group project/bad_icon.png")
    icon_bad = icon_bad.resize((60, 60), Image.ANTIALIAS)
    icon_bad1 = ImageTk.PhotoImage(icon_bad)
    bad_btn = Button(frame1, image=icon_bad1, relief=FLAT, compound=TOP,text=" Bad", font="Helvetica 8 bold")
    bad_btn.grid(row=3, column=3)


    #flags icons
    global icon_kenya
    global icon_kenya1
    global kenya_btn

    icon_kenya = Image.open("C:/Users/use/Desktop/Covid-19 Group project/kenya_icon.png")
    icon_kenya = icon_kenya.resize((60,30 ), Image.ANTIALIAS)
    icon_kenya1 = ImageTk.PhotoImage(icon_kenya)
    kenya_btn = Button(frame1, image=icon_kenya1, relief=FLAT, compound=LEFT,text="Kenya today", font="Helvetica 12 bold")
    kenya_btn.grid(row=4, column=1,columnspan=3)

    #Kenya stats label
    global label_cases, label_recoveries, label_deaths, label_vaccine
    label_cases = Label(frame1, text="CONFIRMED CASES \n "+ str(api["Kenya"]["All"]["confirmed"]),relief=GROOVE,font="Helvetica 10 bold")
    label_cases.grid(column=1, row=5,ipadx=25,pady=5,columnspan=3)

    label_recoveries = Label(frame1, text="CONFIRMED RECOVERIES \n "+str(api["Kenya"]["All"]["recovered"]) ,relief=GROOVE,font="Helvetica 10 bold")
    label_recoveries.grid(column=1, row=6,ipadx=5,columnspan=3)

    label_deaths = Label(frame1, text="CONFIRMED DEATHS \n "+str(api["Kenya"]["All"]["deaths"]),relief=GROOVE,font="Helvetica 10 bold")
    label_deaths.grid(column=1, row=7,ipadx=25,pady=5,columnspan=3)

    label_vaccine = Label(frame1, text="VACCINATION RATE \n"+str(api["Kenya"]["All"]["updated"]),relief=GROOVE,font="Helvetica 10 bold")
    label_vaccine.grid(column=1, row=8,ipadx=25,pady=5,columnspan=3)


    #global icon for stats
        
    global icon_global
    global icon_global1
    global global_btn

    icon_global = Image.open("C:/Users/use/Desktop/Covid-19 Group project/global_icon.png")
    icon_global = icon_global.resize((50,50 ), Image.ANTIALIAS)
    icon_global1 = ImageTk.PhotoImage(icon_global)
    global_btn = Button(frame1, image=icon_global1, relief=FLAT, compound=LEFT,text=" Global Stats", font="Helvetica 12 bold")
    global_btn.grid(row=4, column=4,columnspan=2)

    #global stats
    global label_G_cases, label_G_recoveries, label_G_deaths, label_G_vaccine
    label_G_cases = Label(frame1, text="CONFIRMED CASES \n"+str(api["Global"]["All"]["confirmed"]),relief=GROOVE,font="Helvetica 10 bold")
    label_G_cases.grid(column=4, row=5,ipadx=25,pady=5)

    label_G_recoveries = Label(frame1, text="CONFIRMED RECOVERIES \n "+str(api["Global"]["All"]["recovered"]),relief=GROOVE,font="Helvetica 10 bold")
    label_G_recoveries.grid(column=4, row=6,ipadx=5)

    label_deaths = Label(frame1, text="CONFIRMED DEATHS \n"+str(api["Global"]["All"]["deaths"]),relief=GROOVE,font="Helvetica 10 bold")
    label_deaths.grid(column=5, row=5,ipadx=25,pady=5)

    label_G_vaccine = Label(frame1, text="VACCINATION RATE \n"+str(api["Global"]["All"]["population"]),relief=GROOVE,font="Helvetica 10 bold")
    label_G_vaccine.grid(column=5, row=6,ipadx=25,pady=5)


    global icon_logOut, icon_logOut1
    global logOut_btn
    icon_logOut = Image.open("C:/Users/use/Desktop/Covid-19 Group project/logOut_icon.png")
    icon_logOut = icon_logOut.resize((50,50 ), Image.ANTIALIAS)
    icon_logOut1 = ImageTk.PhotoImage(icon_logOut)
    logOut_btn = Button(frame1, image=icon_logOut1, relief=FLAT,anchor=E, command=logOut)
    logOut_btn.grid(row=0, column=6)


    #Top stories
    global label_topStories,  btn_topStory1, btn_topStory2, btn_topStory3
    label_topStories = Label(frame1, text="COVID-19 Top Stories ",font="Helvetica 15 bold")
    label_topStories.grid(column=6, row=1,ipadx=25)

    btn_topStory1 = Button(frame1, text="TOP STORY 1",relief=GROOVE,font="Helvetica 10 bold")
    btn_topStory1.grid(column=6, row=2,ipady=5) #,ipadx=10,ipady=20,rowspan=2,sticky=N

    btn_topStory2 = Button(frame1, text="TOP STORY 2",relief=GROOVE,font="Helvetica 10 bold")
    btn_topStory2.grid(column=6, row=3,ipady=10) #,ipadx=10,ipady=20,rowspan=2,sticky=N

    btn_topStory3 = Button(frame1, text="TOP STORY 3",relief=GROOVE,font="Helvetica 10 bold")
    btn_topStory3.grid(column=6, row=4) #,ipadx=10,ipady=20,rowspan=2, sticky=N


login_Button = Button(frame, text="Login", command=home_button)
login_Button.grid(column=1, row=10)

label_haveAccount = Label(frame, text="Do not have an account?")
label_haveAccount.grid(column=1, row=11)


def sign_up():
    global signUp
    signUp = Tk()
    signUp.title("Sign-up Window")
    signUp.iconbitmap(
        "C:/Users/use/Desktop/Covid-19 Group project/enlightened.ico")

    # this is the size of the window
    signUp.geometry("450x450")

    label_CreateAccount = Label(
        signUp, text="Create account", font="Helvetica  18 bold")
    label_CreateAccount.grid(row=1, column=1, sticky='NSEW',padx=20)

    label_username = Label(signUp, text="username")
    label_username.grid(row=2, column=1, sticky='NSEW',padx=20)
    enter_username = Entry(signUp, width=30)
    enter_username .grid(row=3, column=1, sticky='NSEW',padx=20)

    label_email = Label(signUp, text="Email address")
    label_email.grid(row=4, column=1, sticky='NSEW',padx=20)
    enter_email = Entry(signUp, width=30)
    enter_email .grid(row=5, column=1, sticky='NSEW ',padx=20)

    label_password = Label(signUp, text="Password")
    label_password.grid(row=6, column=1, sticky='NSEW',padx=20)
    enter_password = Entry(signUp, width=30)
    enter_password .grid(row=7, column=1, sticky='NSEW',padx=20)

    label_password = Label(signUp, text="Password")
    label_password.grid(row=8, column=1, sticky='NSEW',padx=20)
    enter_password = Entry(signUp, width=30)
    enter_password .grid(row=9, column=1, sticky='NSEW',padx=20)

    submit_Button = Button(signUp, text="Submit", command=quit)
    submit_Button.grid(column=1, row=10,padx=20)


def quit():
    signUp.destroy()


sign_Button = Button(frame, text="Sign Up", command=sign_up)
sign_Button.grid(column=1, row=12,sticky='NSEW')


# Give all rows and columns a non-zero weight
# this helps the program to resize well
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)


# THE LABEL PASSWORD BELOW ARE FOR SPACING PURPOSES
label_password = Label(frame, anchor=W)

label_password.grid(row=14, column=1, sticky='NSEW')
label_password = Label(frame, anchor=W)
label_password.grid(row=15, column=1, sticky='NSEW')

root.mainloop()
