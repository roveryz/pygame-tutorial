import pygame 
from pygame.locals import *

# initialize the game
pygame.init()
width, height = 640,480
screen = pygame.display.set_mode((width,height))

# load images
player = pygame.image.load("resources/images/dude.png")

# keep looping through
while 1:
	# clear the screen before drawing it again
	screen.fill(0)
	# draw the screen elements
	screen.blit(player, (100,100))
	# update the screen 
	pygame.display.flip()
	# loop through the events
	for event in pygame.event.get():
		# check if the event is the X button
		if event.type==pygame.QUIT:
			# if it is quit the game
			pygame.quit()
			exit(0)