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
from datetime import datetime, timezone
import requests
import json

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
   logging.info('Raspberry Pi on battery power. Current level is: %d Turning off in 7min' % batterystatus['data'])


   # wait 1 minute for raspi to connect to the internet
   sleep(60)

   cloudinary.config( 
      cloud_name = os.getenv('CLOUD_NAME'), 
      api_key = os.getenv('CLOUD_API_KEY'), 
      api_secret = os.getenv('CLOUD_API_SECRET')
   )

   api = Api(os.environ['AIRTABLE_API_KEY'])
   table = api.table(os.environ['AIRTABLE_BASE_ID'], os.environ['AIRTABLE_TABLE_ID'])



   ### SET WAKEUP TIME

   current_date = str(datetime.now(timezone.utc).strftime('%Y-%m-%d'))

   params = {"lat":37.463638, "lng":-122.436707, "date": current_date}

   f = r"https://api.sunrise-sunset.org/json?"

   def sunrisesunset(f):
      a = requests.get(f, params=params)
      a = json.loads(a.text)
      a = a["results"]
      # return (a["sunrise"], a["sunset"], a["day_length"])
      return (a["sunset"])

   sunset_string = sunrisesunset(f)

   ## added an hour for daylight savings time...
   sun_hour = int(sunset_string[0:1]) + 1

   sun_minute = int(sunset_string[2:4]) - 4

   sun_second = int(sunset_string[5:7])

   alarm_time = {'second': sun_second, 'minute': sun_minute, 'hour': sun_hour, 'day': 'EVERY_DAY'}

   pj.rtcAlarm.SetAlarm(alarm_time)

   ##BENFIX---> this needs to be alarm_time (not original sunset string)
   logging.info('set alarm for ' + sunset_string )



   # TAKE PICTURES
   camera.start_preview()
   sleep(5)

   for i in range(5):

      image_name = datetime.now().strftime("%m_%d_%Y_%H:%M:%S") 

      camera.capture('/home/pi/photos/image_{}.jpg'.format(image_name))

      sleep(1)

      cloudinary.uploader.upload("/home/pi/photos/image_{}.jpg".format(image_name), 
      public_id = "image_{}".format(image_name))

      http_URL = cloudinary.CloudinaryImage("image_{}".format(image_name)).build_url()
      # add 's' to make it https
      image_URL =  http_URL[:4] + "s" + http_URL[4:]

      table.create({'Message': 'Current battery level is: %d' % batterystatus['data'], 'Image_URL': image_URL})

      sleep(59)

   camera.stop_preview()


   # Keep Raspberry Pi running
   sleep(60)

   # Make sure wakeup_enabled and wakeup_on_charge have the correct values
   pj.rtcAlarm.SetWakeupEnabled(True)
   pj.power.SetWakeUpOnCharge(0)

   alarm_time = pj.rtcAlarm.GetAlarm()['data']

   logging.info('alarm set for %d:%d:%d' % (alarm_time['hour'], alarm_time['minute'], alarm_time['second']) )

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
