# import tkinter as tk
from tkinter import *
from tkinter import  ttk
from tkinter.constants import BOTH
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:root@localhost/users")  


def viewall():
    # Creating tkinter root
    root = Tk()
    root.geometry("1600x900") 
    root.title("global data")  
    # Using treeview widget
    trv = ttk.Treeview(root, selectmode ='browse')
    vsb = ttk.Scrollbar(orient="vertical",command=trv.yview)
    vsb.place(x=1550, y=0, height=870)
    trv.configure(yscrollcommand=vsb.set)

    #30+1160+2
    trv.grid(row=1,column=1,padx=20,pady=20)
    # number of columns
    trv["columns"] = ("1", "2", "3","4")

    # Defining heading
    trv['show'] = 'headings'

    # width of columns
    trv.column("1", width = 150)
    trv.column("2", width = 150)
    trv.column("3", width = 150)
    trv.column("4", width = 150)
    trv.pack(fill=BOTH,expand=1)


    # Headings  
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


    root.mainloop()
viewall()