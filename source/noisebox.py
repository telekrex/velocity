#!/usr/bin/env python3
import pygame
import time
pygame.mixer.init()


RPM = 5000


pygame.mixer.music.load('blp2.wav')
run = True
while run:
	pygame.mixer.music.play(loops=0)
	time.sleep(60/RPM)