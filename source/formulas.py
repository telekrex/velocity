#!/usr/bin/env python3


def solve_for_volts(watts, amps):
	return watts / amps


def solve_for_amps(watts, volts):
	return watts / volts


def solve_for_watts(amps, volts):
	return amps * volts


def nm_to_ftlbs(nm):
	# because, I guess
	return nm * 0.7376


def solve_for_hp(rpm, torque):
	return rpm * torque / 5252