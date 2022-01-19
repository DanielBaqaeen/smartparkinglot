from picamera import PiCamera
import time
camera = PiCamera()
#camera.start_preview()
file_name = "img_" + str(time.time()) + ".jpg"
camera.capture(file_name)
print("Done.")
