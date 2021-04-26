# Alexandra Tavakelian - PCBS project Perceptual selection

import random
import pygame
import time

# Colors used in the experiment
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MAX_RESPONSE_DURATION = 2000



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


# What I need to create:
# 10 (repetitions) x 3 (duration conditions) x 2 (partial, whole report) = 60 lists of random combinations # of 6 characters (3 letters, 3 digits, no specific order)
# 4 "clock" conditions for the different display durations: a 60msec clock, a 90msec one, a 120msec and a 500msec 

# Then, I can launch the experiment itself on the screen surface. All displays (instructions + stimuli) will be displayed at the center of the screen, in a white font.

# Display the instructions for partial report, ask to press a key to display first series of stimuli

# Display 60msec condition stimuli (10 stimuli (each is a random combinations of 6 characters) for 60msec + a blank mask for 500msec after each display)

# Display 90msec condition stimuli (10 other stimuli for 90msec + mask)

# Display 120 msec condition stimuli (10 other stimuli for 120msec + mask)



# Display the instructions for whole report, ask to press a key to display first series of stimuli

# Display 60msec condition stimuli (10 stimuli (each is a random combinations of 6 characters) for 60msec + a blank mask for 500msec after each display)

# Display 90msec condition stimuli (10 other stimuli for 90msec + mask)

# Display 120 msec condition stimuli (10 other stimuli for 120msec + mask)


