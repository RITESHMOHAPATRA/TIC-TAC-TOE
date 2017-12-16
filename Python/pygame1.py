import pygame
from tictactoe import Board
import mini2
from mini2 import Tic

pygame.init()
board = Board()
tic = Tic()
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

  		board.first_menu(mouse[0],mouse[1])  #Co-ordinates of mouse pointer passed so that menu options can be highlighted. 
  		pygame.display.flip()
  		pygame.display.update()
  		if(click[0] == 1 and 140>mouse[0]>20 and 190>mouse[1]>100):
  			game_mode()
  			intro = False
  		if(click[0] == 1 and 280>mouse[0]>160 and 190>mouse[1]>100):
  			PVPplay()
  			intro = False
  		if(click[0] == 1 and 210>mouse[0]>90 and 290>mouse[1]>200):
  			pygame.quit()
  			quit()

def game_end(value):

	end = True

	while end:
		mouse = pygame.mouse.get_pos()
  		click = pygame.mouse.get_pressed() 

  		for event in pygame.event.get():
  			if event.type == pygame.QUIT:
  				pygame.quit()
  				quit()
  		board.last_menu(value,mouse[0],mouse[1])
  		pygame.display.flip()
  		pygame.display.update()
  		if(click[0] == 1 and 125>mouse[0]>25 and 275>mouse[1]>200):
  			game_intro()
  			end = False
  		if(click[0] == 1 and 275>mouse[0]>175 and 275>mouse[1]>200):
  			pygame.quit()
  			quit()

def game_mode():

	end = True

	while end:
		mouse = pygame.mouse.get_pos()
  		click = pygame.mouse.get_pressed() 

  		for event in pygame.event.get():
  			if event.type == pygame.QUIT:
  				pygame.quit()
  				quit()
  		board.AI_menu(mouse[0],mouse[1])
  		pygame.display.flip()
  		pygame.display.update()
  		if(click[0] == 1 and 125>mouse[0]>25 and 275>mouse[1]>200):
  			comp_play_easy()
  			end = False
  		if(click[0] == 1 and 275>mouse[0]>175 and 275>mouse[1]>200):
  			comp_play_hard()
  			end = False

def comp_play_hard():
	done = False
	tic.initialize()
	value = 'ongoing'
	while not done:
	        for event in pygame.event.get():
	            mouse = pygame.mouse.get_pos() 
	            click = pygame.mouse.get_pressed()
	            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
	                done = True
	            #Input involves two methods, one by pressing keys and other by mouse input. This part is key input.
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP1 or event.type == pygame.KEYUP and event.key == pygame.K_1:
	                value = mini2.nxt_turn1(7,tic)    
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP2 or event.type == pygame.KEYUP and event.key == pygame.K_2:
	                value = mini2.nxt_turn1(8,tic)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP3 or event.type == pygame.KEYUP and event.key == pygame.K_3:
	                value = mini2.nxt_turn1(9,tic)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP4 or event.type == pygame.KEYUP and event.key == pygame.K_4:
	                value = mini2.nxt_turn1(4,tic)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP5 or event.type == pygame.KEYUP and event.key == pygame.K_5:
	                value = mini2.nxt_turn1(5,tic)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP6 or event.type == pygame.KEYUP and event.key == pygame.K_6:
	                value = mini2.nxt_turn1(6,tic)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP7 or event.type == pygame.KEYUP and event.key == pygame.K_7:
	                value = mini2.nxt_turn1(1,tic)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP8 or event.type == pygame.KEYUP and event.key == pygame.K_8:
	                value = mini2.nxt_turn1(2,tic)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP9 or event.type == pygame.KEYUP and event.key == pygame.K_9:
	                value = mini2.nxt_turn1(3,tic)
	            #This part is mouse input. Functions called only if the mouse is clicked at its certain domain defined by x and y coordinates.
	            if 100>mouse[0]>20 and 280>mouse[1]>200 and click[0] == 1:
	                value = mini2.nxt_turn1(7,tic)
	            if 190>mouse[0]>110 and 280>mouse[1]>200 and click[0] == 1:
	                value = mini2.nxt_turn1(8,tic)
	            if 280>mouse[0]>200 and 280>mouse[1]>200 and click[0] == 1:
	                value = mini2.nxt_turn1(9,tic)
	            if 100>mouse[0]>20 and 190>mouse[1]>110 and click[0] == 1:
	                value = mini2.nxt_turn1(4,tic)
	            if 190>mouse[0]>110 and 190>mouse[1]>110 and click[0] == 1:
	                value = mini2.nxt_turn1(5,tic)
	            if 280>mouse[0]>200 and 190>mouse[1]>110 and click[0] == 1:
	                value = mini2.nxt_turn1(6,tic)
	            if 100>mouse[0]>20 and 100>mouse[1]>20 and click[0] == 1:
	                value = mini2.nxt_turn1(1,tic)
	            if 190>mouse[0]>110 and 100>mouse[1]>20 and click[0] == 1:
	                value = mini2.nxt_turn1(2,tic)
	            if 280>mouse[0]>200 and 100>mouse[1]>20 and click[0] == 1:
	                value = mini2.nxt_turn1(3,tic)
	            
		pygame.display.flip()
		if value != 'ongoing':
			done = True
	if value == 'Player':
		game_end('Player')
	if value == 'Computer':
		game_end('Computer')
	if value == 'Draw':
		game_end(0) 

def comp_play_easy():
	done = False
	board.initialize()
	value = 'ongoing'
	while not done:
	        for event in pygame.event.get():
	            mouse = pygame.mouse.get_pos() 
	            click = pygame.mouse.get_pressed()
	            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
	                done = True
	            #Input involves two methods, one by pressing keys and other by mouse input. This part is key input.
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP1 or event.type == pygame.KEYUP and event.key == pygame.K_1:
	                value = board.nxt_turn1(1)    
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP2 or event.type == pygame.KEYUP and event.key == pygame.K_2:
	                value = board.nxt_turn1(2)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP3 or event.type == pygame.KEYUP and event.key == pygame.K_3:
	                value = board.nxt_turn1(3)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP4 or event.type == pygame.KEYUP and event.key == pygame.K_4:
	                value = board.nxt_turn1(4)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP5 or event.type == pygame.KEYUP and event.key == pygame.K_5:
	                value = board.nxt_turn1(5)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP6 or event.type == pygame.KEYUP and event.key == pygame.K_6:
	                value = board.nxt_turn1(6)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP7 or event.type == pygame.KEYUP and event.key == pygame.K_7:
	                value = board.nxt_turn1(7)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP8 or event.type == pygame.KEYUP and event.key == pygame.K_8:
	                value = board.nxt_turn1(8)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP9 or event.type == pygame.KEYUP and event.key == pygame.K_9:
	                value = board.nxt_turn1(9)
	            #This part is mouse input. Functions called only if the mouse is clicked at its certain domain defined by x and y coordinates.
	            if 100>mouse[0]>20 and 280>mouse[1]>200 and click[0] == 1:
	                value = board.nxt_turn1(1)
	            if 190>mouse[0]>110 and 280>mouse[1]>200 and click[0] == 1:
	                value = board.nxt_turn1(2)
	            if 280>mouse[0]>200 and 280>mouse[1]>200 and click[0] == 1:
	                value = board.nxt_turn1(3)
	            if 100>mouse[0]>20 and 190>mouse[1]>110 and click[0] == 1:
	                value = board.nxt_turn1(4)
	            if 190>mouse[0]>110 and 190>mouse[1]>110 and click[0] == 1:
	                value = board.nxt_turn1(5)
	            if 280>mouse[0]>200 and 190>mouse[1]>110 and click[0] == 1:
	                value = board.nxt_turn1(6)
	            if 100>mouse[0]>20 and 100>mouse[1]>20 and click[0] == 1:
	                value = board.nxt_turn1(7)
	            if 190>mouse[0]>110 and 100>mouse[1]>20 and click[0] == 1:
	                value = board.nxt_turn1(8)
	            if 280>mouse[0]>200 and 100>mouse[1]>20 and click[0] == 1:
	                value = board.nxt_turn1(9)
	            
		pygame.display.flip()
		if value != 'ongoing':
			done = True
	if value == 'Player':
		game_end('Player')
	if value == 'Computer':
		game_end('Computer')
	if value == 0:
		game_end(0) 

def PVPplay():
	done = False
	board.initialize()
	value = 'ongoing'
	while not done:
	        for event in pygame.event.get():
	            mouse = pygame.mouse.get_pos() 
	            click = pygame.mouse.get_pressed()
	            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
	                done = True
	            #Input involves two methods, one by pressing keys and other by mouse input. This part is key input.
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP1 or event.type == pygame.KEYUP and event.key == pygame.K_1:
	                value = board.nxt_turn2(1)    
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP2 or event.type == pygame.KEYUP and event.key == pygame.K_2:
	                value = board.nxt_turn2(2)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP3 or event.type == pygame.KEYUP and event.key == pygame.K_3:
	                value = board.nxt_turn2(3)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP4 or event.type == pygame.KEYUP and event.key == pygame.K_4:
	                value = board.nxt_turn2(4)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP5 or event.type == pygame.KEYUP and event.key == pygame.K_5:
	                value = board.nxt_turn2(5)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP6 or event.type == pygame.KEYUP and event.key == pygame.K_6:
	                value = board.nxt_turn2(6)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP7 or event.type == pygame.KEYUP and event.key == pygame.K_7:
	                value = board.nxt_turn2(7)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP8 or event.type == pygame.KEYUP and event.key == pygame.K_8:
	                value = board.nxt_turn2(8)
	            if event.type == pygame.KEYUP and event.key == pygame.K_KP9 or event.type == pygame.KEYUP and event.key == pygame.K_9:
	                value = board.nxt_turn2(9)
	            #This part is mouse input. Functions called only if the mouse is clicked at its certain domain defined by x and y coordinates.
	            if 100>mouse[0]>20 and 280>mouse[1]>200 and click[0] == 1:
	                value = board.nxt_turn2(1)
	            if 190>mouse[0]>110 and 280>mouse[1]>200 and click[0] == 1:
	                value = board.nxt_turn2(2)
	            if 280>mouse[0]>200 and 280>mouse[1]>200 and click[0] == 1:
	                value = board.nxt_turn2(3)
	            if 100>mouse[0]>20 and 190>mouse[1]>110 and click[0] == 1:
	                value = board.nxt_turn2(4)
	            if 190>mouse[0]>110 and 190>mouse[1]>110 and click[0] == 1:
	                value = board.nxt_turn2(5)
	            if 280>mouse[0]>200 and 190>mouse[1]>110 and click[0] == 1:
	                value = board.nxt_turn2(6)
	            if 100>mouse[0]>20 and 100>mouse[1]>20 and click[0] == 1:
	                value = board.nxt_turn2(7)
	            if 190>mouse[0]>110 and 100>mouse[1]>20 and click[0] == 1:
	                value = board.nxt_turn2(8)
	            if 280>mouse[0]>200 and 100>mouse[1]>20 and click[0] == 1:
	                value = board.nxt_turn2(9)

		pygame.display.flip()
		if value != 'ongoing':
			done = True
	if value == 'Player1':
		game_end('Player1')
	if value == 'Player2':
		game_end('Player2')
	if value == 0:
		game_end(0) 
			


game_intro()
pygame.display.flip()
pygame.display.update()