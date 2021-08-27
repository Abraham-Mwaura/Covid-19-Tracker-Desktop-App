#importing modules
import requests
import json
import bs4 as BeautifulSoup
import pandas as pd
from requests.api import get
from sqlalchemy import create_engine
import mysql.connector
from tkinter import*
import tkinter as tk

from sqlalchemy.sql.expression import label
 
#a function to extract data from a[i,convert it into a dictonary first,convert the 
# dictionary into a dataframe and enter the dataframe contents in a mysql table
def get_data():
  #using requests library to make a request from url and save the apidata object's
  #text under variable apidata
 
  apidata=requests.get("https://api.covid19api.com/summary").text
  apidata#(prints a long python string in json format)
  # if (apidata):
    #print("the api data")
   #else:
   # print("api has no data")
  apidata_info=json.loads(apidata)#loading the string into python and converting it into
  #a python dictionary
  #apidata_info
  
  ##parsing through the dictionary and extracting the info we need
#looping through the list of dictionaries and extracting the values of confirmed and deaths
 
 
  country_list=[]
  for country_info in apidata_info['Countries']:
    country_list.append([country_info['Country'],country_info['TotalConfirmed'],country_info['TotalDeaths'],country_info['Date']])
  #country_list
 
  country_list.append(["Global", apidata_info["Global"]['TotalConfirmed'],apidata_info["Global"]['TotalDeaths'],apidata_info["Global"]['Date']])
 
  country_df=pd.DataFrame(data=country_list,columns=['Country','TotalConfirmed','TotalDeaths','Date'])
  country_df.index_name="Country"
  country_df.head()
  mydb=mysql.connector.connect(
          host="localhost",
          user="root",
          password="root",
          database="users"
  )
  mycursor=mydb.cursor()
  mycursor.execute("DROP TABLE live_cases")
  mycursor.execute("CREATE TABLE live_cases(Country VARCHAR(255),TotalConfirmed VARCHAR(255),TotalDeaths VARCHAR(255),Date VARCHAR(255))")
  my_conn=create_engine("mysql+mysqldb://root:root@localhost/users") 
  country_df.to_sql(con=my_conn,name='live_cases',if_exists='append',index=False)
 
#import schedule
#from schedule import time
#schedule.every(5).minutes.do (get_data)
#while True:
 # schedule.run_pending()
 # time.sleep(60)
 

 #0.466 (x)
 #0.206 (y)
from threading import Timer
t=Timer(2.0,get_data)
t.start()
 
from tkinter import *
import mysql.connector
from tkinter import messagebox
def search():
    global myresult
    Country = e1.get()
    TotalConfirmed= e2.get()
    TotalDeaths = e3.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="users")
    mycursor=mysqldb.cursor()
 
    try:
        mycursor.execute("SELECT * FROM live_cases where Country= '" + Country + "'")
    
        myresult1 = mycursor.fetchall()
        print(myresult1)
        for x in myresult1:
            print(x)
        
        e2.delete(0, END)
        e2.insert(END, x[1])
        e3.delete(0, END)
        e3.insert(END, x[2])
 
        mycursor.execute("SELECT * FROM live_cases where Country='Kenya'")
        myresult2 = mycursor.fetchall()
        global kenyaCases,KenyaDeaths
        # for j in myresult2:
        #     print(j)
        kenyaCases=myresult2[0][1]
        KenyaDeaths=myresult2[0][2]
        print(kenyaCases)
        print(KenyaDeaths)
 
        mycursor.execute("SELECT * FROM live_cases where Country='global'")
        myresult3 = mycursor.fetchall()
        print(myresult3)
        global globalCases,globalDeaths
        # for j in myresult2:
        #     print(j)
        globalCases=myresult3[0][1]
 
        globalDeaths=myresult3[0][2]
        print(globalCases)
        print(globalDeaths)
 
        # print(myresult)
        # for x in myresult:
        #     print(x)
        
 
 
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
# root = Tk()
# root.title("Search Country's covid19 data")
# root.geometry("300x300")
 
Label(root, text="Enter The Country").place(x=10, y=10)
Button(root, text="Search", command=search,height = 1, width = 15).place(x=140, y=40)
Label(root, text="Total Confirmed Cases").place(x=10, y=80)
Label(root, text="Total Deaths").place(x=10, y=120)
 
e1 = Label(root)
e1.place(x=140, y=10)
 
e2 = Label(root)
e2.place(x=140, y=80)
 
e3 = Label(root)
e3.place(x=140, y=120)
 

 

