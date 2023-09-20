# solar_camera

## Set up Raspberry Pi
* Install raspberry Pi OS (via Pi Imager)
* Using Raspberry Pi OS (lite 32)
* Don't forget to do advanced options to enable ssh + WiFi!!
* Expand file system

## Install Pijuice Software

* Reference Here: `https://github.com/PiSupply/PiJuice`
* Install the software *without* a GUI: `sudo apt-get install pijuice-base`
* Restart the Pi
* Run the PiJuice CLI `sudo -u pijuice python3 /usr/bin/pijuice_cli.py`

## Setup Raspi Camera

* raspi-config --> Interface Options --> Enable Legacy Camera
* Reboot
* Test via `raspistill -o FOLDER/image.jpg`


REFERENCE: https://raspberrypi-guide.github.io/other/boot-automation-pijuice
REFERENCE: (PI CAMERA): https://learn.pi-supply.com/make/pijuice-remote-camera-project/
REFERENCE: https://www.tomshardware.com/how-to/stream-live-video-raspberry-pi
REFERENCE: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/0
REFERENCE: https://picamera.readthedocs.io/en/release-1.13/recipes1.html
REFERENCE: https://raspberrypi-guide.github.io/other/boot-automation-pijuice
