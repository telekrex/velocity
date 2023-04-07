#!/usr/bin/env python3





def read_distance(meters):

	# 1km  = 1,000 meters
	# 1,000 mm = 1 meter




	return ''






def read_amps(amps):

	return f'{amps } amps'





def read_voltage(volts):

	# 1 kV = 1,000 Volts

	if volts < 1000:
		# if less than 1 kV,
		# return just the volts
		return f'{volts} Volts'

	# if equal or over 1 kV,
	# return that, in kV scale
	return f'{volts/1000} kV'


def read_watts(watts):

	# 1,000 mW = 1 Watt
	# 1 kW = 1,000 Watts

	if watts < 1:
		# if less than 1 Watt,
		# return value in mW
		return f'{watts*1000} mW'

	if watts > 1000:
		# if more than 1000 Watts,
		# return value in kW
		return f'{watts/1000} kW'




def solve_for_volts(watts, amps):
	return watts / amps


def solve_for_amps(watts, volts):
	return watts / volts


def solve_for_watts(amps, volts):
	return amps * volts






def read_battery(battery):
	return f'{read_voltage(battery.volts)}, {read_amps(battery.amps)}'


def solve_for_battery(cells, volts, amps, wiring):

	if wiring == 'ser':
		# multiply volts by cells
		return cells * volts, amps

	if wiring == 'par':
		# multiply amps by cells
		return volts, cells * amps



class Battery:

	def __init__(self, cells, wiring, volts, amps):
		self.cells = cells
		self.wiring = wiring
		self.volts = volts if wiring == 'par' else volts * cells
		self.amps = amps if wiring == 'ser' else amps * cells




# test
x = Battery(8, 'ser', 3.5, .5)
print(read_battery(x))













#