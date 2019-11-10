from const import  WORLD,WHITE
from pygame.locals import MOUSEBUTTONDOWN

from player import Player
from drawable import  Drawable

class Game():
	
	def __init__(self):
		self.robot=None
		self.ground=None
	
	def start(self,screen):
		self.ground=Drawable('ground.png',WORLD)
		self.ground.position.bottom=480 #screen.get_height()
		
		self.robot=Player('idle.png')
		self.robot.position.bottom=self.ground.position.top
		
	def input(self,event):
		if(event.type==MOUSEBUTTONDOWN):
			self.robot.jump()
	
	def render(self,screen,delta):
		screen.fill(WHITE)
		
		self.ground.draw(screen)
		self.robot.draw(screen)
		
	