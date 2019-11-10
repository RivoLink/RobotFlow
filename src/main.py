import pygame
from game import  Game

pygame.init()

clock=pygame.time.Clock()
screen=pygame.display.set_mode((720, 480))

game=Game()
game.start(screen)

while True:
	
	for ev in pygame.event.get():
		game.input(ev)
		
	tick=clock.tick(60)
	
	game.render(screen,tick)
	
	pygame.display.flip()
