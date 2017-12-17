 #!/usr/bin/env python

import random
import pygame


class Tic(object):
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])

    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self, squares=[]):
        # if len(squares) == 0:
        #     self.squares = [None for i in range(9)]
        # else:
        #     self.squares = squares
        self.screen = pygame.display.set_mode((300, 300))
        self.color = (100, 100, 200)
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (200,0,0)
        self.green = (0,200,0)
        self.bright_red = (255,0,0)
        self.bright_green = (0,255,0) 

    def update_surface(self,letter,position):
        #All the X's and O's carefully set to be in the center of their respective boxes.
        #O's are basic circles whereas X's are combination of two lines for better visual effect.
        if letter == 'X':
            if(position == 7):
                pygame.draw.line(self.screen, self.bright_green, (30, 210), (90, 270), 10)
                pygame.draw.line(self.screen, self.bright_green, (30, 270), (90, 210), 10)
            if(position == 8):
                pygame.draw.line(self.screen, self.bright_green, (120, 210), (180, 270), 10)
                pygame.draw.line(self.screen, self.bright_green, (120, 270), (180, 210), 10)
            if(position == 9):
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
            if(position == 1):
                pygame.draw.line(self.screen, self.bright_green, (30, 30), (90, 90), 10)
                pygame.draw.line(self.screen, self.bright_green, (30, 90), (90, 30), 10)
            if(position == 2):
                pygame.draw.line(self.screen, self.bright_green, (120, 30), (180, 90), 10)
                pygame.draw.line(self.screen, self.bright_green, (120, 90), (180, 30), 10)
            if(position == 3):
                pygame.draw.line(self.screen, self.bright_green, (210, 30), (270, 90), 10)
                pygame.draw.line(self.screen, self.bright_green, (210, 90), (270, 30), 10)
        if letter == 'O':
            if(position == 7):
                pygame.draw.circle(self.screen,self.bright_red, (60,240), 30)
            if(position == 8):
                pygame.draw.circle(self.screen,self.bright_red, (150,240), 30)
            if(position == 9):
                pygame.draw.circle(self.screen,self.bright_red, (240,240), 30)
            if(position == 4):
                pygame.draw.circle(self.screen,self.bright_red, (60,150), 30)
            if(position == 5):
                pygame.draw.circle(self.screen,self.bright_red, (150,150), 30)
            if(position == 6):
                pygame.draw.circle(self.screen,self.bright_red, (240,150), 30)
            if(position == 1):
                pygame.draw.circle(self.screen,self.bright_red, (60,60), 30)
            if(position == 2):
                pygame.draw.circle(self.screen,self.bright_red, (150,60), 30)
            if(position == 3):
                pygame.draw.circle(self.screen,self.bright_red, (240,60), 30)    

    def initialize(self):
        self.screen.fill(self.black)

        self.squares = [None for i in range(9)]

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

    def show(self):
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print(element)

    def available_moves(self):
        """what spots are left empty?"""
        return [k for k, v in enumerate(self.squares) if v is None]

    def available_combos(self, player):
        """what combos are available?"""
        return self.available_moves() + self.get_squares(player)

    def complete(self):
        """is the game over?"""
        if None not in [v for v in self.squares]:
            return True
        if self.winner() != None:
            return True
        return False

    def X_won(self):
        return self.winner() == 'X'

    def O_won(self):
        return self.winner() == 'O'

    def tied(self):
        return self.complete() == True and self.winner() is None

    def winner(self):
        for player in ('X', 'O'):
            positions = self.get_squares(player)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def get_squares(self, player):
        """squares that belong to a player"""
        return [k for k, v in enumerate(self.squares) if v == player]

    def make_move(self, position, player):
        """place on square on the board"""
        self.squares[position] = player

    def alphabeta(self, node, player, alpha, beta):
        if node.complete():
            if node.X_won():
                return -1
            elif node.tied():
                return 0
            elif node.O_won():
                return 1
        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta(node, get_enemy(player), alpha, beta)
            node.make_move(move, None)
            if player == 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == 'O':
            return alpha
        else:
            return beta


def determine(board, player):
    a = -2
    choices = []
    if len(board.available_moves()) == 9:
        return 4
    for move in board.available_moves():
        board.make_move(move, player)
        val = board.alphabeta(board, get_enemy(player), -2, 2)
        board.make_move(move, None)
        # print("move:", move + 1, "causes:", board.winners[val + 1])
        if val > a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)
    return random.choice(choices)


def get_enemy(player):
    if player == 'X':
        return 'O'
    return 'X'

def nxt_turn1(key,board):
    
    player = 'X'
    player_move = key - 1
    if not player_move in board.available_moves():
        return 'ongoing'
    board.make_move(player_move, player)
    # board.show()
    board.update_surface(player,player_move+1)

    if board.complete():
        if board.winner()!= None:
            return board.winner()
        else:
            return 'Draw'

    player = get_enemy(player)
    computer_move = determine(board, player)
    board.make_move(computer_move, player)
    board.update_surface(player,computer_move+1)
    # board.show()
        # board.show()
    if board.complete():
        if board.winner()!= None:
            if board.winner() ==  'X':
                return 'Player'
            if board.winner() == 'O':
                return 'Computer'
        else:
            return 'Draw'

    return 'ongoing'