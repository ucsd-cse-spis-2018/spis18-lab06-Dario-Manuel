# This program demonstrates a more flexible way to implement a delay

# Import the relevant libraries
import time

# Specify how long we want to wait (in seconds)
delayTarget = 1


# Keep track of the time
LastTime = 0

# Main program 
if __name__ == '__main__':

    try:
        
        # This code repeats forever
        while True:

            # Check the current time
            currentTime = time.time()

            # Check if we have waited long enough
            if (currentTime - LastTime > delayTarget):
                print("Amount of time that has passed: {0}".format(currentTime-LastTime))
                LastTime = currentTime
           

            
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Program stopped by User")
