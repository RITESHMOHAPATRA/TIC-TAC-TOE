# -*- coding: utf-8 -*-      
import random
import pygame

class Board(object):    
    def __init__(self):
        self.theBoard = ['-']*10
        self.screen = pygame.display.set_mode((300, 300))
        self.color = (100, 100, 200)
        self.color1 = (100,200,100)
        self.color2 = (200,100,100)

    def makeMove(self,copy,letter, position):
        if not copy:
            self.theBoard[position] = letter
            self.update_surface(letter,position)
        else:
            copy[position] = letter
            return copy
                
    def update_surface(self,letter,position):
        if letter == 'X':
            if(position == 1):
                pygame.draw.line(self.screen, self.color1, (30, 210), (90, 270), 10)
                pygame.draw.line(self.screen, self.color1, (30, 270), (90, 210), 10)
            if(position == 2):
                pygame.draw.line(self.screen, self.color1, (120, 210), (180, 270), 10)
                pygame.draw.line(self.screen, self.color1, (120, 270), (180, 210), 10)
            if(position == 3):
                pygame.draw.line(self.screen, self.color1, (210, 210), (270, 270), 10)
                pygame.draw.line(self.screen, self.color1, (210, 270), (270, 210), 10)
            if(position == 4):
                pygame.draw.line(self.screen, self.color1, (30, 120), (90, 180), 10)
                pygame.draw.line(self.screen, self.color1, (30, 180), (90, 120), 10)   
            if(position == 5):
                pygame.draw.line(self.screen, self.color1, (120, 120), (180, 180), 10)
                pygame.draw.line(self.screen, self.color1, (120, 180), (180, 120), 10)
            if(position == 6):
                pygame.draw.line(self.screen, self.color1, (210, 120), (270, 180), 10)
                pygame.draw.line(self.screen, self.color1, (210, 180), (270, 120), 10)
            if(position == 7):
                pygame.draw.line(self.screen, self.color1, (30, 30), (90, 90), 10)
                pygame.draw.line(self.screen, self.color1, (30, 90), (90, 30), 10)
            if(position == 8):
                pygame.draw.line(self.screen, self.color1, (120, 30), (180, 90), 10)
                pygame.draw.line(self.screen, self.color1, (120, 90), (180, 30), 10)
            if(position == 9):
                pygame.draw.line(self.screen, self.color1, (210, 30), (270, 90), 10)
                pygame.draw.line(self.screen, self.color1, (210, 90), (270, 30), 10)
        if letter == 'O':
            if(position == 1):
                pygame.draw.circle(self.screen,self.color2, (60,240), 30)
            if(position == 2):
                pygame.draw.circle(self.screen,self.color2, (150,240), 30)
            if(position == 3):
                pygame.draw.circle(self.screen,self.color2, (240,240), 30)
            if(position == 4):
                pygame.draw.circle(self.screen,self.color2, (60,150), 30)
            if(position == 5):
                pygame.draw.circle(self.screen,self.color2, (150,150), 30)
            if(position == 6):
                pygame.draw.circle(self.screen,self.color2, (240,150), 30)
            if(position == 7):
                pygame.draw.circle(self.screen,self.color2, (60,60), 30)
            if(position == 8):
                pygame.draw.circle(self.screen,self.color2, (150,60), 30)
            if(position == 9):
                pygame.draw.circle(self.screen,self.color2, (240,60), 30)    

    def isWinner(self,copy,le):
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
       
    def chooseRandomMoveFromList(self,copy,movesList):
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(copy, i):
                possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None
               
    def getComputerMove(self,copy):
        for i in range(1, 10):
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, 'O', i)
                if self.isWinner(copy, 'O'):
                    return i
        copy = self.getBoardCopy()
        for i in range(1, 10):
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, 'X', i)
                if self.isWinner(copy, 'X'):
                    return i
        copy = self.getBoardCopy()    
        move = self.chooseRandomMoveFromList(copy, [1, 3, 7, 9])
        if move != None:
            return move
        if self.isSpaceFree(copy, 5):
            return 5
        return self.chooseRandomMoveFromList(copy, [2, 4, 6, 8])
   
    def isBoardFull(self,copy):
        for i in range(1, 10):
            if self.isSpaceFree(copy,i):
                return False
        return True

    def initialize(self):
        
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

    def nxt_turn(self,position):
        self.makeMove(0,'X',position)
        if self.isWinner(self.getBoardCopy(),'X'):
            self.display_game_over('Player')
            return
        else:
            if self.isBoardFull(self.getBoardCopy()):
                self.display_game_over(0)
                return
        self.makeMove(0,'O',self.getComputerMove(self.getBoardCopy()))
        if self.isWinner(self.getBoardCopy(),'O'):
            self.display_game_over('Computer')
            return
        else:
            if self.isBoardFull(self.getBoardCopy()):
                self.display_game_over(0)
                return

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

