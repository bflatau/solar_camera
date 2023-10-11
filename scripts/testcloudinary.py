#!/usr/bin/python3

import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
import json
from dotenv import load_dotenv

load_dotenv()


cloudinary.config( 
  cloud_name = os.getenv('CLOUD_NAME'), 
  api_key = os.getenv('CLOUD_API_KEY'), 
  api_secret = os.getenv('CLOUD_API_SECRET')
)

# cloudinary.uploader.upload("../../photos/test.jpg", 
#   public_id = "test_image")

# print(cloudinary.CloudinaryImage("test_image").build_url())

json_response = cloudinary.api.resource("test_image")
json_text = json.dumps(json_response)
json_dict = json.loads(json_text)

# print(type(json_dict))

print(cloudinary.CloudinaryImage("test_image").build_url())
print(cloudinary.CloudinaryImage("test_image").image())

print(json_dict['secure_url'])
# http://res.cloudinary.com/dubqxoatm/image/upload/test_image.jpg



test_url = "http://res.cloudinary.com/dubqxoatm/image/upload/test_image"
test_url_https = test_url[:4] + "s" + test_url[4:]
print(test_url_https)