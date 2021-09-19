import serial
import time
def measureTemp():
        serInit = serial.Serial('COM5', 9600)
        # delay 2s
        time.sleep(2)
        global tempSum
        tempSum = 0
        global countTemp
        countTemp= 0
        def ReadData():
            global i
            
            #for i in range(30):
            
            def range_temp():
                global countTemp
                
                if countTemp== 30: return
                # reads serial data in byte string
                else: 
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
                    # temp_label=Label(frame_health, text=str(pointTemp))
                    # temp_label.grid(column=4, row=4)

                    global tempSum

                    tempSum += pointTemp
                    countTemp+=1
                    time.sleep(0.5)
                    return range_temp
                    #frame_health.after(0.5, range_temp)
                
            range_temp()
            serInit.close()
        # Find average temperature
        # execute function
        ReadData()

        # close serial port
        
        
        def avg(a, b):
            return a/b 
        # final temperature
        finalTemp = round(avg(tempSum, 30), 1)

        # avgTemp_label = Label(
        #     frame_health, text="Your Average temperature is "+ str(finalTemp) )
        # avgTemp_label.grid(column=5, row=5)