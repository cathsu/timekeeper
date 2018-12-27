#import time
import datetime

def printTime(timedeltaObj):
    
    #retrieve the hours, minutes, seconds of timedelta object
    days = timedeltaObj.days
    hours = days*24 + timedeltaObj.seconds//3600
    remainingTime = timedeltaObj.seconds % 3600
    minutes = remainingTime // 60
    remainingTime = remainingTime % 60
    seconds = remainingTime
    print("%i hours %i "
              "minutes %i seconds" %(hours, minutes, seconds), end=' ')

name= input("Who is clocking in? ")
print("Press ENTER when you clock in, ENTER again when you "
      "clock out, and Ctrl-C to quit")
input() #press Enter when you want to clock in
startTime = datetime.datetime.now().replace(microsecond=0) #get the start time when user clocks in
lastTime = startTime
totalTime = startTime
lapNum = 1

#Start tracking the lap times
try:
    while True: 
        input() # press Enter when you want to clock out
                # and start a new lap 

        #get the current time 
        currentTime = datetime.datetime.now().replace(microsecond=0)

        #calculate how long the lap took by subtracting start
        #   time of lap (lastTime) from current time 
        lapTime = currentTime - lastTime 

        print("Lap #%i" %lapNum, end=' ')
        printTime(lapTime)
        
        #calculate total time elapsed since starting the stopwatch
        #   by subtracting overall start time of stopwatch (startTime)
        #   from current time 
        totalTime = currentTime - startTime

        print("Total time: ", end=' ')
        printTime(totalTime)

        #increment lapNum by 1
        lapNum += 1 
        
        #reset the last lap time
        lastTime = currentTime
    

except KeyboardInterrupt:

    #print total time
    print("%s, you've worked a total of" %name, end=' ')
    printTime(totalTime)
    
    #Handle the Ctrl-C exception to keep its error message from displaying
    print('\nDone.')
