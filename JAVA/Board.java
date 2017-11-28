
public class Board {
	// The Tic Tac Toe board filled with the pieces
	private char[] board = {' ',' ',' ',
			' ',' ',' ',
			' ',' ',' '};

	// Character used for the player pieces (X/O)
	private char player;
	private char computer;

	public Board(char player, char computer) {
		this.player = player;
		this.computer = computer;
	}
	public char getPlayer() {
		return this.player;
	}
	public char getComputer() {
		return this.computer;
	}	
	public char[] getBoard() {
		return this.board;
	}
	public int getLength() {
		return this.board.length;
	}
	public void reset() {
		for (int i=0; i<this.board.length; i++) {
			this.board[i] = ' ';
		}
	}
	// Will place piece into the board at boardPosition
	public void newPiece(char piece, int position) {
		this.board[position] = piece;
	}
	// Return true if the position on the board is available
	public boolean spotAvailable(int position) {
		return this.board[position] != this.player && 
				this.board[position] != this.computer;
	}	
	// Return true if piece is the winner of the game
	public boolean isWinner(char piece) {
		for (int i=0;i<3;i++) {
			// Check for horizontal and vertical wins
			if (this.board[3*i] == piece && this.board[3*i+1] == piece && 
					this.board[3*i+2] == piece || this.board[i] == piece && 
					this.board[i+3] == piece && this.board[i+6] == piece) {
				return true;	
			}
		}
		// Check for diagonal wins
		if (this.board[2] == piece && this.board[4] == piece && 
				this.board[6] == piece || this.board[0] == piece && 
				this.board[4] == piece && this.board[8] == piece) {
			return true;

		}
		return false;
	}
	// Create a copy of the TicTacToe object in it's current state
	public Board copy() {
		Board newBoard = new Board(this.player, this.computer);
		for (int i=0; i<this.board.length; i++) {
			newBoard.board[i] = this.board[i];
		}
		return newBoard;
	}
	// Used for printing the board in the display of a standard board
	// whilst debugging
	public String toString() {
		String boardString = "\n";
		for (int i=0; i<this.board.length; i++) {
			boardString += " " + this.board[i];

			if (i % 3 == 2 && i != this.board.length - 1) {
				boardString += "\n" + "---|---|---\n";
			} else  if (i != this.board.length - 1){
				boardString += " |";
			}
		}
		return boardString;
	}
}
