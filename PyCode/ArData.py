import serial
import time
import math
#initialize serial port
#com6->Port where arduino is connected
#9600->byte reading rate from serial 
serInit= serial.Serial('COM6',9600)

#delay 2s
time.sleep(2)
tempSum=0
def ReadData():
    for i in range (30):
    #reads serial data in byte string
        byteTemp= serInit.readline()

#convert byte code to unicode string
        UniTemp1= byteTemp.decode()
#removes escape characters
        global UniTemp2
        UniTemp2= UniTemp1.rsplit()

#Typecasts string to float
        pointTemp= float(UniTemp2[0])
        print(pointTemp)
        #arData.append(UniTemp2)
        global tempSum
        
        tempSum+= pointTemp

        time.sleep(0.5)
#Find average temperature
def avg(a,b):
    return a/b

#execute function
ReadData()

#close serial port
serInit.close()

#final temperature
finalTemp= round(avg(tempSum,30),1)

#write to file
F_Out= open("FinalData.txt", "w+")
F_Out.write(str(finalTemp))
F_Out.close()
print("Your temperature is= ", finalTemp, "C")
print("Autoclose in: ")
for i in range(1,10):
    print(10-i)
    time.sleep(1)