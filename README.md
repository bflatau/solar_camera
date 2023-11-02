# solar_camera

## Set up Raspberry Pi
* Install raspberry Pi OS (via Pi Imager)
* Using Raspberry Pi OS (lite 32)
* Don't forget to do advanced options to enable ssh + WiFi!!
* Expand file system

## Install Raspberry Pi Software
* sudo apt update
* sudo apt install git

## Generate SSH Key For Repo Access

* `ssh-keygen -t ed25519 -C "your_email@example.com"`
* add key to github account
* download repo

## Install Pijuice Software

* Reference Here: `https://github.com/PiSupply/PiJuice`
* Install the software *without* a GUI: `sudo apt-get install pijuice-base`
* Restart the Pi
* Run the PiJuice CLI `sudo -u pijuice python3 /usr/bin/pijuice_cli.py`

## Setup Raspi Camera

* raspi-config --> Interface Options --> Enable Legacy Camera
* Reboot
* Test via `raspistill -o FOLDER/image.jpg`
* check that picamera is installed:
    - `python -c "import picamera"`
    - `python3 -c "import picamera"`
* if there are errors, install picamera:
    - `sudo apt-get update`
    - `sudo apt-get install python-picamera python3-picamera`
* to remove picamera:
    - `sudo apt-get remove python-picamera python3-picamera`

## Setup PiJuice
* On initial setup, make sure you set up Wakeup alarm **make sure you check `Wakeup Enabled`**

## Setup Camera Script
* Create script to run at startup
* Make script executable `chmod +x /home/pi/SCRIPTNAME.py`
* Add as a startup service `sudo nano /etc/rc.local`
* Add just before the line `exit 0` --> `python3 /home/pi/scriptlocation/SCRIPTNAME.py &`
* TEST RC.LOCAL file by going to path `cd /etc/` and then running the script `sudo ./rc.local`


## Setup Cloudinary

* if pip3 isn't installed, install `sudo apt-get install python3-pip`
* `pip3 install cloudinary`
* **NOTE**: rc.local file runs as root, so figure that out better, for now do, `sudo pip3 install cloudinary`

## Setup Airtable

* `pip install pyairtable`
* **NOTE**: rc.local file runs as root, so figure that out better, for now do, `sudo pip3 install pyairtable`


## ENV FILE

* Make sure dotenv is installed , `pip3 install python-dotenv`

* CLOUD_NAME = "cloudinary_cloud_name" 
* CLOUD_API_KEY = "cloudinary_api_key" 
* CLOUD_API_SECRET = "cloudinary_api_secret"
* AIRTABLE_API_KEY = "airtable_api_key"
* AIRTABLE_BASE_ID = "airtable_base_id"
* AIRTABLE_TABLE_ID = "airtable_table_id"








REFERENCE: https://raspberrypi-guide.github.io/other/boot-automation-pijuice
REFERENCE: (PI CAMERA): https://learn.pi-supply.com/make/pijuice-remote-camera-project/
REFERENCE: https://www.tomshardware.com/how-to/stream-live-video-raspberry-pi
REFERENCE: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/0
REFERENCE: https://picamera.readthedocs.io/en/release-1.13/recipes1.html
REFERENCE: https://raspberrypi-guide.github.io/other/boot-automation-pijuice
REFERENCE: https://pimylifeup.com/raspberry-pi-syncthing/
REFERENCE: https://dev.to/matthewvielkind/using-python-and-airtable-3bb7
REFERENCE: https://dev.to/sh4yy/how-to-send-your-events-and-logs-to-discord-via-python-or-javascript-13li
REFERENCE: https://github.com/tradingstrategy-ai/python-logging-discord-handler

LTEDATA: https://www.jeffgeerling.com/blog/2022/using-4g-lte-wireless-modems-on-raspberry-pi


WORKING: https://raspberrypi.stackexchange.com/questions/78991/running-a-script-after-an-internet-connection-is-established


SUNSET: https://holypython.com/api-3-sunrise-and-sunset-data/
SUNSET: https://sunrise-sunset.org/api

PARSE LOG FILE: https://pythonic.me/2016/12/20/python-log-file-parsing/

SETUP BATTERY: https://learn.pi-supply.com/make/how-to-setup-connect-your-pijuice-battery/




