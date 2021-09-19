from threading import Timer
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pandas as pd
import requests
import json
import pyrebase
import webbrowser
import mysql.connector
from sqlalchemy import create_engine
import serial
import time
from tkinter import ttk 

from tooltip import ToolTip
#from tkinter.constants import BOTH


my_conn = create_engine("mysql+mysqldb://root:root@localhost/users")

def get_data():
    apidata = requests.get("https://api.covid19api.com/summary").text
    # loading the string into python and converting it into
    apidata_info = json.loads(apidata)

    # parsing through the dictionary and extracting the info we need
    country_list = []
    for country_info in apidata_info['Countries']:
        country_list.append([country_info['Country'], country_info['TotalConfirmed'],
                            country_info['TotalDeaths'], country_info['Date']])
    #appends the global data at the end of the database
    country_list.append(["Global", apidata_info["Global"]['TotalConfirmed'],
                        apidata_info["Global"]['TotalDeaths'], apidata_info["Global"]['Date']])

    country_df = pd.DataFrame(data=country_list, columns=[
                              'Country', 'TotalConfirmed', 'TotalDeaths', 'Date'])
    country_df.index_name = "Country"
    country_df.head()

    mycursor1 = myDb.cursor()
    mycursor1.execute("DROP TABLE live_cases")
    mycursor1.execute(
        "CREATE TABLE live_cases(Country VARCHAR(255),TotalConfirmed VARCHAR(255),TotalDeaths VARCHAR(255),Date VARCHAR(255))")

    country_df.to_sql(con=my_conn, name='live_cases',
                      if_exists='append', index=False)


myDb = mysql.connector.connect(  # connecting to database
    host="127.0.0.1",
    user="root",
    password="root",
    database="users"
)

myCursor = myDb.cursor()
#the function get_data in executed after every five minutes
t = Timer(60.0, get_data)
t.start()
# this line of code is run on the 1st instance of the code
#myCursor.execute( "CREATE DATABASE users ")
#myCursor.execute("CREATE TABLE userinfo(firstname VARCHAR(30),secondname VARCHAR(30),username VARCHAR(30),email VARCHAR(30),password VARCHAR(30))")


Config = {
    #this data is stored as a dictionary; they are the parameters for firebase connection
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
def connFirebase ():
    global db
    firebase = pyrebase.initialize_app(Config)
    print(firebase)
    db = firebase.database()

fbTimer= Timer(6.0, connFirebase)
fbTimer.start()


# create the first instance of the screen
root = Tk()
#This is the title for our app
root.title("Covid1-19 Tracker and predictions")
#App logo
root.iconbitmap("C:/Users/use/Desktop/Covid-19 Group project/logo_icon.ico")
#The initial set size for our app
#
root.geometry("1600x900")


# creating the first frame
frame = Frame(root)
#this ensures that the frame spans in the whole window
frame.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)

# mounting the image on the frame
my_img = ImageTk.PhotoImage(Image.open("logo_icon.ico"))
my_icon = Label(frame, image=my_img)
my_icon.place(rely=0.18148, relx=0.3,relheight=0.333,relwidth=0.1875)


label_haveAccount = Label(frame, text="Already have an account?", anchor=W)
label_haveAccount.place(relx=0.5, rely=0.1848 )

label_username = Label(frame, text="username", anchor=W)
label_username.place(relx=0.5199,rely=0.2644)

enter_usernamel = Entry(frame, width=30)
enter_usernamel.place(relx=0.5, rely=0.3233)


label_password = Label(frame, text="Password", anchor=W)
label_password.place(relx=0.5199, rely=0.3822)

enter_passwordl = Entry(frame, width=30)
enter_passwordl.place(relx=0.5, rely=0.4411)


def global_window():
    global globe_welcome_Label, world_label
    global icon_backHome, icon_backHome1,icon_world,icon_world1
    frame_globe = Frame(root)
    frame_globe.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)
    frame.forget()

    icon_world= Image.open(
            "C:/Users/use/Desktop/Covid-19 Group project/world.jpg")
    icon_world = icon_world.resize((1600, 900), Image.ANTIALIAS)
    icon_world1 = ImageTk.PhotoImage(icon_world)
    world_label = Label(frame_globe, image=icon_world1)
    world_label.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)
    ToolTip(widget=world_label, text="This is the world data")


    #using treeview to display the data from the data  from the database
    trv = ttk.Treeview(frame_globe, selectmode ='browse')
    vsb = ttk.Scrollbar(frame_globe, orient="vertical",command=trv.yview)
    vsb.place(relx=0.900, rely=0.1,relheight=0.856)
    trv.configure(yscrollcommand=vsb.set)

    
    trv.place(relx=0.0668,rely=0.1,relheight=0.856, relwidth=0.856)
    # number of columns
    trv["columns"] = ("1", "2", "3","4")

    # Defining heading
    trv['show'] = 'headings'

    # width of columns
    trv.column("1", width = 300) 
    trv.column("2", width = 300)
    trv.column("3", width = 300)
    trv.column("4", width = 300)
    #trv.pack(fill=BOTH,expand=1)

  
    # respective columns
    trv.heading("1", text ="Country")
    trv.heading("2", text ="TotalConfirmed")
    trv.heading("3", text ="TotalDeaths")
    trv.heading("4", text ="Date")  


    # getting data from MySQL table 
    results=my_conn.execute('''SELECT * from live_cases''')
    for dt in results: 
        trv.insert("", 'end',iid=dt[0], text=dt[0],
                values =(dt[0],dt[1],dt[2],dt[3]))



    def globalWindowQuit():
        frame_globe.place_forget()

    icon_backHome = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_globe, image=icon_backHome1,
                          relief=RAISED, command=globalWindowQuit)
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

    def HealthWindowQuit():
        frame_health.place_forget()

    icon_backHome = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_health, image=icon_backHome1,
                          relief=RAISED, command=HealthWindowQuit)
    backHome_btn.grid(row=0, column=0, pady=5)

    def measureTemp():
        serInit = serial.Serial('COM5', 9600)
        # delay 2s
        time.sleep(2)
        global tempSum
        tempSum = 0
        global countTemp
        countTemp = 0

        def ReadData():
            global i
            for i in range(5):
                # reads serial data in byte string
                byteTemp = serInit.readline()

            # convert byte code to unicode string
                UniTemp1 = byteTemp.decode()
            # removes escape characters
                global UniTemp2
                UniTemp2 = UniTemp1.rsplit()

            # Typecasts string to float
                pointTemp = float(UniTemp2[0])
                print(pointTemp)
                # arData.append(UniTemp2)
                temp_label = Label(frame_health, text=str(pointTemp))
                temp_label.grid(column=4, row=4)

                global tempSum

                tempSum += pointTemp
                time.sleep(0.5)

            serInit.close()
        # Find average temperature
        # execute function
        ReadData()

        # close serial port

        def avg(a, b):
            return a/b
        # final temperature
        finalTemp = round(avg(tempSum, 30), 1)

        avgTemp_label = Label(
            frame_health, text="Your Average temperature is " + str(finalTemp))
        avgTemp_label.grid(column=5, row=5)

        print("Your temperature is= ", finalTemp, "C")

    measureTemp_Btn = Button(
        frame_health, text="Click here to measure temperature", command=measureTemp)
    measureTemp_Btn.grid(column=3, row=3)


        "has patient been in contact with a confirmed COVID-19 patient\n"
        ans=input("has patient traveled from a country declared as a hotspot zone\n")

        ans=input("Does patient have asthma, chronic bronchitis, pulmonary hypertension,diabetes, sickle cell anaemia, chronic liver or kidney disease?\n")
        if ans=='yes':

        ans=input("Is patient living in a town declared as Covid-19  hotspot zone?\n")

        ans=input("Has patient been vaccinated\n")




        ans=input("Does patient have a temperature higher than 38°c?\n")

        ans=input("Does patient have chest pain or pressure\n")

        ans=input("Does patient have trouble breathing?\n")

        ans=input("Is  Patient experiencing loss of speech or movement?\n"

        print("severe symptoms percentage= ",s,"%")



        ans=input("Does patient have a fever?\n")

        ans=input("Does patient have a dry cough?\n") 

        ans=input("Does patient have a running nose?\n")

        ans=input("Is patient experiencing loss of smell or taste?\n")
        ans=input("Does patient have a sore throat?\n")

        ans=input("Does patient have a headache?\n"

        ans=input("Is patient experiencing loss of appetite?\n")
        ans=input("Is patient experiencing fatigue?\n")
        ans=input("Does patient have diarrhea?\n")

        ans=input("Does patient have muscle or joint pain\n")







def yourInfo_window():
    global info_welcLabel
    global icon_backHome, icon_backHome1

    frame_info = Frame(root)
    frame_info.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)
    frame.forget()

    info_welcLabel = Label(
        frame_info, text="This is the Customers Personal Information Window", font="Helvetica  25 bold", padx=100)
    info_welcLabel.grid(column=1, row=0)

    def infoWindowQuit():
        frame_info.place_forget()

    icon_backHome = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_info, image=icon_backHome1,
                          relief=RAISED, command=infoWindowQuit)
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

    def devWindowQuit():
        frame_dev.place_forget()

    icon_backHome = Image.open(
        "C:/Users/use/Desktop/Covid-19 Group project/backHome_icon.png")
    icon_backHome = icon_backHome.resize((70, 50), Image.ANTIALIAS)
    icon_backHome1 = ImageTk.PhotoImage(icon_backHome)
    backHome_btn = Button(frame_dev, image=icon_backHome1,
                          relief=RAISED, command=devWindowQuit)
    backHome_btn.grid(row=0, column=0, pady=5)


def open_url(num):
    if num == 1:
        new_link = db.child("Story1").child("link").get()
        webbrowser.open(new_link.val())
    elif num == 2:
        new_link = db.child("Story2").child("link").get()
        webbrowser.open(new_link.val())
    elif num == 3:
        new_link = db.child("Story3").child("link").get()
        webbrowser.open(new_link.val())
    elif num == 4:
        new_link = db.child("Story4").child("link").get()
        webbrowser.open(new_link.val())
    elif num == 5:
        new_link = db.child("Story5").child("link").get()
        webbrowser.open(new_link.val())
    elif num == 6:
        new_link = db.child("Story6").child("link").get()
        webbrowser.open(new_link.val())
    elif num == 7:
        new_link = db.child("Story6").child("link").get()
        webbrowser.open(new_link.val())
    elif num == 8:
        new_link = db.child("Story6").child("link").get()
        webbrowser.open(new_link.val())
    else:
        return


def home_button():
    frame1 = Frame(root)

    frame1.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)
    frame.forget()

    def logOut():

        global response
        response = messagebox.askyesno(
            "log-out window", "Do you want to log out")
        if response == 1:
            frame1.place_forget()
        else:
            pass

    def icons():
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
    icons()

    def emojis():
        # Mounting the welcome label
        global welcome_label, feel_label
        welcome_label = Label(frame1, text="Welcome",
                              font="Helvetica  25 bold", padx=100, bg="#233D72", fg="white")
                           
        welcome_label.place(rely=0.094444, relx=0.17222, relwidth=0.18,relheight=0.0370, height=16.7, width=144)
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
    emojis()

    def kenyaData():
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
        myCursor.execute("SELECT * FROM live_cases where Country='Kenya'")
        myresult2 = myCursor.fetchall()
        global kenyaCases, KenyaDeaths, kenyaDates
        # for j in myresult2:
        #     print(j)
        kenyaCases = myresult2[0][1]
        KenyaDeaths = myresult2[0][2]
        kenyaDates = myresult2[0][3]
        print(kenyaCases)
        print(KenyaDeaths)

        label_cases = Label(frame1, text="CONFIRMED CASES \n " +
                            kenyaCases, relief=GROOVE, font="Helvetica 10 bold")
        label_cases.place(relx=0.075, rely=0.586)

        label_recoveries = Label(
            frame1, text="CONFIRMED RECOVERIES \n ", relief=GROOVE, font="Helvetica 10 bold")
        label_recoveries.place(relx=0.2195, rely=0.586)

        label_deaths = Label(frame1, text="CONFIRMED DEATHS \n " +
                             KenyaDeaths, relief=GROOVE, font="Helvetica 10 bold")
        label_deaths.place(relx=0.075, rely=0.678)

        label_vaccine = Label(frame1, text="VACCINATION RATE \n" +
                              kenyaDates, relief=GROOVE, font="Helvetica 10 bold")
        label_vaccine.place(relx=0.2185, rely=0.678)

    kenyaData()

    # global icon for stats
    def GlobalData():
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

        myCursor.execute("SELECT * FROM live_cases where Country='global'")
        myresult3 = myCursor.fetchall()
        global globalCases, globalDeaths, globalDate

        globalCases = myresult3[0][1]
        globalDeaths = myresult3[0][2]
        globalDate = myresult3[0][3]
        print(globalCases)
        print(globalDeaths)

        #global stats
        global label_G_cases, label_G_recoveries, label_G_deaths, label_G_vaccine
        label_G_cases = Label(frame1, text="CONFIRMED CASES \n" +
                              globalCases, relief=GROOVE, font="Helvetica 10 bold")
        label_G_cases.place(relx=0.563, rely=0.6)

        label_G_recoveries = Label(
            frame1, text="CONFIRMED RECOVERIES \n ", relief=GROOVE, font="Helvetica 10 bold")
        label_G_recoveries.place(relx=0.697, rely=0.6)

        label_deaths = Label(frame1, text="CONFIRMED DEATHS \n" +
                             globalDeaths, relief=GROOVE, font="Helvetica 10 bold")
        label_deaths.place(relx=0.563, rely=0.688)

        label_G_vaccine = Label(frame1, text="VACCINATION RATE \n" +
                                globalDate, relief=GROOVE, font="Helvetica 10 bold")
        label_G_vaccine.place(relx=0.697, rely=0.688)

        global icon_logOut, icon_logOut1
        global logOut_btn
        icon_logOut = Image.open(
            "C:/Users/use/Desktop/Covid-19 Group project/logOut_icon.png")
        icon_logOut = icon_logOut.resize((50, 50), Image.ANTIALIAS)
        icon_logOut1 = ImageTk.PhotoImage(icon_logOut)
        logOut_btn = Button(frame1, image=icon_logOut1,
                            anchor=E, command=logOut)
        logOut_btn.place(rely=0.01111, relx=0.9475)

    GlobalData()

    def topStories():
        # Top stories
        global label_topStories,  btn_topStory1, btn_topStory2, btn_topStory3
        label_topStories = Label(frame1, text="COVID-19 TOP STORIES",
                                 font="Helvetica 15 bold", bg="#233D72", fg="white")
        label_topStories.place(relx=0.8625, rely=0.15)

        #thankGod= db.child("Story1").child("link").get()
        news_source1 = db.child("Story1").child("source").get()
        news_title1 = db.child("Story1").child("title").get()
        btn_topStory1 = Button(frame1, command=lambda: open_url(1), text=news_source1.val()+"\n" + news_title1.val(),
                               relief=GROOVE, font="Helvetica 10 bold")
        btn_topStory1.place(relx=0.8625, rely=0.2222)

        news_source2 = db.child("Story2").child("source").get()
        news_title2 = db.child("Story2").child("Title").get()
        btn_topStory2 = Button(frame1, text=news_source2.val()+"\n" + news_title2.val(),
                               relief=GROOVE, font="Helvetica 10 bold", command=lambda: open_url(2))
        btn_topStory2.place(relx=0.8625, rely=0.30556)

        news_source3 = db.child("Story3").child("source").get()
        news_title3 = db.child("Story3").child("TITE").get()
        btn_topStory3 = Button(frame1, command=lambda: open_url(3), text=news_source3.val()+"\n" + news_title3.val(),
                               relief=GROOVE, font="Helvetica 10 bold")
        # ,ipadx=10,ipady=20,relyspan=2, sticky=N
        btn_topStory3.place(relx=0.8625, rely=0.3889)

        news_source4 = db.child("Story4").child("source").get()
        news_title4 = db.child("Story4").child("Title").get()
        btn_topStory4 = Button(frame1, command=lambda: open_url(4), text=news_source4.val()+"\n" + news_title4.val(),
                               relief=GROOVE, font="Helvetica 10 bold")
        # ,ipadx=10,ipady=20,relyspan=2, sticky=N
        btn_topStory4.place(relx=0.8625, rely=0.4722)

        news_source5 = db.child("Story5").child("source").get()
        news_title5 = db.child("Story5").child("Title").get()
        btn_topStory5 = Button(frame1, command=lambda: open_url(5), text=news_source5.val()+"\n" + news_title5.val(),
                               relief=GROOVE, font="Helvetica 10 bold")
        # ,ipadx=10,ipady=20,relyspan=2, sticky=N
        btn_topStory5.place(relx=0.8625, rely=0.5556)

        news_source6 = db.child("Story6").child("source").get()
        news_title6 = db.child("Story6").child("TITLE").get()
        btn_topStory6 = Button(frame1, command=lambda: open_url(6), text=news_source6.val()+"\n" + news_title6.val(),
                               relief=GROOVE, font="Helvetica 10 bold")
        # ,ipadx=10,ipady=20,relyspan=2, sticky=N
        btn_topStory6.place(relx=0.8625, rely=0.6389)

        news_source7 = db.child("Story7").child("source").get()
        news_title7 = db.child("Story7").child("TITLE").get()
        btn_topStory7 = Button(frame1, command=lambda: open_url(7), text=news_source7.val()+"\n" + news_title7.val(),
                               relief=GROOVE, font="Helvetica 10 bold")
        # ,ipadx=10,ipady=20,relyspan=2, sticky=N
        btn_topStory7.place(relx=0.8625, rely=0.7222)

        news_source8 = db.child("Story8").child("source").get()
        news_title8 = db.child("Story8").child("TITLE").get()
        btn_topStory8 = Button(frame1, command=lambda: open_url(8), text=news_source8.val()+"\n" + news_title8.val(),
                               relief=GROOVE, font="Helvetica 10 bold")
        # ,ipadx=10,ipady=20,relyspan=2, sticky=N
        btn_topStory8.place(relx=0.8625, rely=0.8055)

    topStories()

    def search():
        try:
            myCursor.execute(
                "SELECT * FROM live_cases where Country= '" + e1.get() + "'")
            e1.delete(0, END)
            myresult1 = myCursor.fetchall()
            print(myresult1)
            global myresult, var_ConfirmedCases, var_confirmedDeaths

            Label(frame1, text="Total Confirmed Cases").place(relx=0.547, rely=0.216)
            Label(frame1, text="Total Deaths").place(relx=0.547, rely=0.266)

            var_ConfirmedCases = myresult1[0][1]
            var_confirmedDeaths = myresult1[0][2]
            global searchConDeaths, searchCases

            searchConCases_label= Label(frame1, text=var_ConfirmedCases)
            searchConCases_label.place(relx=0.687, rely=0.216)

            searchConDeaths= Label(frame1, text=var_confirmedDeaths)
            searchConDeaths.place(relx=0.687, rely=0.266)

        except Exception as e:
            print(e)
            myDb.rollback()
            myDb.close()

    global e1, country
    e1 = Entry(frame1)
    e1.place(relx=0.546, rely=0.130)
    Label(frame1, text="Enter The Country").place(relx=0.546, rely=0.089)
    #country = e1.get()

    # print(country)
    Button(frame1, text="Search", command=search,
           height=1, width=15).place(relx=0.546, rely=0.170)

    status_label = Label(frame1,
                         text="LAST UPDATED ON ", relief=GROOVE)
    status_label.place(relx=0.00001, rely=0.98, relwidth=1)


def login():
    user_ver = enter_usernamel.get()
    print(user_ver)
    pas_ver = enter_passwordl.get()
    print(pas_ver)
    sql = "select * from userinfo where username = %s and password = %s"
    test = myCursor.execute(sql, [(user_ver), (pas_ver)])
    print(test)
    results = myCursor.fetchall()
    if results:
        for i in results:
            enter_passwordl.delete(0, END)
            enter_usernamel.delete(0, END)
            print(results)
            home_button()  # if credentials are correct,the function logged is executed
            # break
    else:
        messagebox.showwarning(title="Login details",
                               message="Invalid credentials")


login_Button = Button(frame, text="Login", command=login)
login_Button.place(relx=0.51999, rely=0.500)

label_haveAccount = Label(frame, text="Don't have an account?")
label_haveAccount.place(relx=0.5, rely=0.6589)


def sign_up():

    global signUp
    signUp = Frame(root)
    signUp.place(x=0, y=0, relheight=1, relwidth=1, anchor=NW)

    def submit():
        if(enter_password1.get() == enter_password2.get()):
            # inserting records entered in the form into the database
            myCursor.execute("INSERT INTO userinfo VALUES('%s','%s','%s','%s','%s')" % (enter_firstname.get(), enter_secondname.get(), enter_username.get(),
                                                                                        enter_email.get(), enter_password2.get()))
            # committing changes made in the database
            myDb.commit()
            # deleting records entered into the entry boxes after inserting them into mysql table
            enter_firstname.delete(0, END)
            enter_secondname.delete(0, END)
            enter_username.delete(0, END)
            enter_email.delete(0, END)
            enter_password1.delete(0, END)
            enter_password2.delete(0, END)

            signUp.place_forget()
        else:
            # when the password do not match with any in the record.
            messagebox.showwarning(
                title="password", message="Password do not match")

    label_CreateAccount = Label(
        signUp, text="Create account", font="Helvetica  18 bold")
    label_CreateAccount.grid(row=1, column=1, sticky='NSEW', padx=5, pady=10)

    label_firstname = Label(signUp, text="First name")
    label_firstname.grid(row=2, column=1, sticky='NSEW', padx=5, pady=5)
    enter_firstname = Entry(signUp, width=30)
    enter_firstname .grid(row=2, column=2, sticky='NSEW', padx=5, pady=5)

    label_secondname = Label(signUp, text="Second name")
    label_secondname.grid(row=3, column=1, sticky='NSEW', padx=5, pady=5)
    enter_secondname = Entry(signUp, width=30)
    enter_secondname .grid(row=3, column=2, sticky='NSEW', padx=5, pady=5)

    label_username = Label(signUp, text="username")
    label_username.grid(row=4, column=1, sticky='NSEW', padx=5, pady=5)
    enter_username = Entry(signUp, width=30)
    enter_username .grid(row=4, column=2, sticky='NSEW',  padx=5, pady=5)

    label_email = Label(signUp, text="Email address")
    label_email.grid(row=5, column=1, sticky='NSEW', padx=5, pady=5)
    enter_email = Entry(signUp, width=30)
    enter_email .grid(row=5, column=2, sticky='NSEW ', padx=5, pady=5)

    label_password1 = Label(signUp, text="Password")
    label_password1.grid(row=6, column=1, sticky='NSEW', padx=5, pady=5)
    enter_password1 = Entry(signUp, width=30)
    enter_password1 .grid(row=6, column=2, sticky='NSEW', padx=5, pady=5)

    label_password2 = Label(signUp, text="Password")
    label_password2.grid(row=7, column=1, sticky='NSEW', padx=5, pady=5)
    enter_password2 = Entry(signUp, width=30)
    enter_password2 .grid(row=7, column=2, sticky='NSEW', padx=5, pady=5)

    submit_Button = Button(signUp, text="Submit", command=submit)
    submit_Button.grid(column=1, row=10, padx=5, pady=5, sticky=NSEW)





sign_Button = Button(frame, text="Sign Up", command=sign_up)
sign_Button.place(relx=0.5199,rely=0.6900)


root.mainloop()
