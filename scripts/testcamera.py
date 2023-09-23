from picamera import PiCamera
import datetime
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/photos/image_{}.jpg'.format(datetime.datetime.now().strftime("%m_%d_%Y_%H:%M:%S")))
camera.stop_preview()