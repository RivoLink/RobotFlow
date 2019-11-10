from const import PLAYER
from drawable import  Drawable

class Player(Drawable):
	
	def __init__(self,file):
		super().__init__(file,PLAYER)
		
		
	def jump(self):
		t=0
		
		
		self.position.x=10