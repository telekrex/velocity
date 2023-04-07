#!/usr/bin/env python3


class Battery:

	def __init__(self, cells, wiring = 'ser', volts, amps):
		self.cells = cells
		self.wiring = wiring
		self.volts = volts if wiring == 'par' else volts * cells
		self.amps = amps if wiring == 'ser' else amps * cells