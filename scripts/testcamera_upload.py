#!/usr/bin/python3

import os
from picamera import PiCamera
import cloudinary
import cloudinary.uploader
from pyairtable import Api
from dotenv import load_dotenv
import datetime
from time import sleep

load_dotenv()

camera = PiCamera()

cloudinary.config( 
  cloud_name = os.getenv('CLOUD_NAME'), 
  api_key = os.getenv('CLOUD_API_KEY'), 
  api_secret = os.getenv('CLOUD_API_SECRET')
)

api = Api(os.environ['AIRTABLE_API_KEY'])
table = api.table(os.environ['AIRTABLE_BASE_ID'], os.environ['AIRTABLE_TABLE_ID'])


camera.start_preview()


for i in range(5):
    sleep(4)
    image_name = datetime.datetime.now().strftime("%m_%d_%Y_%H:%M:%S") 

    camera.capture('/home/pi/photos/image_{}.jpg'.format(image_name))
    sleep(1)

    cloudinary.uploader.upload("../../photos/image_{}.jpg".format(image_name), 
    public_id = "image_{}".format(image_name))

    image_URL = cloudinary.CloudinaryImage("image_{}".format(image_name)).build_url()

    table.create({'Message': 'battery info goes here', 'Image_URL': image_URL})

camera.stop_preview()