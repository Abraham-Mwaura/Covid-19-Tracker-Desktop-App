print("       COVID-19 SELF-TEST  \n\n    ")
print("Please Answer The  Following Questions with yes or no\n\n\n")
ans=input("has patient been in contact with a confirmed COVID-19 patient\n")
if ans=='yes':
    e1=20
elif ans=='no':
    e1=0
else:
    print("please answer with yes or no")
  
    
ans=input("has patient traveled from a country declared as a hotspot zone\n")
if ans=='yes':
    e2=20
elif ans=='no':
    e2=0
else:
    print("please answer with yes or no")
    ans=input()
ans=input("Does patient have asthma, chronic bronchitis, pulmonary hypertension,diabetes, sickle cell anaemia, chronic liver or kidney disease?\n")
if ans=='yes':
    e3=20
elif ans=='no':
    e3=0
else:
    print("please answer with yes or no")
    ans=input()
ans=input("Is patient living in a town declared as Covid-19  hotspot zone?\n")
 
if ans=='yes':
    e4=20
elif ans=='no':
    e4=0
else:
    print("please answer with yes or no")
    ans= input()
ans=input("Has patient been vaccinated\n")
if ans=='yes':
    e5=0
elif ans=='no':
    e5=20
else:
    print("please answer with yes or no")
    ans= input()
e=e1+e2+e3+e4+e5
print("exposure percentage= ",e,"%")
 
 
 


 
 
ans=input("Does patient have a temperature higher than 38°c?\n")
if ans=='yes':
    s1=25
elif ans=='no':
    s1=0
else:
    print("please answer with yes or no")
    ans= input()
ans=input("Does patient have chest pain or pressure\n")
if ans=='yes':
    s2=25
elif ans=='no':
    s2=0
else:
    print("please answer with yes or no")
    ans= input()
ans=input("Does patient have trouble breathing?\n")
if ans=='yes':
    s3=25
elif ans=='no':
    s3=0
else:
    print("please answer with yes or no")
    ans= input()   
ans=input("Is  Patient experiencing loss of speech or movement?\n")
if ans=='yes':
    s4=25
elif ans=='no':
    s4=0
else:
    print("please answer with yes or no")
    ans= input()
s=s1+s2+s3+s4
print("severe symptoms percentage= ",s,"%")
 
 
 
 
 
 
 
ans=input("Does patient have a fever?\n")
if ans=='yes':
    m1=10
elif ans=='no':
    m1=0
else:
    print("please answer with yes or no")
    ans= input()
 
ans=input("Does patient have a dry cough?\n") 
if ans=='yes':
    m2=10
elif ans=='no':
    m2=0
else:
    print("please answer with yes or no")
    ans= input()
 
ans=input("Does patient have a running nose?\n")
if ans=='yes':
    m3=10
elif ans=='no':
    m3=0
else:
    print("please answer with yes or no")
    ans= input()
 
ans=input("Is patient experiencing loss of smell or taste?\n")
if ans=='yes':
    m4=10
elif ans=='no':
    m4=0
else:
    print("please answer with yes or no")
    ans= input()
 
ans=input("Does patient have a sore throat?\n")
if ans=='yes':
    m5=10
elif ans=='no':
    m5=0
else:
    print("please answer with yes or no")
    ans= input()
 
 
ans=input("Does patient have a headache?\n")
if ans=='yes':
    m6=10
elif ans=='no':
    m6=0
else:
    print("please answer with yes or no")
    ans= input()
 
ans=input("Is patient experiencing loss of appetite?\n")
if ans=='yes':
    m7=10
elif ans=='no':
    m7=0
else:
    print("please answer with yes or no")
    ans= input()
 
ans=input("Is patient experiencing fatigue?\n")
if ans=='yes':
    m8=10
elif ans=='no':
    m8=0
else:
    print("please answer with yes or no")
    ans= input()
 
ans=input("Does patient have diarrhea?\n")
if ans=='yes':
    m9=10
elif ans=='no':
    m9=0
else:
    print("please answer with yes or no")
    ans= input()
 
ans=input("Does patient have muscle or joint pain\n")
if ans=='yes':
    m10=10
elif ans=='no':
    m10=0
else:
    print("please answer with yes or no")
    ans= input()
 
 
m=m1+m2+m3+m4+m5+m6+m7+m8+m9+m10
print("mild symptoms% = ",m)
 
 
print ("    TEST RESULTS    \n\n")
print("Exposure%",e)
print("Severe symptoms%",s)
print("Mild symptoms%",m)
 
test_per=(e+s+m)/3
print("test percentage= ",test_per,"%","This is an approximate diagnosis. Please visit your health care provider for the accurate covid-19 test")
 
 
 
print("          RECOMMENDATIONS         ")
if(test_per==0):
 print(" you do not need to be tested for COVID-19.\n\n")
 print("stay safe by taking  precautions, such as social distancing, wearing a   mask, keeping rooms well   ventilated, avoiding crowds, cleaning your hands, and coughing into a bent elbow or tissue.\n\n")
 
if(test_per>0 and test_per<30):
 print("self-quarantine for 14 days\n. Monitor your health daily and If your symptoms get worse, call your health care provider immediately.\n\n") 
 
if(test_per>30 and test_per<50):
 print("please get tested for covid 19")
 
if (test_per>50 and test_per<80):
 print ( "covid test percentage is higher than 50%!!\n Please seek medical advice and call before going to nearest emergency department.\n\n") 
if(test_per>80):
 print ( "seek medical attention immediately!!!\n Call before going to the nearest emergency department.\n\n") 
 
 
 
if( s>50 ):
 print("you have more than 2 severe symptoms.\n Please seek medical advice as soon as possible and call before   going to nearest emergency department.\n\n") 
 
if (e>50):
 print ("High risk exposure.\n Stay safe by taking  precautions, such as social distancing, wearing a   mask, keeping rooms well   ventilated, avoiding crowds, cleaning your hands, and coughing into a bent elbow or tissue.\n") 
 
 
 




























