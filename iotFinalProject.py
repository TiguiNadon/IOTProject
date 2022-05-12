from guizero import App, Text, TextBox, Picture, PushButton, Window
import datetime
import threading

#Create the first window object
app = App(layout="grid", title="Work punch machine")

#Functions

#Function to start the timer when the start shift button is clicked
def startTimer():
    startTimer.startDate = datetime.datetime.now()
    startTimer.time = startTimer.startDate.strftime("%H:%M:%S")


# Function to stop the timer when the finish shift button is pressed
def stopTimer():
    stopTimer.stopDate = datetime.datetime.now()
    stopTimer.time = stopTimer.stopDate.strftime("%H:%M:%S")

def totalTimer():
    totalTimer.totalTime = stopTimer.stopDate - startTimer.startDate
    totalTimer.seconds = totalTimer.totalTime.seconds
    
    
def displayReport():
    #Create the second window object
    window = Window(app, layout= "grid", title="Second window")
    

    

    #Employee section
    employee_label = Text(window, text="Employee: ", grid=[0,0], align="left", color="black")
    employeeResult_label = Text(window, text="Name", grid=[1,0], align="left", color="black")
    employeeResult_label.value = name.value #Change the value for the name of the employee

    #Workstation section
    workstationWindow_label = Text(window, text="Workstation: ", grid=[0,1], align="left", color="black")
    workstationWindowResult_label = Text(window, text="Result ", grid=[1,1], align="left", color="black")
    workstationWindowResult_label.value = workstation.value #Change the value for the name of the workstation

    #Time label
    startingTime_label = Text(window, text="Time you started working: ", grid=[0,2], align="left", color="black")
    finishingTime_label = Text(window, text="Time you finished working: ", grid=[0,3], align="left", color="black")
    timeworked_Label = Text(window, text = "Time worked: ", grid=[0,4],  align="left", color="black")

    #Time result
    startingTimeResult_label = Text(window, text=str(startTimer.time), grid=[1,2], align="left", color="black")
    finishingTimeResult_label = Text(window, text=str(stopTimer.time), grid=[1,3], align="left", color="black")
    timeworkedResult_Label = Text(window, text=str(totalTimer.seconds), grid=[1,4],  align="left", color="black")
    secondsResult_Label = Text(window, text="seconds", grid=[2,4],  align="left", color="black")

    

def punchInWindowError():
    punchIn = Window(app, layout= "grid", title="Punch in error window")
    employee_label = Text(punchIn, text="You forgot to punch in", grid=[0,0], align="left", color="black")

#First window
#Labels
name_label = Text(app, text="Full Name", grid=[0,0], align="left", color="black")
workstationApp_label = Text(app, text="Workstation", grid=[0,1], align="left", color="black")


#Textboxes
name = TextBox(app, grid=[1,0])
workstation = TextBox(app, grid=[1,1])

#Buttons
#startButton = PushButton(app, command=startTimer, text="Punch In", grid=[0,8], align="left")
#finishButton = PushButton(app, command=stopTimer, text="Punch Out", grid=[1,8], align="right")
reportButton = PushButton(app, command=displayReport, text="Show report",grid=[2,8], align = "right")

#Display the gui
def displayApp():
    
        app.display()

import RPi.GPIO as GPIO
import time

redLedPin = 11
redBtnPin = 12

touchBtn = 37

blueLedPin = 31    # pin11 --- led
blueBtnPin = 32    # pin12 --- button

def setup():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(blueLedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.setup(blueBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.output(blueLedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to make led off
    GPIO.setup(redLedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.setup(redBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.output(redLedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to make led off
    GPIO.setup(touchBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def destroy():
    GPIO.output(blueLedPin, GPIO.HIGH)     # led off
    GPIO.output(redLedPin, GPIO.HIGH)
    GPIO.cleanup()
    
def loop():
    while True:
            if GPIO.input(touchBtn) == GPIO.LOW:
                print("Touch Button not pressed")
            else:
                if GPIO.input(blueBtnPin) == GPIO.LOW:
                    GPIO.output(blueLedPin, GPIO.LOW)
                #GPIO.output(redLedPin, GPIO.LOW)
                    startTimer()
                elif GPIO.input(blueBtnPin) == GPIO.HIGH:
                    GPIO.output(blueLedPin, GPIO.HIGH)

                if GPIO.input(redBtnPin) == GPIO.LOW:
                    GPIO.output(redLedPin, GPIO.LOW)
                    stopTimer()
                    totalTimer()
                    time.sleep(2.0)
                    destroy()
                elif GPIO.input(redBtnPin) == GPIO.HIGH:
                    GPIO.output(redLedPin, GPIO.HIGH)
                    
                


trd1 = threading.Thread(target=loop)
trd2 = threading.Thread(target=displayApp)
if __name__ == '__main__':     # Program start from here
    setup()
    try:
         trd1.start()
         trd2.start()
         
         
         
         trd2.join()
         #loop()
         #app.display()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()