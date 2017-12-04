import pygame
from tictactoe import Board

pygame.init()
board = Board()
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 72)

def game_intro():

    intro = True

    while intro:
  		mouse = pygame.mouse.get_pos()
  		click = pygame.mouse.get_pressed() 

  		for event in pygame.event.get():
  			if event.type == pygame.QUIT:
  				pygame.quit()
  				quit()
  		board.first_menu(mouse[0],mouse[1])
  		pygame.display.flip()
  		pygame.display.update()
  		if(click[0] == 1 and 125>mouse[0]>25 and 275>mouse[1]>200):
  			comp_play()
  		if(click[0] == 1 and 275>mouse[0]>175 and 275>mouse[1]>200):
  			pygame.quit()
  			quit()

  		# clock.tick(15)

def comp_play():
	done = False
	board.initialize()
	while not done:
	        for event in pygame.event.get():
	            mouse = pygame.mouse.get_pos() 
	            click = pygame.mouse.get_pressed()
	            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
	                done = True
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP1 or event.type == pygame.KEYUP and event.key == pygame.K_1:
	                board.nxt_turn(1)    
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP2 or event.type == pygame.KEYUP and event.key == pygame.K_2:
	                board.nxt_turn(2)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP3 or event.type == pygame.KEYUP and event.key == pygame.K_3:
	                board.nxt_turn(3)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP4 or event.type == pygame.KEYUP and event.key == pygame.K_4:
	                board.nxt_turn(4)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP5 or event.type == pygame.KEYUP and event.key == pygame.K_5:
	                board.nxt_turn(5)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP6 or event.type == pygame.KEYUP and event.key == pygame.K_6:
	                board.nxt_turn(6)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP7 or event.type == pygame.KEYUP and event.key == pygame.K_7:
	                board.nxt_turn(7)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP8 or event.type == pygame.KEYUP and event.key == pygame.K_8:
	                board.nxt_turn(8)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP9 or event.type == pygame.KEYUP and event.key == pygame.K_9:
	                board.nxt_turn(9)
	            if 100>mouse[0]>20 and 280>mouse[1]>200 and click[0] == 1:
	                board.nxt_turn(1)
	            if 190>mouse[0]>110 and 280>mouse[1]>200 and click[0] == 1:
	                board.nxt_turn(2)
	            if 280>mouse[0]>200 and 280>mouse[1]>200 and click[0] == 1:
	                board.nxt_turn(3)
	            if 100>mouse[0]>20 and 190>mouse[1]>110 and click[0] == 1:
	                board.nxt_turn(4)
	            if 190>mouse[0]>110 and 190>mouse[1]>110 and click[0] == 1:
	                board.nxt_turn(5)
	            if 280>mouse[0]>200 and 190>mouse[1]>110 and click[0] == 1:
	                board.nxt_turn(6)
	            if 100>mouse[0]>20 and 100>mouse[1]>20 and click[0] == 1:
	                board.nxt_turn(7)
	            if 190>mouse[0]>110 and 100>mouse[1]>20 and click[0] == 1:
	                board.nxt_turn(8)
	            if 280>mouse[0]>200 and 100>mouse[1]>20 and click[0] == 1:
	                board.nxt_turn(9)

	        pygame.display.flip()

game_intro()