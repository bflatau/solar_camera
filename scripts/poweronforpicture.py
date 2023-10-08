#!/usr/bin/python3

import os
import logging
from time import sleep
from pijuice import PiJuice
from picamera import PiCamera
import cloudinary
import cloudinary.uploader
from pyairtable import Api
from dotenv import load_dotenv
import datetime

load_dotenv()

logging.basicConfig(
	filename = '/home/pi/pistatus.log',
	level = logging.DEBUG,
	format = '%(asctime)s %(message)s',
	datefmt = '%m/%d/%Y %H:%M:%S')

pj = PiJuice(1,0x14)
camera = PiCamera()

pjOK = False
while pjOK == False:
   stat = pj.status.GetStatus()
   if stat['error'] == 'NO_ERROR':
      pjOK = True
   else:
      sleep(0.1)

batterystatus = pj.status.GetChargeLevel()

# If on battery power, shut down after 3min
data = stat['data']
if data['powerInput'] == "NOT_PRESENT" and data['powerInput5vIo'] == 'NOT_PRESENT':

   # Write statement to log
   logging.info('Raspberry Pi on battery power. Current level is: %d Turning off in 3min' % batterystatus['data'])


   # wait 1 minute for raspi to connect to the internet
   sleep(60)

   cloudinary.config( 
      cloud_name = os.getenv('CLOUD_NAME'), 
      api_key = os.getenv('CLOUD_API_KEY'), 
      api_secret = os.getenv('CLOUD_API_SECRET')
   )

   api = Api(os.environ['AIRTABLE_API_KEY'])
   table = api.table(os.environ['AIRTABLE_BASE_ID'], os.environ['AIRTABLE_TABLE_ID'])

   # Take 5 pictures
   camera.start_preview()

   for i in range(5):

      sleep(5)
      image_name = datetime.datetime.now().strftime("%m_%d_%Y_%H:%M:%S") 

      camera.capture('/home/pi/photos/image_{}.jpg'.format(image_name))
      sleep(1)

      cloudinary.uploader.upload("/home/pi/photos/image_{}.jpg".format(image_name), 
      public_id = "image_{}".format(image_name))

      image_URL = cloudinary.CloudinaryImage("image_{}".format(image_name)).build_url()

      table.create({'Message': 'Current battery level is: %d' % batterystatus['data'], 'Image_URL': image_URL})

   camera.stop_preview()


   # Keep Raspberry Pi running
   sleep(180)

   # Make sure wakeup_enabled and wakeup_on_charge have the correct values
   pj.rtcAlarm.SetWakeupEnabled(True)
   pj.power.SetWakeUpOnCharge(0)

   # Make sure power to the Raspberry Pi is stopped to not deplete
   # the battery

   pj.power.SetSystemPowerSwitch(0)
   pj.power.SetPowerOff(30)

   # Now turn off the system
   logging.info('turning off')

   # BENDO: do this at the start, so that it shuts down in X min (if script fails due to no internet???)
   os.system("sudo shutdown -h now")

else:

# 	# Write statement to log
	logging.info('Raspberry Pi on mains power, not turned off automatically')
