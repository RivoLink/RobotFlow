import numpy as np
from const import RULER,WORLD,WIDTH,HEIGHT
from pygame import Rect
from drawable import Drawable

RED=(255,0,0)
BLUE=(0,0,255)

class World:
	def __init__(self,robot):
		self.rects=[]
		self.mask=[]
		
		self.robot=robot
		
		self.block1=None
		self.ground=None
		
		self.__create_rects()
		self.__create_items()
		
	@property
	def distance(self):
		d=int(self.block1.position.x-self.robot.position.x)
		if not self.robot.isJumping and 0<d and d<96:
			self.robot.jump()
		return d
	
	
	def __create_rects(self):
		x=self.robot.position.center[0]
		for idx in range(0,23):
			rect=Rect((x+10*idx,0),(10,10))
			rect.bottom=RULER
			self.rects.append(rect)
		self.mask=np.zeros(len(self.rects),np.uint8)
		
	def __create_items(self):
		self.ground=Drawable('ground.png',WORLD)
		self.ground.position.bottom=HEIGHT
		
		self.block1=Drawable('block1.png',WORLD)
		self.block1.position.x=WIDTH+10
		self.block1.position.bottom=RULER
		
	def draw(self,screen):
		self.ground.draw(screen)
		self.ground.scroll(0,WIDTH)
		
		self.block1.draw(screen)
		self.block1.scroll(WIDTH+10,-10)
		
		for idx in range(0,len(self.rects)):
			rect=self.rects[idx]
			rect.right=self.robot.position.center[0]+10*idx
			if rect.colliderect(self.block1.rect):
				self.mask[idx]=1
				screen.fill(RED,rect)
			else:
				self.mask[idx]=0
				screen.fill(BLUE,rect)
	