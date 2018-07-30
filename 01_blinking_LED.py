# This program demonstrates how to create a blinking LED

# Import the relevant libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

# Set GPIO Pins
LedPin = 11                                     # GPIO pin for the LED

# Set GPIO direction (IN / OUT)
GPIO.setup(LedPin, GPIO.OUT)                    # Set LedPin's mode to output

# Start conditions
GPIO.output(LedPin, GPIO.LOW)                   # Set LedPin low to turn the led off 



# Main program 
if __name__ == '__main__':                      # Program starts here

    try:
        
        # This code repeats forever
        while True:

            print('LED on')
            GPIO.output(LedPin, GPIO.HIGH)      # LED on
            time.sleep(0.5)
            print('LED off')
            GPIO.output(LedPin, GPIO.LOW)  	# LED off
            time.sleep(0.5)


    # Reset by pressing CTRL + C
    except KeyboardInterrupt:              
        print("Program stopped by User")
        GPIO.output(LedPin, GPIO.LOW)          	# LED off
        GPIO.cleanup()                          # Release resource
        
