from guizero import App, Text, TextBox, Picture, PushButton, Window
import datetime

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


def displayReport(): 
    #Create the second window object
    window = Window(app, layout= "grid", title="Second window")    
    
    #Fetch the finish and start time and calculate the elapsed time between
    totalTime = stopTimer.stopDate - startTimer.startDate     
    seconds = totalTime.seconds

    #Employee section
    employee_label = Text(window, text="Employee: ", grid=[0,0], align="left", color="white")
    employeeResult_label = Text(window, text="Name", grid=[1,0], align="left", color="white")
    employeeResult_label.value = name.value #Change the value for the name of the employee

    #Workstation section
    workstationWindow_label = Text(window, text="Workstation: ", grid=[0,1], align="left", color="white")
    workstationWindowResult_label = Text(window, text="Result ", grid=[1,1], align="left", color="white")
    workstationWindowResult_label.value = workstation.value #Change the value for the name of the workstation

    #Time label
    startingTime_label = Text(window, text="Time you started working: ", grid=[0,2], align="left", color="white")
    finishingTime_label = Text(window, text="Time you finished working: ", grid=[0,3], align="left", color="white")
    timeworked_Label = Text(window, text = "Time worked: ", grid=[0,4],  align="left", color="white")
    
    #Time result
    startingTimeResult_label = Text(window, text=str(startTimer.time), grid=[1,2], align="left", color="white")
    finishingTimeResult_label = Text(window, text=str(stopTimer.time), grid=[1,3], align="left", color="white")
    timeworkedResult_Label = Text(window, text=str(seconds), grid=[1,4],  align="left", color="white")
    secondsResult_Label = Text(window, text="seconds", grid=[2,4],  align="left", color="white")

    #Photo section
    photo_label = Text(window, text="Your photo :", grid=[0,5], align="left", color="white")
    #photo = Picture(window, image="photofb.png", grid=[0,5], align="left")





#First window
#Labels
name_label = Text(app, text="Full Name", grid=[0,0], align="left", color="white")
workstationApp_label = Text(app, text="Workstation", grid=[0,1], align="left", color="white")


#Textboxes
name = TextBox(app, grid=[1,0])
workstation = TextBox(app, grid=[1,1])

#Buttons
startButton = PushButton(app, command=startTimer, text="Punch In", grid=[0,8], align="left")
finishButton = PushButton(app, command=stopTimer, text="Punch Out", grid=[1,8], align="right")
reportButton = PushButton(app, command=displayReport, text="Show report",grid=[2,8], align = "right")

#Display the gui
app.display()
