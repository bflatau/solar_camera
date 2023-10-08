from pijuice import PiJuice


pj = PiJuice(1,0x14)

batterystatus = pj.status.GetChargeLevel()

print('Battery Status is: %d' % batterystatus['data'])

# print(pj.status.GetChargeLevel())