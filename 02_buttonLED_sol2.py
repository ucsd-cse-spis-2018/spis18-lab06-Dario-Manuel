# This program demonstrates how to read a button
# It will use this information to control an LED

# Import the relevant libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

# Set GPIO Pins
LedPin = 11                                     # GPIO pin for the LED
BtnPin = 15                                     # GPIO pin for the button

# Set GPIO direction (IN / OUT)
GPIO.setup(LedPin, GPIO.OUT)                            # Set LedPin's mode to output
GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Set BtnPin's mode is input, and pull up to high level (3.3V)

# Start conditions
GPIO.output(LedPin, GPIO.LOW)                   # Set LedPin low to turn the led off 
isOn = False

def switch(offOn):
    if offOn == True:
        GPIO.output(LedPin, GPIO.LOW)
    else:
        GPIO.output(LedPin, GPIO.HIGH)
    return (not offOn)


# Main program 
if __name__ == '__main__':                      # Program starts here

    try:

        # This code repeats forever
        while True:
                
            button = GPIO.input(BtnPin)
            
            if button == 0:
                isOn = switch(isOn)
                time.sleep(.5)



    # Reset by pressing CTRL + C
    except KeyboardInterrupt:              
        print("Program stopped by User")
        GPIO.output(LedPin, GPIO.LOW)          	# LED off
        GPIO.cleanup()                          # Release resource

