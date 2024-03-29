import pygame
from tictactoe import Board

import mini2
from mini2 import Tic


#initialization

pygame.init()
board = Board()
tic = Tic()
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 72)

#start the game
def game_intro():
    intro = True #For generating an infinite loop.

    #run the game while unless player press quit or close the game
    while intro:
  		mouse = pygame.mouse.get_pos()
  		click = pygame.mouse.get_pressed() 

  		#get the mouse click and event
  		for event in pygame.event.get():
  			if event.type == pygame.QUIT:
  				pygame.quit()
  				print 'Exit 1'
  				quit()


  		board.first_menu(mouse[0],mouse[1])  #Co-ordinates of mouse pointer passed so that menu options can be highlighted. 
  		pygame.display.set_caption("Game Menu")

  		#load the main manu based screen, asking user to select whom he has to play with AI,PvP or Quit		

  		board.first_menu(mouse[0],mouse[1])  #Co-ordinates of mouse pointer passed so that menu options can be highlighted. 

  		pygame.display.flip()

  		clock=pygame.time.Clock() 
		clock.tick(60)
  		mouse = pygame.mouse.get_pos()
  		click = pygame.mouse.get_pressed() 
  		
  		pygame.display.update()

  		#Passing to different menus if clicked at the right positions.
  		if(click[0] == 1 and 140>mouse[0]>20 and 190>mouse[1]>100):
  			game_mode()

  		if(click[0] == 1 and 140>mouse[0]>20 and 190>mouse[1]>100): #getting the click from the user if he selected vs AI
  			comp_play()

  			intro = False
  		if(click[0] == 1 and 280>mouse[0]>160 and 190>mouse[1]>100): #getting the click from the user if he selected Player to Player
  			PVPplay()
  			intro = False

  		if(click[0] == 1 and 210>mouse[0]>90 and 290>mouse[1]>200):
  			quitmenu()
  			intro = False


        
  		if(click[0] == 1 and 210>mouse[0]>90 and 290>mouse[1]>200): #getting the click from the user if he wants to quit
  		if(click[0] == 1 and 210>mouse[0]>90 and 290>mouse[1]>200): #getting the click from the user if he wants to
  			pygame.quit()
  			print 'Exit 2'
  			quit()
'''
After the game is over and the result is either Computer, Player or Draw
It displays the last_menu screen and asks whether to Play again,If yes ,control tranfer to game_into()'s first_menu again
If no then exit. 
'''

def game_end(value):
	end = True  #For generating an infinite loop.

	while end:
		
		mouse = pygame.mouse.get_pos()
  		click = pygame.mouse.get_pressed() 
  		for event in pygame.event.get():
  			if event.type == pygame.QUIT:
  				pygame.quit()
  				quit()

  		board.last_menu(value,mouse[0],mouse[1]) #Co-ordinates of mouse pointer passed so that menu options can be highlighted.
  		pygame.display.set_caption("Game Over")
  		pygame.display.flip()
  		pygame.display.update()
  		if(click[0] == 1 and 125>mouse[0]>25 and 275>mouse[1]>200):
  			game_intro()
  			end = False
  		if(click[0] == 1 and 275>mouse[0]>175 and 275>mouse[1]>200):
  			quitmenu()
  			end = False

def quitmenu():
 	end = True  #For generating an infinite loop.

	while end:
		mouse = pygame.mouse.get_pos()
	  	click = pygame.mouse.get_pressed() 

	  	for event in pygame.event.get():
	  		if event.type == pygame.QUIT:
	  			pygame.quit()
	  			quit()
	  	board.quit_menu(mouse[0],mouse[1])  #Co-ordinates of mouse pointer passed so that menu options can be highlighted.
	  	pygame.display.set_caption("Quit Menu")
	  	pygame.display.flip()
	  	pygame.display.update()
  		#Passing to different menus if clicked at the right positions.
	  	if(click[0] == 1 and 125>mouse[0]>25 and 275>mouse[1]>200):
	  		game_intro()
	  		end = False
	  	if(click[0] == 1 and 275>mouse[0]>175 and 275>mouse[1]>200):
	  		pygame.quit()
	  		quit()



def game_mode():
	end = True   #For generating an infinite loop.

	while end:
		mouse = pygame.mouse.get_pos()
  		click = pygame.mouse.get_pressed() 

  		for event in pygame.event.get():
  			if event.type == pygame.QUIT:
  				pygame.quit()
  				quit()
  		board.AI_menu(mouse[0],mouse[1])  #Co-ordinates of mouse pointer passed so that menu options can be highlighted.
  		pygame.display.set_caption("Game Mode")
  		pygame.display.flip()
  		pygame.display.update()
  		#Passing to different menus if clicked at the right positions.
  		if(click[0] == 1 and 125>mouse[0]>25 and 275>mouse[1]>200):
  			comp_play_easy()
  			end = False
  		if(click[0] == 1 and 275>mouse[0]>175 and 275>mouse[1]>200):
  			comp_play_hard()
  			end = False

def comp_play_hard():
	done = False  #For generating an infinite loop.
	tic.initialize()
	pygame.display.set_caption("Computer Play - Hard")
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
	#In case of the game getting over, displaying of results.
	if value == 'Player':
		game_end('Player')
	if value == 'Computer':
		game_end('Computer')
	if value == 'Draw':
		game_end(0) 

def comp_play_easy():
	done = False  #For generating an infinite loop.

  		#display the last_menu to get the users choice to play again !		
  		board.last_menu(value,mouse[0],mouse[1])
  		pygame.display.flip()
  		pygame.display.update()

  		#remove the bug of mouse getting already clcked by the user	
  		clock=pygame.time.Clock() #wait before taking the next mouse click (solved the problem of click getting saved)
		clock.tick(60)
		lst = list(click)
  		lst[0] = 0
  		click = tuple(lst)
  		lst = list(mouse)
  		lst[0] = 150
  		lst[1] = 150
  		mouse = tuple(lst)

  		#If yes the show the first screen
  		if(mouse[0] == 150 and mouse[1] == 150 and click[0] == 0):
  			clock=pygame.time.Clock() #wait before taking the next mouse click (solved the problem of click getting saved)
			clock.tick(60)
	  		mouse = pygame.mouse.get_pos()
	  		click = pygame.mouse.get_pressed() 
	  				
	  		if(125>mouse[0]>25 and 275>mouse[1]>200 and click[0] == 1):
	  				game_intro()
	  				end = False
	  		#If no then exit	
	  		if(275>mouse[0]>175 and 275>mouse[1]>200 and click[0] == 1):
	  				pygame.quit()
	  				quit()
  		lst[0] = 0
  		lst[1] = 0
  		mouse = tuple(lst)
		print 'click = ', click[0]
  		mouse = pygame.mouse.get_pos()
  		#click = pygame.mouse.get_pressed() 
 				
  		#If yes the show the first screen
  		if(125>mouse[0]>25 and 275>mouse[1]>200):
  			click = pygame.mouse.get_pressed() #even this seems not to work
  			if(click[0] == 1):
  				game_intro()
  				end = False
  		#If no then exit	
  		if(275>mouse[0]>175 and 275>mouse[1]>200):
  			click = pygame.mouse.get_pressed()
  			if(click[0] == 1):
  				pygame.quit()
  				quit()

#If player wants to play with AI(computer) this function will be called
def comp_play():
	done = False

	board.initialize()
	pygame.display.set_caption("Computer Play - Easy")
	value = 'ongoing'
	while not done:
			#Input involves two methods, one by pressing keys(1...9) and other by mouse input. 
	        for event in pygame.event.get():
	            mouse = pygame.mouse.get_pos() 
	            click = pygame.mouse.get_pressed()
	            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
	                done = True

	            #This part is key input.

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
	#In case of the game getting over, displaying of results.
	if value == 'Player':
		game_end('Player')
	if value == 'Computer':
		game_end('Computer')
	if value == 0:
		game_end(0) 

#If player wants to play with other player then this function will be called
def PVPplay():
	done = False  #For generating an infinite loop.
	board.initialize()
	pygame.display.set_caption("P v P Play")
	value = 'ongoing'
	while not done:
			#Input involves two methods, one by pressing keys and other by mouse input.
	        for event in pygame.event.get():
	            mouse = pygame.mouse.get_pos() 
	          #  print 'mouse position ', mouse
	            click = pygame.mouse.get_pressed()
	          #  print 'click position ', click
	            if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
	                done = True


	            #This part is key input.

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
	#In case of the game getting over, displaying of results.
	if value == 'Player1':
		game_end('Player1')
	if value == 'Player2':
		game_end('Player2')
	if value == 0:
		game_end(0) 
			



game_intro()   #Displying of first menu as the game starts.

#start the game
game_intro()

pygame.display.flip()
pygame.display.update()