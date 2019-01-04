# 1 import
import pygame 
from pygame.locals import *
import math
import random

# 2 initialize the game
pygame.init()
width, height = 640,480
screen = pygame.display.set_mode((width,height))
keys=[False,False,False,False]
playerpos = [100,100]
# for shot
acc=[0,0] # trace player's accuracy
# this accuracy is a list of number
# here record the arrows num and shotted enermies' num
arrows=[] # trace arrow
# enermies' list and a timer to create enermy
badtimer = 100
badtimer1 = 0
badguys=[[640,100]]
healthvalue=194

# 3 load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
# load arrow's image
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg1 = pygame.image.load("resources/images/badguy.png")
badguyimg = badguyimg1

# 4 keep looping through
while 1:
	# 5 clear the screen before drawing it again
	screen.fill(0)
	# 6 draw the screen elements
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			screen.blit(grass,(x*100,y*100))
	# notice
	# grass need to be paint first, so it will at bottom
	# if player first,
	# then cannot see player, override by grass
	screen.blit(castle,(0,30))
	screen.blit(castle,(0,135))
	screen.blit(castle,(0,240))
	screen.blit(castle,(0,345))
	
	position = pygame.mouse.get_pos()
	# tan
	angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26)) # why need 32,26?
	playerrot = pygame.transform.rotate(player, 360-angle*57.29) # where the 57.29 from???
	playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
	screen.blit(playerrot, playerpos1)	
	# 6.2 draw the arrow
	for bullet in arrows:
		index=0
		velx=math.cos(bullet[0])*10
		vely=math.sin(bullet[0])*10
		bullet[1]+=velx
		bullet[2]+=vely
		if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
			arrows.pop(index)
		index+=1
		for projectile in arrows:
			arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
			screen.blit(arrow1, (projectile[1], projectile[2]))
	# 6.3 Dray badguys
	if badtimer == 0:
		badguys.append([640, random.randint(50,430)])
		badtimer=100-(badtimer1*2)
		if badtimer1>=35:
			badtimer1=35
		else:
			badtimer1+=5
	index=0
	# update enermy's x and check if out of screen
	for badguy in badguys:
		if badguy[0]<-64:
			badguys.pop(index)
		badguy[0]-=7
		# 6.3.1 attack castle
		badrect = pygame.Rect(badguyimg.get_rect())
		badrect.top=badguy[1]
		badrect.left=badguy[0]
		if badrect.left<64:
			healthvalue-=random.randint(5,20)
			badguys.pop(index)
		# 6.3.2 check for collisions
		index1=0
		for bullet in arrows:
			bullrect=pygame.Rect(arrow.get_rect())
			bullrect.left=bullet[1]
			bullrect.top=bullet[2]
			if badrect.colliderect(bullrect):
				acc[0]+=1
				badguys.pop(index)
				arrows.pop(index1)
			index1+=1
		# 6.3.3 next bad guy
		index+=1
	# draw all enermy
	for badguy in badguys:
		screen.blit(badguyimg, badguy)
			
		
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
		if event.type==pygame.MOUSEBUTTONDOWN:
			positon = pygame.mouse.get_pos()
			acc[1]+=1
			# The following code will calculate the angle of rotation of the arrow based on the position of the player and the cursor, and store it in the arrows array.
			arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
		# 9 Move Player
		if keys[0]:
			playerpos[1]-=5
		elif keys[2]:
			playerpos[1]+=5
		if keys[1]:
			playerpos[0]-=5
		elif keys[3]:
			playerpos[0]+=5
	badtimer-=1