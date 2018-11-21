# 1 import
import pygame 
from pygame.locals import *

# 2 initialize the game
pygame.init()
width, height = 640,480
screen = pygame.display.set_mode((width,height))
keys=[False,False,False,False]
playerpos = [100,100]
# 3 load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

# 4 keep looping through
while 1:
	# 5 clear the screen before drawing it again
	screen.fill(0)
	# 6 draw the screen elements
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			screen.blit(grass,(x*100,y*100))
	screen.blit(player, playerpos)
	# notice
	# grass need to be paint first, so it will at bottom
	# if player first,
	# then cannot see player, override by grass
	screen.blit(castle,(0,30))
	screen.blit(castle,(0,135))
	screen.blit(castle,(0,240))
	screen.blit(castle,(0,345))
	# 7 update the screen 
	pygame.display.flip()
	# 8 loop through the events
	for event in pygame.event.get():
		# check if the event is the X button
		if event.type==pygame.QUIT:
			# if it is quit the game
			pygame.quit()
			exit(0)
		if event.type==pygame.KEYDOWN:
			if event.key==K_w:
				keys[0]=True
			elif event.key==K_a:
				keys[1]=True
			elif event.key==K_s:
				keys[2]=True
			elif event.key==K_d:
				keys[3]=True
		if event.type==pygame.KEYUP:
			if event.key==K_w:
				keys[0]=False
			elif event.key==K_a:
				keys[1]=False
			elif event.key==K_s:
				keys[2]=False
			elif event.key==K_d:
				keys[3]=False
		# 9 Move Player
		if keys[0]:
			playerpos[1]-=5
		elif keys[2]:
			playerpos[1]+=5
		if keys[1]:
			playerpos[0]-=5
		elif keys[3]:
			playerpos[0]+=5