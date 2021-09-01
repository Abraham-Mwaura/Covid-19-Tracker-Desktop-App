#importing modules tkinter,mysql
from tkinter import*
import mysql.connector
 

root=Tk()#creating root window
root.title("user database")#root title
root.geometry("400x400")#setting a size for the window and positioning it on the screen
root.resizable(0,0)#makes the root non-resizable

#creating connection object mydb
mydb=mysql.connector.connect(#connecting to database
    host="localhost",
    user="root",
    password="root",
    database="users"
)
#myexecute("CREATE DATABASE users")cursor.
#printing database connection
#print(mydb)
#creating a cursor object
mycursor=mydb.cursor()

#declaring variables 
firstname=StringVar()
secondname=StringVar()
username=StringVar()
email=StringVar()
password=StringVar()

#mycursor.execute("CREATE DATABASE users")cursor.

#mycursor.execute("CREATE TABLE userinfo(firstname VARCHAR(30),secondname VARCHAR(30),username VARCHAR(30),email VARCHAR(30),password VARCHAR(30))")
mydb=mysql.connector.connect(
          host="localhost",
          user="root",
          password="root",
          database="users"
)
#function for adding data into database


def submit():
   #cursor object
    
        user=username.get()
        email1=email.get()
        mycursor=mydb.cursor()
    
        sql = "select username and email from userinfo where username =%s or email=%s"
        mycursor.execute(sql,[(user),(email1)])
        results = mycursor.fetchall()
        if results:
                #print("username or email is already taken")
                #label_result.config(text="Username or Email Is taken",fg='red')
                failed()
        else:
    #inserting records entered  into the database
            mycursor.execute("INSERT INTO userinfo VALUES('%s','%s','%s','%s','%s')"% (firstname.get(),secondname.get(),username.get(),email.get(),password.get()))
#committing changes made in the database
            logged()
            mydb.commit()
        


def logged():#widget to display "welcome+username" if the login credentials Are correct
    global loggedin
    loggedin= Toplevel(root)
    loggedin.title("Welcome")
    loggedin.geometry("300x300")
    Label(loggedin, text="Account Registerd successfully", fg="green", font="bold").pack()
    Label(loggedin, text="").pack()
    Button(loggedin, text="Ok", bg="grey", width=8, height=1, command=loggedin_destroy).pack()

def loggedin_destroy():#destroys the login widget after the user clicks  log out button
    loggedin.destroy()
    root.destroy()
def failed():
    global fail
    fail = Toplevel(root)
    fail.title("Error")
    fail.geometry("200x200")
    Label(fail, text="", fg="red", font="bold").pack()
    Label(fail, text="All the Required Fields are Not Filled \n\n or Username Or Email Is Already Taken").pack()
    Button(fail, text="Ok", bg="blue", width=8, height=1, command=fail_destroy).pack()

def fail_destroy():#destroys the widget after user clicks ok button
    fail.destroy()

#deleting records entered into the entry boxes after inserting them into mysql table
    firstname.delete(0,END)
    secondname.delete(0,END)
    username.delete(0,END)
    email.delete(0,END)
    password.delete(0,END)



    

   #entry boxes and their positions
firstname=Entry(root,width=30)
firstname.grid(row=0,column=1,padx=20)
secondname=Entry(root,width=30)
secondname.grid(row=1,column=1)
username=Entry(root,width=30)
username.grid(row=2,column=1)
email=Entry(root,width=30)
email.grid(row=3,column=1)
password=Entry(root,width=30)
password.grid(row=4,column=1)


#creating labels  and defining their positions
firstname_label=Label(root,text="firstname")
firstname_label.grid(row=0,column=0)
secondname_label=Label(root,text="lastname")
secondname_label.grid(row=1,column=0)
username_label=Label(root,text="username")
username_label.grid(row=2,column=0)
email_label=Label(root,text="email")
email_label.grid(row=3,column=0)
password_label=Label(root,text="password")
password_label.grid(row=4,column=0)


#creates a button (add record to database)
submit_btn=Button(root,text="Sign Up",command=submit)
submit_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


root.mainloop()#method executed to run the application