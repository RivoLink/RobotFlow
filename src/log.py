import pygame
from pygame import Rect
from const import WHITE,WIDTH,HEIGHT

class Label:
	def __init__(self,text,pos):
		self.text=text
		self.x=pos[0]
		self.y=pos[1]
		
	@property
	def position(self):
		return (self.x,self.y)
		
	@property
	def position_h(self):
		return (self.x,self.y+HEIGHT)
		
class Log:
	def __init__(self):
		self.font = pygame.font.SysFont("DejaVuSans", 20)
		self.labels=[
			Label(self.font.render('action:',1,WHITE),(0,0)),
			Label(self.font.render('state:',1,WHITE),(WIDTH/4,0)),
			Label(self.font.render('distance:',1,WHITE),(0,30))
		]
		
	def set_action(self,text):
		self.set_text(0,'action:'+text)
	
	def set_stats(self,text):
		self.set_text(1,'stats:'+text)
		
	def set_distance(self,text):
		self.set_text(2,'distance:'+text)
		
	def set_text(self,index,text):
		label=self.labels[index]
		self.labels[index]=Label(self.font.render(text,1,WHITE),label.position)
	
	def add_text(self,text,pos):
		label=Label(self.font.render(text,1,WHITE),pos)
		self.labels.append(label)
		
	def draw(self,screen):
		screen.fill((0,0,0),Rect((0,HEIGHT),(WIDTH,screen.get_height()-HEIGHT)))
		
		for label in self.labels:
			screen.blit(label.text,label.position_h)
		
		
		
		
		
		
		
		
		