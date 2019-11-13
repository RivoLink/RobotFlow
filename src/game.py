from const import  RULER,HEIGHT,WIDTH,WORLD,WHITE
from pygame.locals import MOUSEBUTTONDOWN

from log import  Log
from world import World
from player import Player
from drawable import  Drawable

class Game():
	
	def __init__(self):
		self.log=Log()
		self.world=None
		self.robot=None
		
	def start(self):
		self.robot=Player('idle.png')
		self.robot.position.bottom=RULER
		
		self.world=World(self.robot)
		
	def input(self,event):
		if event.type==MOUSEBUTTONDOWN:
			self.robot.jump()
	
	def render(self,screen):
		screen.fill(WHITE)
		
		self.robot.draw(screen)
		self.robot.scroll(0,0)
		
		self.world.draw(screen)
		
		self.log.set_action(str(self.robot.action))
		self.log.set_stats(str(self.world.mask))
		self.log.set_distance(str(self.world.distance))
		self.log.draw(screen)
		