#!/usr/bin/env python3


def solve_for_volts(watts, amps):
	return watts / amps


def solve_for_amps(watts, volts):
	return watts / volts


def solve_for_watts(amps, volts):
	return amps * volts


def nm_to_ftlbs(nm):
	return nm * 0.7376


def watts_to_torque(watts):
	# 1 watt = 1 newton-meter
	return nm_to_ftlbs(watts)


def estimate_hp(rpm, torque, drive='rear'):
	# loss = 0.15 if drive == 'rear' else '0.10'
	# finish this
	return rpm * torque / 5252