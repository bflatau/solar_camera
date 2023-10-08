#!/usr/bin/python3

import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()


cloudinary.config( 
  cloud_name = os.getenv('CLOUD_NAME'), 
  api_key = os.getenv('CLOUD_API_KEY'), 
  api_secret = os.getenv('CLOUD_API_SECRET')
)

cloudinary.uploader.upload("../../photos/test.jpg", 
  public_id = "test_image")

# print(cloudinary.CloudinaryImage("test_image.jpg").build_url())
# http://res.cloudinary.com/dubqxoatm/image/upload/test_image.jpg