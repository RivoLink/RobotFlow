import pygame
from const import PATH_SPRITES

class Drawable:
	def __init__(self,file,T):
		self.T=T
		file=PATH_SPRITES.format(self.T)+file
		self.image=pygame.image.load(file).convert_alpha()
		self.rect=self.image.get_rect()
		
	@property
	def position(self):
		return self.rect
	
	def draw(self,screen):
		screen.blit(self.image,self.rect)
		
	def scroll(self,origin,limit):
		if self.position.right>limit:
			self.position.x-=1
		else:
			self.position.x=origin
		
	