# Alexandra Tavakelian - PCBS project Perceptual selection

# Import relevant systems
import random, pygame, time, sys

# Colors used in the experiment
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (127, 127, 127)

max_response_duration= 2000
n_trials = 10

time_cond_60 = 60
time_cond_90 = 90
time_cond_120 = 120


# Assigning values to X and Y
display_width = 1500
display_height = 800
center_width = display_width // 2
center_height = display_height // 2

pygame.init()

# What I need to create:
# 10 (repetitions) x 3 (duration conditions) x 2 (partial, whole report) = 60 lists of random combinations # of 6 characters (3 letters, 3 digits, no specific order)
random.randint(0, 9)



# Then, I can launch the experiment itself on the screen surface. All displays (instructions + stimuli) will be displayed at the center of the screen, in a white font.

# Display the instructions for partial report, ask to press a key to display first series of stimuli
clock = pygame.time.Clock()
screen = pygame.display.set_mode((display_width, display_height))
screen_rect = screen.get_rect()
base_font = pygame.font.Font(None, 50)

instructions_text = "Try to remember as many digits as possible (not letters)."
instructions_surface = base_font.render(instructions_text, True, WHITE)
instructions_rect = instructions_surface.get_rect(center=screen_rect.center)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			instructions_text += event.unicode
			instructions_surface = base_font.render(instructions_text, True, WHITE)
			instructions_rect = instructions_surface.get_rect(center=screen_rect.center)
	
	screen.fill(BLACK)
	screen.blit(instructions_surface, instructions_rect)

	pygame.display.flip()
	clock.tick(1)
	pygame.time.delay(1000)


# Display 60msec condition stimuli (10 stimuli (each is a random combinations of 6 characters) for 60msec + a blank mask for 500msec after each display)

clock.tick(1)
pygame.time.delay(60)
pygame.display.update()
screen.fill(GREY)
pygame.time.delay(500)
pygame.display.update()

# Display 90msec condition stimuli (10 other stimuli for 90msec + mask)

clock.tick(1)
pygame.time.delay(90)
pygame.display.update()
screen.fill(GREY)
pygame.time.delay(500)
pygame.display.update()

# Display 120 msec condition stimuli (10 other stimuli for 120msec + mask)

clock.tick(1)
pygame.time.delay(120)
pygame.display.update()
screen.fill(GREY)
pygame.time.delay(500)
pygame.display.update()

# Display the instructions for whole report, ask to press a key to display first series of stimuli

# Display 60msec condition stimuli (10 stimuli (each is a random combinations of 6 characters) for 60msec + a blank mask for 500msec after each display)

# Display 90msec condition stimuli (10 other stimuli for 90msec + mask)

# Display 120 msec condition stimuli (10 other stimuli for 120msec + mask)


