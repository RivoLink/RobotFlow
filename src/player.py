from const import PLAYER
from drawable import  Drawable

class Action():
	def __init__(self,val,text):
		self.val=val
		self.text=text
		
	def __str__(self):
		return self.text
	
class Player(Drawable):
	STEP=15
	JUMPX=80
	
	WALK=Action(0,'walk(0)')
	JUMP=Action(1,'jump(1)')
	
	def __init__(self,file):
		super().__init__(file,PLAYER)
		self.isJumping=False
		self.step=self.STEP
		self.y0=self.position.y
		self.action=self.WALK
		
	def draw(self,screen):
		if self.isJumping:
			self.__jumping()
		super().draw(screen)
		
	def jump(self):
		if not self.isJumping:
			self.action=self.JUMP
			self.isJumping=True
			self.y0=self.position.y
			
	def scroll(self,origin,limit):
		if not self.isJumping and self.position.y==self.y0:
			if self.position.left > 5:
				self.position.x-=1
                    
	def __jumping(self):
		if self.step > -self.STEP+1:
			self.step-=1
			self.position.y -= (self.step * abs(self.step)) * 0.2 
		else:
			self.action=self.WALK
			self.isJumping=False
			self.step=self.STEP
			self.position.y=self.y0
		self.position.x+=self.JUMPX/self.STEP
