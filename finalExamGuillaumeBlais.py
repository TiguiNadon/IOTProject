from guizero import App, Text, TextBox, Picture, PushButton, Window
import RPi.GPIO as GPIO
app = App(layout="grid", title="Final Exam Guillaume Blais")
import threading



redLedPin = 37
redBtnPin = 38

yellowLedPin = 40
orangeLedPin = 35

greenLedPin = 22    # pin11 --- led
blueBtnPin = 32    # pin12 --- button
    
def setup():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(greenLedPin, GPIO.OUT)   # Set LedPin's mode is output,
    GPIO.setup(orangeLedPin, GPIO.OUT)
    GPIO.setup(yellowLedPin, GPIO.OUT)
    GPIO.setup(blueBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
 # Set LedPin high(+3.3V) to make led off
    GPIO.setup(redLedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.setup(redBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.output(redLedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to make led off
    
def winner():


    while True:
                GPIO.output(greenLedPin, GPIO.HIGH)
                GPIO.output(redLedPin, GPIO.HIGH)

                if GPIO.input(blueBtnPin) == GPIO.LOW:
                    GPIO.output(yellowLedPin, GPIO.LOW)
                #GPIO.output(redLedPin, GPIO.LOW)
                #print("Blue button not pressed")
                elif GPIO.input(blueBtnPin) == GPIO.HIGH:
                    GPIO.output(yellowLedPin, GPIO.HIGH)
                #print("Blue button  pressed")

                if GPIO.input(redBtnPin) == GPIO.LOW:
                    GPIO.output(orangeLedPin, GPIO.LOW)
                    

                    print("")
                elif GPIO.input(redBtnPin) == GPIO.HIGH:
                    GPIO.output(orangeLedPin, GPIO.HIGH)
                    print("")

def yankeesAnswer():
                GPIO.output(greenLedPin, GPIO.LOW)
                print("Wrong Answer")
                
def metsAnswer():
                GPIO.output(redLedPin, GPIO.LOW)
                print("Wrong Answer")

def soxAnswer():
                GPIO.output(redLedPin, GPIO.LOW)
                print("Wrong Answer")

def jaysAnswer():
                GPIO.output(redLedPin, GPIO.LOW)
                

#For the first screen 
spacer = Text(app, text="                      ", grid=[0,3], align="right", color="black")
name1_label = Text(app, text="John", grid=[1,3], align="right", color="black")
spacer = Text(app, text="                     ", grid=[2,3], align="right", color="black")
name3_label = Text(app, text="Paul", grid=[3 ,3], align="right", color="black")

question1 = Text(app, text="Who is the best baseball team", grid=[2 ,4], align="right", color="black")
yankeeButton = PushButton(app, command=yankeesAnswer,text="Yankees",grid=[1,5], align = "right")
metsButton = PushButton(app, command=metsAnswer, text="Mets",grid=[1,6], align = "right")
soxButton = PushButton(app, command=soxAnswer, text="Red Sox",grid=[1,7], align = "right")
jaysButton = PushButton(app,command=jaysAnswer, text="Blue Jays",grid=[1,8], align = "right")


#Display the gui
def displayApp():
    
        app.display()

trd1 = threading.Thread(target=winner)
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
