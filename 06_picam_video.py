# This program illustrates how to capture frames in a video stream and how to do further processing on them
# It uses numpy to do the calculations and OpenCV to display the frames

import picamera
import picamera.array                           # This needs to be imported explicitly
import time
import cv2
import numpy as np                              



# Initialize the camera
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.vflip = False                            # Flip upside down or not
camera.hflip = True                             # Flip left-right or not


# Create a data structure to store a frame
rawframe = picamera.array.PiRGBArray(camera, size=(640, 480))


# Allow the camera to warm up
time.sleep(0.1)


if __name__ == '__main__':
    try:
        
        # Continuously capture frames from the camera
        # Note that we chose the RGB format
        for frame in camera.capture_continuous(rawframe, format = 'rgb', use_video_port = True):

            # Clear the rawframe in preparation for the next frame
            rawframe.truncate(0)


            # Create a numpy array representing the image
            img_np = frame.array


            #-----------------------------------------------------
            # We will use numpy to do all our image manipulations
            #-----------------------------------------------------

            # Make a copy of the image
            img_np1 = img_np.copy()
            img_np1.setflags(write=1)                                   # Making the array mutable                                                                                                      

            # Modify the copy of the image
            # This is where you would write your code to manipulate the image (invert it, make it grayscale, etc.)
            w,h,d = img_np1.shape
            img_np1[w//4:3*w//4 , h//4:3*h//4 , :] = 255 - img_np1[w//4:3*w//4 , h//4:3*h//4 , :]


            # Show the frames
            # Note that OpenCV assumes BRG color representation, and we therefore swapped the r and b color channels
            # The waitKey command is needed to force openCV to show the image
            cv2.imshow("Orignal frame", img_np[:,:,::-1])
            cv2.imshow("Modified frame", img_np1[:,:,::-1])
            cv2.waitKey(1)




    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Program stopped by User")
        cv2.destroyAllWindows()
        # Clean up the camera resources
        camera.close()
        
