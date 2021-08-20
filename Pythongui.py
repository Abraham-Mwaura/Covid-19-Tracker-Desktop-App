 
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
#import webbrowser
# these are for the api
import requests
import json
import pyrebase 

Config = {
    "apiKey": "AIzaSyDusq6Crtup5gEtC7uTvtMtkDZjuJorQQc",
    "authDomain": "covid-19-group-project.firebaseapp.com",
    "databaseURL": "https://covid-19-group-project-default-rtdb.firebaseio.com",
    "projectId": "covid-19-group-project",
    "storageBucket": "covid-19-group-project.appspot.com",
    "messagingSenderId": "320687700566",
    "appId": "1:320687700566:web:2b18881b3850ae72b6d9f7",
    "measurementId": "G-PNJPHDFBMC"
  }

  # Initialize Firebase
firebase= pyrebase.initialize_app(Config)
db = firebase.database()

thankGod= db.child("Story1").child("link").get()


print(thankGod.val())
# news_variables = [1,2,3]


# for index,  var in enumerate(news_variables):
    #  news_variables[index]=thankGod.val()
     
# creating an instance of root
root = Tk()
root.title("Covid1-19 Tracker and predictions")

root.iconbitmap("C:/Users/use/Desktop/Covid-19 Group project/logo_icon.ico")
root.geometry("1000x700")


# creating the first frame
frame = Frame(root)
frame.grid(row=0, column=0, sticky=N+S+W+E)


try:
    api_request = requests.get("https://covid-api.mmediagroup.fr/v1/cases")
    # converts the Data into a json file
    api = json.loads(api_request.text)
except Exception as e:
    api = "Error"


# mounting the image on the frame
my_img = ImageTk.PhotoImage(Image.open("enlightened.ico"))
my_icon = Label(frame, image=my_img)
my_icon.grid(row=0, column=0, rowspan=14, sticky="NSEW", pady=100, padx=100)


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
    response = messagebox.askyesno("log-out window", "Do you want to log out")

    if response == 1:
        root.quit()
    else:
        return


def global_window():
    global globe_welcome_Label
    global icon_backHome, icon_backHome1
    frame_globe = Frame(root)
    frame_globe.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)
    frame.forget()
    globe_welcome_Label = Label(
        frame_globe, text="This is the global Data Window", font="Helvetica  25 bold", padx=100)
    globe_welcome_Label.grid(column=1, row=0)

    icon_backHome = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_globe, image=icon_backHome1,
                          relief=RAISED, command=home_button)
    backHome_btn.grid(row=0, column=0, pady=5)


def yourHealth_window():
    global health_welcLabel
    global icon_backHome, icon_backHome1

    frame_health = Frame(root)
    frame_health.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)
    frame.forget()

    health_welcLabel = Label(
        frame_health, text="This is the Customers Health Window", font="Helvetica  25 bold", padx=100)
    health_welcLabel.grid(column=1, row=0)

    icon_backHome = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_health, image=icon_backHome1,
                          relief=RAISED, command=home_button)
    backHome_btn.grid(row=0, column=0, pady=5)


def yourInfo_window():
    global info_welcLabel
    global icon_backHome, icon_backHome1

    frame_info = Frame(root)
    frame_info.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)
    frame.forget()

    info_welcLabel = Label(
        frame_info, text="This is the Customers Personal Information Window", font="Helvetica  25 bold", padx=100)
    info_welcLabel.grid(column=1, row=0)

    icon_backHome = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_info, image=icon_backHome1,
                          relief=RAISED, command=home_button)
    backHome_btn.grid(row=0, column=0, pady=5)


def developer_window():
    global dev_welcLabel
    global icon_backHome, icon_backHome1

    frame_dev = Frame(root)
    frame_dev.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)
    frame.forget()

    dev_welcLabel = Label(
        frame_dev, text="We like coding, coding is the best thing that happened to us", font="Helvetica  25 bold", padx=100)
    dev_welcLabel.grid(column=1, row=0)

    icon_backHome = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_dev, image=icon_backHome1,
                          relief=RAISED, command=home_button)
    backHome_btn.grid(row=0, column=0, pady=5)


def home_button():
    # root, options) one can also include some options here
    frame1 = Frame(root)
   # We fill up the screen for expansion, then forget previous frame
    frame1.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)
   # frame1.grid(column=0, row=0, sticky=N+S+W+E)
    # Dismounts the previous frame
    frame.forget()

    # This are the sidebar Menu icons
    global icon_menu, icon_globe, icon_programmer, icon_heartbeat, icon_info, ico_bg
    global menu_btn, globe_btn, programmer_btn, heartbeat_btn, info_btn
    global icon_menu1, icon_globe1, icon_programmer1, icon_heartbeat1, icon_info1, icon_bg1

    icon_bg = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/bg_icon.png")
    icon_bg = icon_bg.resize((1600, 900), Image.ANTIALIAS)
    icon_bg1 = ImageTk.PhotoImage(icon_bg)
    bg_label = Label(frame1, image=icon_bg1)
    bg_label.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)

    # antialias is used to resize here
    icon_menu = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/menu_icon.png")
    icon_menu = icon_menu.resize((50, 50), Image.ANTIALIAS)
    icon_menu1 = ImageTk.PhotoImage(icon_menu)
    menu_btn = Button(frame1, image=icon_menu1, relief=RAISED)
    menu_btn.place(rely=0.00625, relx=0.00625)

    icon_globe = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/globe_icon.png")
    icon_globe = icon_globe.resize((50, 50), Image.ANTIALIAS)
    icon_globe1 = ImageTk.PhotoImage(icon_globe)
    globe_btn = Button(frame1, image=icon_globe1,
                       relief=RAISED, command=global_window)
    globe_btn.place(rely=0.125, relx=0.00625)

    icon_heartbeat = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/heartbeat_icon.png")
    icon_heartbeat = icon_heartbeat.resize((50, 50), Image.ANTIALIAS)
    icon_heartbeat1 = ImageTk.PhotoImage(icon_heartbeat)
    heartbeat_btn = Button(frame1, image=icon_heartbeat1,
                           relief=RAISED, command=yourHealth_window)
    heartbeat_btn.place(rely=0.25, relx=0.00625)

    icon_info = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/info_icon.png")
    icon_info = icon_info.resize((50, 50), Image.ANTIALIAS)
    icon_info1 = ImageTk.PhotoImage(icon_info)
    info_btn = Button(frame1, image=icon_info1,
                      relief=RAISED, command=yourInfo_window)
    info_btn.place(rely=0.375, relx=0.00625)

    icon_programmer = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/programmer_icon.png")
    icon_programmer = icon_programmer.resize((50, 50), Image.ANTIALIAS)
    icon_programmer1 = ImageTk.PhotoImage(icon_programmer)
    programmer_btn = Button(frame1, image=icon_programmer1,
                            relief=RAISED, command=developer_window)
    programmer_btn.place(rely=0.5, relx=0.00625)

    # Mounting the welcome label
    global welcome_label, feel_label
    welcome_label = Label(frame1, text="Welcome",
                          font="Helvetica  25 bold", padx=100, bg="#233D72", fg="white")
    welcome_label.place(rely=0.094444, relx=0.17222, relwidth=0.18)
    # how are you feel

    welcome_label = Label(frame1, text="How are you feeling today?",
                          font="Helvetica  10 bold", bg="#233D72", fg="white")
    welcome_label.place(rely=0.25, relx=0.085625)

    # emoji Icons
    global icon_great, icon_bad, icon_notSure
    global great_btn, bad_btn, notSure_btn
    global icon_great1, icon_bad1, icon_notSure1

    icon_great = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/great_icon.png")
    icon_great = icon_great.resize((60, 60), Image.ANTIALIAS)
    icon_great1 = ImageTk.PhotoImage(icon_great)
    great_btn = Button(frame1, image=icon_great1, text='Great !', relief=FLAT,
                       compound=TOP, font="Helvetica  8 bold", bg="#233D72", fg="white")
    great_btn.place(rely=0.3, relx=0.06375)

    icon_notSure = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/notSure_icon.png")
    icon_notSure = icon_notSure.resize((60, 60), Image.ANTIALIAS)
    icon_notSure1 = ImageTk.PhotoImage(icon_notSure)
    notSure_btn = Button(frame1, image=icon_notSure1, text="Not sure", compound=TOP,
                         font="Helvetica  8 bold", relief=FLAT, bg="#233D72", fg="white")
    notSure_btn.place(rely=0.3, relx=0.14126)

    icon_bad = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/bad_icon.png")
    icon_bad = icon_bad.resize((60, 60), Image.ANTIALIAS)
    icon_bad1 = ImageTk.PhotoImage(icon_bad)
    bad_btn = Button(frame1, image=icon_bad1, relief=FLAT, compound=TOP,
                     text=" Bad", font="Helvetica 8 bold", bg="#233D72", fg="white")
    bad_btn.place(rely=0.3, relx=0.225)

    # flags icons
    global icon_kenya
    global icon_kenya1
    global kenya_btn

    icon_kenya = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/kenya_icon.png")
    icon_kenya = icon_kenya.resize((60, 30), Image.ANTIALIAS)
    icon_kenya1 = ImageTk.PhotoImage(icon_kenya)
    kenya_btn = Button(frame1, image=icon_kenya1, relief=FLAT, compound=LEFT,
                       text="Kenya today", font="Helvetica 12 bold", bg="#233D72", fg="white")
    kenya_btn.place(rely=0.502, relx=0.133)

    # Kenya stats label
    global label_cases, label_recoveries, label_deaths, label_vaccine
    label_cases = Label(frame1, text="CONFIRMED CASES \n " + str(
        api["Kenya"]["All"]["confirmed"]), relief=GROOVE, font="Helvetica 10 bold")
    label_cases.place(relx=0.075, rely=0.586)

    label_recoveries = Label(frame1, text="CONFIRMED RECOVERIES \n "+str(
        api["Kenya"]["All"]["recovered"]), relief=GROOVE, font="Helvetica 10 bold")
    label_recoveries.place(relx=0.2195, rely=0.586)

    label_deaths = Label(frame1, text="CONFIRMED DEATHS \n "+str(
        api["Kenya"]["All"]["deaths"]), relief=GROOVE, font="Helvetica 10 bold")
    label_deaths.place(relx=0.075, rely=0.678)

    label_vaccine = Label(frame1, text="VACCINATION RATE \n"+str(
        api["Kenya"]["All"]["updated"]), relief=GROOVE, font="Helvetica 10 bold")
    label_vaccine.place(relx=0.2185, rely=0.678)

    # global icon for stats

    global icon_global
    global icon_global1
    global global_btn

    icon_global = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/global_icon.png")
    icon_global = icon_global.resize((50, 50), Image.ANTIALIAS)
    icon_global1 = ImageTk.PhotoImage(icon_global)
    global_btn = Button(frame1, image=icon_global1, relief=FLAT, compound=LEFT,
                        text=" Global Stats", font="Helvetica 12 bold", bg="#A8CBE6")
    global_btn.place(rely=0.4998, relx=0.610)

    #global stats
    global label_G_cases, label_G_recoveries, label_G_deaths, label_G_vaccine
    label_G_cases = Label(frame1, text="CONFIRMED CASES \n"+str(
        api["Global"]["All"]["confirmed"]), relief=GROOVE, font="Helvetica 10 bold")
    label_G_cases.place(relx=0.563, rely=0.6)

    label_G_recoveries = Label(frame1, text="CONFIRMED RECOVERIES \n "+str(
        api["Global"]["All"]["recovered"]), relief=GROOVE, font="Helvetica 10 bold")
    label_G_recoveries.place(relx=0.697, rely=0.6)

    label_deaths = Label(frame1, text="CONFIRMED DEATHS \n"+str(
        api["Global"]["All"]["deaths"]), relief=GROOVE, font="Helvetica 10 bold")
    label_deaths.place(relx=0.563, rely=0.688)

    label_G_vaccine = Label(frame1, text="VACCINATION RATE \n"+str(
        api["Global"]["All"]["population"]), relief=GROOVE, font="Helvetica 10 bold")
    label_G_vaccine.place(relx=0.697, rely=0.688)

    global icon_logOut, icon_logOut1
    global logOut_btn
    icon_logOut = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/logOut_icon.png")
    icon_logOut = icon_logOut.resize((50, 50), Image.ANTIALIAS)
    icon_logOut1 = ImageTk.PhotoImage(icon_logOut)
    logOut_btn = Button(frame1, image=icon_logOut1, anchor=E, command=logOut)
    logOut_btn.place(rely=0.01111, relx=0.9475)

    # Top stories
    global label_topStories,  btn_topStory1, btn_topStory2, btn_topStory3
    label_topStories = Label(frame1, text="COVID-19 Top Stories ",
                             font="Helvetica 15 bold", bg="#233D72", fg="white")
    label_topStories.place(relx=0.8625, rely=0.15)

    btn_topStory1 = Button(frame1, text="TOP STORY 1",
                           relief=GROOVE, font="Helvetica 10 bold")
 
    btn_topStory1.place(relx=0.8625, rely=0.2222)

    btn_topStory2 = Button(frame1, text="TOP STORY 2",
                           relief=GROOVE, font="Helvetica 10 bold")
  
    btn_topStory2.place(relx=0.8625, rely=0.30556)

    btn_topStory3 = Button(frame1, text="TOP STORY 3",
                           relief=GROOVE, font="Helvetica 10 bold")
    # ,ipadx=10,ipady=20,relyspan=2, sticky=N
    btn_topStory3.place(relx=0.8625, rely=0.3889)

    btn_topStory4 = Button(frame1, text="TOP STORY 4",
                           relief=GROOVE, font="Helvetica 10 bold")
    # ,ipadx=10,ipady=20,relyspan=2, sticky=N
    btn_topStory4.place(relx=0.8625, rely=0.4722)

    btn_topStory5 = Button(frame1, text="TOP STORY 5",
                           relief=GROOVE, font="Helvetica 10 bold")
    # ,ipadx=10,ipady=20,relyspan=2, sticky=N
    btn_topStory5.place(relx=0.8625, rely=0.5556)

    btn_topStory6 = Button(frame1, text="TOP STORY 6",
                           relief=GROOVE, font="Helvetica 10 bold")
    # ,ipadx=10,ipady=20,relyspan=2, sticky=N
    btn_topStory6.place(relx=0.8625, rely=0.6389)

    btn_topStory7 = Button(frame1, text="TOP STORY 7",
                           relief=GROOVE, font="Helvetica 10 bold")
    # ,ipadx=10,ipady=20,relyspan=2, sticky=N
    btn_topStory7.place(relx=0.8625, rely=0.7222)




    status_label= Label(frame1,
     text="LAST UPDATED ON "+str(
        api["Kenya"]["All"]["updated"]),relief=GROOVE)
    status_label.place(relx=0.00001, rely=0.98,relwidth=1)


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
    label_CreateAccount.grid(row=1, column=1, sticky='NSEW', padx=20)

    label_username = Label(signUp, text="username")
    label_username.grid(row=2, column=1, sticky='NSEW', padx=20)
    enter_username = Entry(signUp, width=30)
    enter_username .grid(row=3, column=1, sticky='NSEW', padx=20)

    label_email = Label(signUp, text="Email address")
    label_email.grid(row=4, column=1, sticky='NSEW', padx=20)
    enter_email = Entry(signUp, width=30)
    enter_email .grid(row=5, column=1, sticky='NSEW ', padx=20)

    label_password = Label(signUp, text="Password")
    label_password.grid(row=6, column=1, sticky='NSEW', padx=20)
    enter_password = Entry(signUp, width=30)
    enter_password .grid(row=7, column=1, sticky='NSEW', padx=20)

    label_password = Label(signUp, text="Password")
    label_password.grid(row=8, column=1, sticky='NSEW', padx=20)
    enter_password = Entry(signUp, width=30)
    enter_password .grid(row=9, column=1, sticky='NSEW', padx=20)

    submit_Button = Button(signUp, text="Submit", command=quit)
    submit_Button.grid(column=1, row=10, padx=20)


def quit():
    signUp.destroy()


sign_Button = Button(frame, text="Sign Up", command=sign_up)
sign_Button.grid(column=1, row=12, sticky='NSEW')


# Give all rows and columns a non-zero weight
# this helps the program to resize well
# frame.grid_columnconfigure(0, weight=1)
# frame.grid_columnconfigure(1, weight=1)
# frame.grid_columnconfigure(2, weight=1)
# frame.grid_rowconfigure(0, weight=1)
# frame.grid_rowconfigure(1, weight=1)


# THE LABEL PASSWORD BELOW ARE FOR SPACING PURPOSES
label_password = Label(frame, anchor=W)

label_password.grid(row=14, column=1, sticky='NSEW')



root.mainloop()
