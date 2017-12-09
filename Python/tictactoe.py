# -*- coding: utf-8 -*-      
import random
import pygame

class Board(object):    
    def __init__(self):
        self.screen = pygame.display.set_mode((300, 300))
        self.color = (100, 100, 200)
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (200,0,0)
        self.green = (0,200,0)
        self.bright_red = (255,0,0)
        self.bright_green = (0,255,0) 
        self.marker = 'O'
    #calls update surface and marks the letter at the given position    
    def makeMove(self,copy,letter, position):
        if not copy:
            self.theBoard[position] = letter
            self.update_surface(letter,position)
        else:
            copy[position] = letter
            return copy
                
    def update_surface(self,letter,position):
        #All the X's and O's carefully set to be in the center of their respective boxes.
        #O's are basic circles whereas X's are combination of two lines for better visual effect.
        if letter == 'X':
            if(position == 1):
                pygame.draw.line(self.screen, self.bright_green, (30, 210), (90, 270), 10)
                pygame.draw.line(self.screen, self.bright_green, (30, 270), (90, 210), 10)
            if(position == 2):
                pygame.draw.line(self.screen, self.bright_green, (120, 210), (180, 270), 10)
                pygame.draw.line(self.screen, self.bright_green, (120, 270), (180, 210), 10)
            if(position == 3):
                pygame.draw.line(self.screen, self.bright_green, (210, 210), (270, 270), 10)
                pygame.draw.line(self.screen, self.bright_green, (210, 270), (270, 210), 10)
            if(position == 4):
                pygame.draw.line(self.screen, self.bright_green, (30, 120), (90, 180), 10)
                pygame.draw.line(self.screen, self.bright_green, (30, 180), (90, 120), 10)   
            if(position == 5):
                pygame.draw.line(self.screen, self.bright_green, (120, 120), (180, 180), 10)
                pygame.draw.line(self.screen, self.bright_green, (120, 180), (180, 120), 10)
            if(position == 6):
                pygame.draw.line(self.screen, self.bright_green, (210, 120), (270, 180), 10)
                pygame.draw.line(self.screen, self.bright_green, (210, 180), (270, 120), 10)
            if(position == 7):
                pygame.draw.line(self.screen, self.bright_green, (30, 30), (90, 90), 10)
                pygame.draw.line(self.screen, self.bright_green, (30, 90), (90, 30), 10)
            if(position == 8):
                pygame.draw.line(self.screen, self.bright_green, (120, 30), (180, 90), 10)
                pygame.draw.line(self.screen, self.bright_green, (120, 90), (180, 30), 10)
            if(position == 9):
                pygame.draw.line(self.screen, self.bright_green, (210, 30), (270, 90), 10)
                pygame.draw.line(self.screen, self.bright_green, (210, 90), (270, 30), 10)
        if letter == 'O':
            if(position == 1):
                pygame.draw.circle(self.screen,self.bright_red, (60,240), 30)
            if(position == 2):
                pygame.draw.circle(self.screen,self.bright_red, (150,240), 30)
            if(position == 3):
                pygame.draw.circle(self.screen,self.bright_red, (240,240), 30)
            if(position == 4):
                pygame.draw.circle(self.screen,self.bright_red, (60,150), 30)
            if(position == 5):
                pygame.draw.circle(self.screen,self.bright_red, (150,150), 30)
            if(position == 6):
                pygame.draw.circle(self.screen,self.bright_red, (240,150), 30)
            if(position == 7):
                pygame.draw.circle(self.screen,self.bright_red, (60,60), 30)
            if(position == 8):
                pygame.draw.circle(self.screen,self.bright_red, (150,60), 30)
            if(position == 9):
                pygame.draw.circle(self.screen,self.bright_red, (240,60), 30)    

    #check if the board contains 3 consecutive same letter            
    def isWinner(self,copy,le):
        #Checking of each possible winning combination.
        return ((copy[7] == le and copy[8] == le and copy[9] == le) or #check horizontal top row 
            (copy[4] == le and copy[5] == le and copy[6] == le) or     #check horizontal middle row     
            (copy[1] == le and copy[2] == le and copy[3] == le) or     #check horizontal bottom row
            (copy[7] == le and copy[4] == le and copy[1] == le) or     #check vertical first column 
            (copy[8] == le and copy[5] == le and copy[2] == le) or     #check vertical second column     
            (copy[9] == le and copy[6] == le and copy[3] == le) or     #check vertical last column
            (copy[7] == le and copy[5] == le and copy[3] == le) or     #check diagonal 
        return ((copy[7] == le and copy[8] == le and copy[9] == le) or 
            (copy[4] == le and copy[5] == le and copy[6] == le) or 
            (copy[1] == le and copy[2] == le and copy[3] == le) or 
            (copy[7] == le and copy[4] == le and copy[1] == le) or 
            (copy[8] == le and copy[5] == le and copy[2] == le) or 
            (copy[9] == le and copy[6] == le and copy[3] == le) or 
            (copy[7] == le and copy[5] == le and copy[3] == le) or 
            (copy[9] == le and copy[5] == le and copy[1] == le)) 
                
    def getBoardCopy(self):
        dupboard=[]
        for i in self.theBoard:
            dupboard.append(i)
        return dupboard
    
    def isSpaceFree(self,copy,move):
        return copy[move] == '-'

    #loop through the board append all the possible moves and return one move amongst randomly    
    def chooseRandomMoveFromList(self,copy,movesList):
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(copy, i):
                possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    #get a move from computer while playing with AI           
    def getComputerMove(self,copy):
        tempcopy = copy[:] #creating a local copy because (refrence updates the copy with each for loop and wrong checking is done) 
        tempcopy = copy[:]
        #this is for checking if the computer can win if he does move in particular cell
        for i in range(1, 10):
            if self.isSpaceFree(tempcopy, i):
                tempcopy = self.makeMove(tempcopy, 'O', i)
                if self.isWinner(tempcopy, 'O'):
                    return i
            tempcopy = copy[:]

        #this is to check if the player will win in his next move, the computer will block this move    
        for i in range(1, 10):
            if self.isSpaceFree(tempcopy, i):
                tempcopy = self.makeMove(tempcopy, 'X', i)
                if self.isWinner(tempcopy, 'X'):
                    return i
            tempcopy = copy[:]

        #select random move if both the checks donot return the move    

        copy = self.getBoardCopy()    
        move = self.chooseRandomMoveFromList(copy, [1, 3, 7, 9])
        if move != None:
            return move
        if self.isSpaceFree(copy, 5): #center of the board
            return 5
        return self.chooseRandomMoveFromList(copy, [2, 4, 6, 8])
       
    def isBoardFull(self,copy):
        for i in range(1, 10):
            if self.isSpaceFree(copy,i):
                return False
        return True

    def initialize(self):
        self.screen.fill(self.black)
        self.theBoard = ['-']*10
        #Each square of the game grid is made by four lines of 10 pixel density each. 
        #The original rectangle function isnt used because it creates blurred pixels on the edges which is not visually attractive. 
        pygame.draw.rect(self.screen, self.color, pygame.Rect(10, 10, 100, 10))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(10, 10, 10, 100))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(100, 10, 10, 100))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(10, 100, 100, 10))

        pygame.draw.rect(self.screen, self.color, pygame.Rect(100, 10, 90, 10))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(100, 100, 90, 10))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(190, 10, 10, 100))

        pygame.draw.rect(self.screen, self.color, pygame.Rect(200, 10, 90, 10))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(200, 100, 90, 10))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(280, 10, 10, 100))

        pygame.draw.rect(self.screen, self.color, pygame.Rect(10, 100, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(100, 100, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(10, 190, 100, 10))

        pygame.draw.rect(self.screen, self.color, pygame.Rect(100, 100, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(190, 100, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(100, 190, 100, 10))

        pygame.draw.rect(self.screen, self.color, pygame.Rect(280, 100, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(280, 100, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(190, 190, 100, 10))

        pygame.draw.rect(self.screen, self.color, pygame.Rect(10, 190, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(100, 190, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(10, 280, 100, 10))

        pygame.draw.rect(self.screen, self.color, pygame.Rect(100, 190, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(190, 190, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(100, 280, 100, 10))

        pygame.draw.rect(self.screen, self.color, pygame.Rect(280, 190, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(280, 190, 10, 90))
        pygame.draw.rect(self.screen, self.color, pygame.Rect(190, 280, 100, 10)) 

    #while playing with AI this function is called to get the players and the commputer's move
    def nxt_turn1(self,position):
        flag = self.isSpaceFree(self.getBoardCopy(),position)
        if flag:
            self.makeMove(0,'X',position)
            if self.isWinner(self.getBoardCopy(),'X'):
                return 'Player'
            else:
                if self.isBoardFull(self.getBoardCopy()):
                    return 0
            self.makeMove(0,'O',self.getComputerMove(self.getBoardCopy()))
            if self.isWinner(self.getBoardCopy(),'O'):
                return 'Computer'
            else:
                if self.isBoardFull(self.getBoardCopy()):
                    return 0

        return 'ongoing'

    #while playing PvP mode this function is called to get both the player's move    
    def nxt_turn2(self,position):
        flag = self.isSpaceFree(self.getBoardCopy(),position)
        if flag:
            if(self.marker == 'X'):
                self.marker = 'O'
            elif(self.marker == 'O'):
                self.marker = 'X'
            self.makeMove(0,self.marker,position)
            if self.isWinner(self.getBoardCopy(),self.marker):
                if self.marker == 'X':
                    return 'Player1'
                if self.marker == 'O':
                    return 'Player2'
            else:
                if self.isBoardFull(self.getBoardCopy()):
                    return 0

        return 'ongoing'

    def display_game_over(self, winner):
        surface_size = self.screen.get_height()
        font = pygame.font.Font('freesansbold.ttf', surface_size / 8)
        if winner:
            text = '%s won!' % winner
        else:
            text = 'Draw!'
        text = font.render(text, True,(100,120,130), (200,220,230))
        rect = text.get_rect()
        rect.center = (surface_size / 2, surface_size / 2)
        self.screen.blit(text, rect)
        
    '''    
    The function calling is handled by pygame1.py file. 
    This menu is just the graphical interface required for the same. Hence, no function calling done.
    '''
    def first_menu(self,x,y):       

    def first_menu(self,x,y):       #The function calling is handled by pygame1.py file. This menu is just the graphical interface required for the same. Hence, no function calling done.
        self.screen.fill(self.white)
        surface_size = self.screen.get_height()
        font = pygame.font.Font('freesansbold.ttf', 45)
        font2 = pygame.font.Font('freesansbold.ttf', 35)
        font3 = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('TIC-TAC-TOE', True,self.black, self.white)
        rect = text.get_rect()
        rect.center = (150,20)
        self.screen.blit(text, rect)
        text5 = font3.render('GAME MODE', True,self.black, )
        rect5 = text5.get_rect()
        rect5.center = (150,80)
        self.screen.blit(text5, rect5)

        if 140 > x > 20 and 190 > y > 100:
            pygame.draw.rect(self.screen, self.bright_green,(20,100,120,90))
        else:
            pygame.draw.rect(self.screen, self.green,(20,100,120,90))
        if 280 > x > 160 and 190 > y > 100:
            pygame.draw.rect(self.screen, self.bright_green,(160,100,120,90))
        else:
            pygame.draw.rect(self.screen, self.green,(160,100,120,90))
        if 210 > x > 90 and 290 > y > 200:
            pygame.draw.rect(self.screen, self.bright_red,(90,200,120,90))
        else:
            pygame.draw.rect(self.screen, self.red,(90,200,120,90))
        
        text2 = font2.render('Vs. AI', True,self.black, )
        rect2 = text2.get_rect()
        rect2.center = (80,145)
        self.screen.blit(text2, rect2)
        text3 = font2.render('P v P', True,self.black, )
        rect3 = text3.get_rect()
        rect3.center = (220,145)
        self.screen.blit(text3, rect3)
        text4 = font2.render('Quit!', True,self.black, )
        rect4 = text4.get_rect()
        rect4.center = (150,245)
        self.screen.blit(text4, rect4) 

    #This menu is called after the game is over, it shows the result and ask whether the user wishes to play again or not
    def last_menu(self,player,x,y):
        self.screen.fill(self.white)
        surface_size = self.screen.get_height()
        font = pygame.font.Font('freesansbold.ttf', surface_size/8)
        if player:
            text = '%s won!' % player
        else:
            text = 'Draw!'
        text = font.render(text, True,self.black, self.white)
        rect = text.get_rect()
        rect.center = (surface_size / 2, 30)
        self.screen.blit(text, rect)

        text2 = font.render("Play Again?", True,self.black,self.white)
        rect2 = text2.get_rect()
        rect2.center = (surface_size/2,100)
        self.screen.blit(text2,rect2)
    
        text3 = font.render("Yes", True,self.black,self.green)
        text4 = font.render("No", True,self.black,self.red)
        
        if 125 > x > 25 and 275 > y > 200:
            text3 = font.render("Yes", True,self.black,self.bright_green)
            pygame.draw.rect(self.screen, self.bright_green,(25,200,100,75))
        else:
            pygame.draw.rect(self.screen, self.green,(25,200,100,75))
        if 275 > x > 175 and 275 > y > 200:
            text4 = font.render("No", True,self.black,self.bright_red)
            pygame.draw.rect(self.screen, self.bright_red,(175,200,100,75))
        else:
            pygame.draw.rect(self.screen, self.red,(175,200,100,75))
        self.screen.blit(text3, (40, 220))
        self.screen.blit(text4, (200, 220))