import random
from tkinter import *
import tkinter.font as tkFont
import tkinter.simpledialog as sd
from tkinter import messagebox


class TicTacToe:

    def __init__(self,master):

        # This list is storing the moves. If the value is 0 then its empty and value 1 then its user move
        # and when value 2 then its move by computer


        self.root = master

        master.minsize(width = 400,height = 400)
        #master.maxsize(width = 1000,height = 1000)
        self.frame = Frame(master)
        self.frame.pack()
        self.bframe = Frame(master)

        self.customFont = tkFont.Font(family="Helvetica",slant = tkFont.ITALIC,size=12)
        self.b_hello = Button(self.frame,text = "Start Game",fg = "white",bg = "blue",font = self.customFont,command = self.startGame)
        self.b_hello.pack(side = LEFT)
        self.b_quit = Button(self.frame,text = "Quit Game",fg = "white",bg = "blue",font = self.customFont,command = self.frame.quit)
        self.b_quit.pack(side = LEFT,padx = 30)

    def startGame(self):

        self.moves = [0]*10
        #print("moves:",len(self.moves))
        self.moves[0] = -1 # As we are not going to use this
        
        self.can = Canvas(root,width = 200,height = 200)
        self.can.pack(side = TOP)

        # Draw the board
        self.drawboard()

        # Ask the user for its choice
        self.inputPlayerLetter()

        turn = self.whoGoesFirst()
        self.ongoingGame = True
        while self.ongoingGame:
            #print(turn)
            if(turn == 'user'):
                self.userMove()
                if(self.isWinner(self.moves,1)):
                    messagebox.showinfo("Win", "Hurray! You won the game..")
                    self.ongoingGame = False
                else:
                    if(self.isBoardFull()):
                        messagebox.info("tie","The game is a tie ..")
                        self.ongoingGame = False
                    else:
                        turn = 'computer'
            else:
                move = self.getComputerMove() # This is the cell for computer
                i,j = self.returnPos(move)
                self.can.create_text(i,j,text = self.computer_choice)
                self.moves[move] = 2

                if(self.isWinner(self.moves,2)):
                    messagebox.showinfo("Defeat","You Lost!")
                    self.ongoingGame = False
                else:
                    if(self.isBoardFull()):
                        messagebox.showinfo("tie" ,"The game is a tie ..")
                        self.ongoingGame = False
                    else:
                        turn = 'user'

    def drawboard(self):
        for i in range(1,4):
            for j in range(1,4):
                self.can.create_rectangle(30 * j,30 * i,30 * (j + 1),30 * (i+1))

    def inputPlayerLetter(self):
        var = messagebox.askquestion("Your choice","Press Yes for 'X' and press No for 'O' ")
        if(var == 'yes'):
            self.user_choice = 'X'
            self.computer_choice = 'O'
        else:
            self.user_choice = 'O'
            self.computer_choice = 'X'

    def whoGoesFirst(self):
        if(random.randint(0,1) == 0):
            return 'computer'
        else:
            return 'user'

    def makeMove(self,cellno,moveBy,c_moves):
        # moveBy val 1 indicates user move and val 2 indicates computer move
        c_moves[cellno] = moveBy


    def isWinner(self,c_move,num):
        return ((c_move[1] == num and c_move[2] == num and c_move[3] == num) or # across the top
            (c_move[4] == num and c_move[5] == num and c_move[6] == num) or # across the middle
            (c_move[7] == num and c_move[8] == num and c_move[9] == num) or # across the movesttom
            (c_move[1] == num and c_move[4] == num and c_move[7] == num) or # down the left side
            (c_move[8] == num and c_move[5] == num and c_move[2] == num) or # down the middle
            (c_move[3] == num and c_move[6] == num and c_move[9] == num) or # down the right side
            (c_move[1] == num and c_move[5] == num and c_move[9] == num) or # diagonal
            (c_move[3] == num and c_move[5] == num and c_move[7] == num)) # diagonal

    def getCopyOfMoves(self):
        copy_moves = []
        for i in range(0,10):
            copy_moves.append(self.moves[i])
        #print("Copy Moves:",len(copy_moves))
        return copy_moves


    def isSpaceFree(self,moves,pos):
        return moves[pos] == 0


    def returnPos(self,cellno):
        if(cellno >= 1 and cellno <= 3):
            i = 1
            j = cellno
        elif(cellno >= 4 and cellno <= 6):
            i = 2
            j = cellno % 3
            if(j == 0):
                j = 3
        else:
            i = 3
            j = cellno % 3
            if(j == 0):
                j = 3

        posX = 0.5 * (30 * j + 30 * (j + 1))
        posY = 0.5 * (30 * i + 30 * (i + 1))
        return(posX,posY)

    def userMove(self):
        pos = sd.askinteger('','Enter the position',initialvalue = 1,minvalue = 1,maxvalue = 9)

        if type(pos) is int:
            if(self.isSpaceFree(self.moves,pos)):
                i,j = self.returnPos(pos)
                self.can.create_text(i,j,text = self.user_choice)
                self.moves[pos] = 1
            else:
                messagebox.showerror(message = "Cell already occupied")
                self.userMove()
        else:
            self.ongoingGame = False


    def chooseRandomMoveFromList(self,moveslist):
        possible_moves = []
        for i in moveslist:
            if(self.isSpaceFree(self.moves,i)):
                possible_moves.append(i)
        if len(possible_moves) > 0:
            return random.choice(possible_moves)
        else:
            return None

    def getComputerMove(self):

        copy_moves = self.getCopyOfMoves()
        # We should not allow this
        for i in range(1, 10):
            if self.isSpaceFree(copy_moves,i):
                self.makeMove(i,2,copy_moves) #self,cellno,moveBy,c_moves
                if self.isWinner(copy_moves,1):
                    return i
        # If we can win then we should go for it

        for i in range(1,len(self.moves)):
            if self.isSpaceFree(copy_moves,i):
                self.makeMove(i,2,copy_moves)
                if self.isWinner(copy_moves,2):
                    return i

        ## We have to move on
        move = self.chooseRandomMoveFromList([1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if self.isSpaceFree(self.moves,5):
            return 5

        # Move on one of the sides.
        return self.chooseRandomMoveFromList([2, 4, 6, 8])


    def isBoardFull(self):
        if 0 not in self.moves:
            return True
        return False


root  = Tk()
test = TicTacToe(root)
root.mainloop();
