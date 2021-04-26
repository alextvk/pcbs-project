# Alexandra Tavakelian - PCBS project Perceptual selection

import random
import pygame
import time

# Colors used in the experiment
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MAX_RESPONSE_DURATION = 2000

trials = [('')]

# Assigning values to X and Y
display_width = 800
display_height = 800
center_width = display_width // 2
center_height = display_height // 2

# Creating the Graphic Window 
pygame.init()
screen = pygame.display.set_mode((display_width, display_height), pygame.DOUBEBUF)
pygame.display.set_caption("Display Stimuli")
screen.fill(BLACK)

# clock = pygame.time.Clock() or time = 60 ? 

# Font and text parameters 
font = pygame.font.Font("Arial.ttf", 100)
text = font.render("A1B2C3", True, WHITE)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	pygame.display.update()

