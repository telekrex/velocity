#!/usr/bin/env python3


def read_distance(meters):

	# 1km  = 1,000 meters
	# 1,000 mm = 1 meter




	return ''


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