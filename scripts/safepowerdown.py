 #!/usr/bin/python3

import os
from pijuice import PiJuice

pj = PiJuice(1,0x14)
pj.power.SetWakeUpOnCharge(0)

   # Make sure power to the Raspberry Pi is stopped to not deplete
   # the battery
pj.power.SetSystemPowerSwitch(0)
pj.power.SetPowerOff(30)

# Now turn off the system
os.system("sudo shutdown -h now")