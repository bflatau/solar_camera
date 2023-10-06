#!/usr/bin/python3

import os
from pyairtable import Api
from dotenv import load_dotenv

load_dotenv()


api = Api(os.environ['AIRTABLE_API_KEY'])
table = api.table(os.environ['AIRTABLE_BASE_ID'], os.environ['AIRTABLE_TABLE_ID'])

table.create({'Message': 'testing', 'Image_URL': 'blah'})

# result = table.all()

# print(result)