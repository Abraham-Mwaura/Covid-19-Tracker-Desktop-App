from tkinter import *
from tkinter import messagebox 
from tkinter.font import BOLD
root = Tk()

t1=IntVar()
t2=IntVar()
t3=IntVar()
t4=IntVar()
t5=IntVar()
t6=IntVar()
t7=IntVar()
t8=IntVar()
t9=IntVar()
t10=IntVar()
t11=IntVar()
t12=IntVar()
t13=IntVar()
t14=IntVar()
t15=IntVar()
t16=IntVar()
t17=IntVar()
t18= IntVar()
text1=''
text2=''

def exposureRate():
    global predict1
    predict1 = t1.get()+t2.get()+t3.get()+t4.get()+t18.get()
    #+t5.get()+t6.get()+t7.get()+t8.get()
    Label(root,text="Your exposure rate is :"+str(predict1)+"%"+"\n", fg="#2E8BC0",font="helvetica 15 bold", ).grid(row=9,column=1)
exposureRate()

Label(root,text='Have you been in contact with a confirmed COVID-19 patient?',font=0.1).grid(row=4,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='Yes', variable=t1,value=20,command=exposureRate,font=0.1).grid(row=4,column=2)
Radiobutton(root, text='No', variable=t1,value=0.00,command=exposureRate,font=0.1).grid(row=4, column=3)

Label(root,text="Have you  traveled from a country declared as a hotspot zone?",font=0.1).grid(row=5,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='Yes', variable=t2,value=20,command=exposureRate,font=0.1).grid(row=5,column=2)
Radiobutton(root, text='No', variable=t2,value=0.00,command=exposureRate,font=0.1).grid(row=5, column=3)

Label(root,text="Do have asthma, chronic bronchitis, pulmonary hypertension,diabetes,\n sickle cell anaemia, chronic liver or kidney disease?",font=0.1).grid(row=6,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='Yes', variable=t3,value=20,command=exposureRate,font=0.1).grid(row=6,column=2)
Radiobutton(root, text='No', variable=t3,value=0.00,command=exposureRate,font=0.1).grid(row=6, column=3)


Label(root,text='Are you living in a town declared as Covid-19  hotspot zone?',font=0.1).grid(row=7,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t4,value=20,command=exposureRate,font=0.1).grid(row=7,column=2)
Radiobutton(root, text='No', variable=t4,value=0.00,command=exposureRate,font=0.1).grid(row=7, column=3)

Label(root,text='Have you been vaccinated?',font=0.1).grid(row=8,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='Yes', variable=t18,value=0.00,command=exposureRate,font=0.1).grid(row=8,column=2)
Radiobutton(root, text='No', variable=t18,value=20,command=exposureRate,font=0.1).grid(row=8, column=3)




def symptomsPercent():
    global predict2
    predict2 = t5.get()+t6.get()+t7.get()+t8.get()
    Label(root,text="Your severe symptoms percentage rate is :"+str(predict2)+"\n",fg="#2E8BC0",font="helvetica 15 bold",).grid(row=14,column=1)
symptomsPercent()

Label(root,text='Does patient have a temperature higher than 38°c?',font=0.1).grid(row=10,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t5,value=25,command=symptomsPercent,font=0.1).grid(row=10,column=2)
Radiobutton(root, text='No', variable=t5,value=0.00,command=symptomsPercent,font=0.1).grid(row=10, column=3)

Label(root,text='Does patient have chest pain or pressure',font=0.1).grid(row=11,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t6,value=25,command=symptomsPercent,font=0.1).grid(row=11,column=2)
Radiobutton(root, text='No', variable=t6,value=0.00,command=symptomsPercent,font=0.1).grid(row=11, column=3)


Label(root,text='Does patient have trouble breathing').grid(row=12,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t7,value=25,command=symptomsPercent,font=0.1).grid(row=12,column=2)
Radiobutton(root, text='No', variable=t7,value=0.00,command=symptomsPercent,font=0.1).grid(row=12, column=3)

Label(root,text='Is  Patient experiencing loss of speech or movement?',font=0.1).grid(row=13,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t8,value=25,command=symptomsPercent,font=0.1).grid(row=13,column=2)
Radiobutton(root, text='No', variable=t8,value=0.00,command=symptomsPercent,font=0.1).grid(row=13, column=3)


def mildSymptoms():
    global predict3
    predict3 = t9.get()+t10.get()+t11.get()+t12.get()+t13.get()+t14.get()+t15.get()+t16.get()+t17.get()
    Label(root,text="mild symptoms%:"+str(predict3)+"\n",fg="#2E8BC0",font="helvetica 15 bold",).grid(row=24,column=1)
mildSymptoms()

Label(root,text="Does patient have a fever?",anchor=W,font=0.1).grid(row=15,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t9,value=10,command=mildSymptoms,font=0.1).grid(row=15,column=2)
Radiobutton(root, text='No', variable=t9,value=0.00,command=mildSymptoms,font=0.1).grid(row=15, column=3)

Label(root,text='Does patient have a dry cough?',font=0.1).grid(row=16,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t10,value=10,command=mildSymptoms,font=0.1).grid(row=16,column=2)
Radiobutton(root, text='No', variable=t10,value=0.00,command=mildSymptoms,font=0.1).grid(row=16, column=3)


Label(root,text='Does patient have a running nose?',font=0.1).grid(row=17,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t11,value=10,command=mildSymptoms,font=0.1).grid(row=17,column=2)
Radiobutton(root, text='No', variable=t11,value=0.00,command=mildSymptoms,font=0.1).grid(row=17, column=3)

Label(root,text='Is patient experiencing loss of smell or taste?',font=0.1).grid(row=18,column=1,sticky=W,padx=20,pady=2.5 )
Radiobutton(root, text='yes', variable=t12,value=10,command=mildSymptoms,font=0.1).grid(row=18,column=2)
Radiobutton(root, text='No', variable=t12,value=0.00,command=mildSymptoms,font=0.1).grid(row=18, column=3)

Label(root,text="Does patient have a sore throat?",font=0.1).grid(row=19,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t13,value=10,command=mildSymptoms,font=0.1).grid(row=19,column=2)
Radiobutton(root, text='No', variable=t13,value=0.00,command=mildSymptoms,font=0.1).grid(row=19, column=3)

Label(root,text='Is patient experiencing loss of appetite?',font=0.1).grid(row=20,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t14,value=10,command=mildSymptoms,font=0.1).grid(row=20,column=2)
Radiobutton(root, text='No', variable=t14,value=0.00,command=mildSymptoms,font=0.1).grid(row=20, column=3)

Label(root,text='Is patient experiencing fatigue?',font=0.1).grid(row=21,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t15,value=10,command=mildSymptoms,font=0.1).grid(row=21,column=2)
Radiobutton(root, text='No', variable=t15,value=0.00,command=mildSymptoms,font=0.1).grid(row=21, column=3)

Label(root,text='Does patient have diarrhea?',font=0.1).grid(row=22,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t16,value=10,command=mildSymptoms,font=0.1).grid(row=22,column=2)
Radiobutton(root, text='No', variable=t16,value=0.00,command=mildSymptoms,font=0.1).grid(row=22, column=3)

Label(root,text='Does patient have muscle or joint pain',font=0.1).grid(row=23,column=1,sticky=W,padx=20,pady=2.5)
Radiobutton(root, text='yes', variable=t17,value=10,command=mildSymptoms,font=0.1).grid(row=23,column=2)
Radiobutton(root, text='No', variable=t17,value=0.00,command=mildSymptoms,font=0.1).grid(row=23, column=3)

def recommendations():
    global text2, text1

    top = Toplevel()
    top.geometry("400x200")
    top.title("RECOMMENDATIONS")

    test_percentage=(predict1+predict2+predict3)/3
    #Label(top,text='Your test Percentage is '+ str(test_percentage) ).grid(row=25,column=1)
    #messagebox.showinfo("RECCOMMENDATIONS",text+text1 )

#Label(root,text='RECCOMMENDATIONS ').grid(row=26,column=1)
    if(test_percentage==0):
        text1='''You do not need to be tested for COVID-19.stay
            safe by taking  precautions,
            such as social distancing, wearing a  
            mask, keeping rooms well   ventilated, 
            avoiding crowds, 
            cleaning your hands, and coughing into 
            a bent elbow or tissue. '''

    if(test_percentage>0 and test_percentage<30):
        text1='''self-quarantine for 14 days\n.
            Monitor your health daily and If your symptoms get worse, 
            call your health care provider immediately.'''

    if(test_percentage>30 and test_percentage<50):
        text1='"please get tested for covid 19"' 

    if (test_percentage>50 and test_percentage<80):
        text1='''covid test percentage is higher than 50%!!\n 
        Please seek medical advice and call before going
        to nearest emergency department.'+ test_percentage'''

    if(test_percentage>80):
        text1= '''seek medical attention immediately!!!\n 
        Call before going to the nearest emergency department.\n\n'''

    #e is the exposure pecentage, predict 1

    # s is the severe sypmptoms percentage predict 2
    if( predict1>50 ):
        text2="you have more than 2 severe symptoms.\n Please seek medical advice as soon as possible and call before   going to nearest emergency department.\n\n" 
    if (predict2>50):
        text2='"High risk exposure.\n Stay safe by taking  precautions, such as social distancing, wearing a   mask, keeping rooms well   ventilated, avoiding crowds, cleaning your hands, and coughing into a bent elbow or tissue.\n"'



    l2 = Label(top, text = text1 +"\n" + text2 ,font=10,fg="#2E8BC0" )
    l2.pack()

Button(root,text="show Recommendations",command=recommendations).grid(row=34,column=1)

mainloop()