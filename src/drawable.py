import pygame
from const import PATH_SPRITES

class Drawable:
	def __init__(self,file,T):
		self.T=T
		file=PATH_SPRITES.format(self.T)+file
		self._image=pygame.image.load(file).convert_alpha()
		self._rect=self._image.get_rect()
	
	@property
	def position(self):
		return self._rect
	
	def draw(self,screen):
		screen.blit(self._image,self._rect)
		
	def scroll(self,screen):
		if self.position.right>screen.get_width():
			self.position.x-=1
		else:
			self.position.x=0
		
	