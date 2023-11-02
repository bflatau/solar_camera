import requests
import json
from time import sleep
from datetime import datetime, timezone
from pijuice import PiJuice

pj = PiJuice(1,0x14)
pjOK = False

while pjOK == False:
   stat = pj.status.GetStatus()
   if stat['error'] == 'NO_ERROR':
      pjOK = True
   else:
      sleep(0.1)


current_date = str(datetime.now(timezone.utc).strftime('%Y-%m-%d'))

params = {"lat":37.463638, "lng":-122.436707, "date": current_date}

f = r"https://api.sunrise-sunset.org/json?"

def sunrisesunset(f):
    a = requests.get(f, params=params)
    a = json.loads(a.text)
    a = a["results"]
    # return (a["sunrise"], a["sunset"], a["day_length"])
    return (a["sunset"])
    #RETURNS:  ('11:01:26 AM', '10:23:48 PM', '11:22:22')


sunset_string = sunrisesunset(f)

sun_hour = int(sunset_string[0:1]) + 1

sun_minute = int(sunset_string[2:4]) - 5

sun_second = int(sunset_string[5:7])

alarm_time = {'second': sun_second, 'minute': sun_minute, 'hour': sun_hour, 'day': 'EVERY_DAY'}

print(sunset_string)


# pj.rtcAlarm.SetAlarm(alarm_time)

# alarm_time = pj.rtcAlarm.GetAlarm()['data']
# {'data': {'second': 58, 'minute': 34, 'hour': 1, 'day': 'EVERY_DAY'}, 'error': 'NO_ERROR'}

# print('alarm set for %d:%d:%d' % (alarm_time['hour'], alarm_time['minute'], alarm_time['second']) )

