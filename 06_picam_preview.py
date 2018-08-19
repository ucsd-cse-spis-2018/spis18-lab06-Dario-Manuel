# This is a basic program to show the camera preview

import picamera
import time

# Initialize the camera
camera = picamera.PiCamera()

# This line is optional; if you need to rotate the image
camera.rotation = 180           

# Show the preview for 5 seconds
camera.start_preview()

time.sleep(5)

camera.stop_preview()

# Clean up the camera resources
camera.close()
