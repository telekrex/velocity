#!/usr/bin/env python3


class Battery:

	# Battery represents a battery
	# with basic specifications
	# for formulas

	def __init__(self, volts, amphours):
		self.volts = volts
		self.amphours = amphours
		self.watthours = volts * amphours

		# to do:
		# chemical and material types affecting weight and capacity


class CustomBattery:

	# Custom Battery represents a battery
	# that's initialized by combining cells
	# in the case that you're desiging your
	# own battery

	def __init__(self, cells, wiring = 'ser', volts, amphours):
		self.cells = cells
		self.wiring = wiring
		self.volts = volts if wiring == 'par' else volts * cells
		self.amphours = amphours if wiring == 'ser' else amphours * cells
		self.watthours = self.volts * self.amphours