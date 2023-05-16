# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 12:57:12 2020

@author: Grace Choo
"""

"""
Automate Mouse movement every X minutes for how many hours you want.

Note: Use Spyder to run this instead of jupyter notebook
      While running the code, make sure that there is a blank excel spreadsheet at the background.
      This is so that you are able to see the mouse moves and clicks, which indicates the code is running.
      Modules you will need to install prior are pyautogui, time, datetime
"""

##################
#    Settings    #
##################
NumHour = 3  #specify the number of hours you want this code to run.
NumMinutes = 1  #specify the number of minutes to rest before you want the mouse to move again. (5 minutes is a good choice. Do not select more than 9 minutes or your pc might lock you out.)

######################
#    Settings End    #
######################
import pyautogui
import time
import datetime
import sys

#sys.stdout = open("test.txt", "w")
currentDT = datetime.datetime.now()
print ("Mouse starts moving at " + currentDT.strftime("%I:%M:%S %p"))
time.sleep(5) #rest for 5 seconds for setting up

# this code moves the mouse in a PERFECT square clockwise every [NumMinutes] minutes for [NumHour] hours

for i in range(int(NumHour*60/NumMinutes)+1):
    try:
        pyautogui.FAILSAFE = False # disable failsafe feature. dont need it.
        pyautogui.moveTo(600, 510) # This is the mouse cursor starting position in relation to your screen.
        pyautogui.moveRel(100, 0, duration=0.25) # mouse cursor moves right (x axis) in 0.25 seconds (duration is needed otherwise the cursor just teleborted from point A to point B)
        pyautogui.click() # mouse clicks
        pyautogui.moveRel(0, 100, duration=0.25) # mouse cursor moves down (y axis)
        pyautogui.click() # mouse clicks
        pyautogui.moveRel(-100, 0, duration=0.25) # mouse cursor moves left (x axis)
        pyautogui.click() # mouse clicks
        pyautogui.moveRel(0, -100, duration=0.25) # mouse cursor moves up (y axis)
        pyautogui.click() # mouse clicks
        i+=1
        print("Mouse Moved "+str(i)+" times.")  # to track how many times the mouse has moved
        time.sleep(NumMinutes*60)     # specify the number of seconds to rest before going to the begining of the loop.
    except (KeyboardInterrupt):
        currentDT = datetime.datetime.now()
        print("Keyboard Interruption detected. Break the loop. Loops stops at " + currentDT.strftime("%I:%M:%S %p"))
        #sys.stdout.close()
        break
    
    except:
        currentDT = datetime.datetime.now()
        print("Error Detected. Continue with the loop. The time now is " + currentDT.strftime("%I:%M:%S %p"))

currentDT = datetime.datetime.now()
print("Mouse Move End. The time now is " + currentDT.strftime("%I:%M:%S %p"))
#sys.stdout.close()
#Code Ends Here


################################
#    Other Additional Stuff    #
################################

#To see what is the location of mouse cursor
pyautogui.position()

#To see what is your screen size
pyautogui.size()



#delete all variables
%reset
cls    #clear console

