#!/usr/bin/python3

import os
import logging
from time import sleep
from pijuice import PiJuice
from picamera import PiCamera
import datetime

logging.basicConfig(
	filename = '/home/pi/pistatus.log',
	level = logging.DEBUG,
	format = '%(asctime)s %(message)s',
	datefmt = '%d/%m/%Y %H:%M:%S')


pj = PiJuice(1,0x14)
camera = PiCamera()


# Check that the Pi sees PiJuice
pjOK = False
while pjOK == False:
   stat = pj.status.GetStatus()
   if stat['error'] == 'NO_ERROR':
      pjOK = True
   else:
      sleep(0.1)

# Write statement to log
batterystatus = pj.status.GetChargeLevel()
logging.info('Waking Up, current battery level is: %d Turning off in 3min' % batterystatus['data'])


# Take 5 pictures
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/photos/image_{}.jpg'.format(datetime.datetime.now().strftime("%d_%m_%Y_%H:%M:%S")))
camera.stop_preview()


# Keep Raspberry Pi running for 3 Min (180 seconds)
sleep(180)

# Make sure wakeup_enabled and wakeup_on_charge have the correct values
pj.rtcAlarm.SetWakeupEnabled(True)

# Make sure power to the Raspberry Pi is stopped to not deplete
# the battery
pj.power.SetSystemPowerSwitch(0)
pj.power.SetPowerOff(30)

# Now turn off the system
os.system("sudo shutdown -h now")