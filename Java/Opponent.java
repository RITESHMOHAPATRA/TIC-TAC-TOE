
public class Opponent {
	// Will return the index of the best move to make
	public int getMove(Board board) {
		Board boardCopy = board.copy();

		// Take middle if it's not taken
		if (boardCopy.spotAvailable(4)) {
			return 4;
			// Return index of corner if middle is taken by player
		} else if (boardCopy.getBoard()[4] == board.getPlayer() && 
				boardCopy.spotAvailable(2)) {
			return 2;
		}
		// Return index of first winning positon for computer
		int computerIndex = findWinPosition(boardCopy, board.getComputer());
		if (computerIndex != -1) {
			return computerIndex;
		}
		// Return index of first winning position for player
		int playerIndex = findWinPosition(boardCopy, board.getPlayer());
		if (playerIndex != -1) {
			return playerIndex;
		}
		// Return index of fork for computer
		computerIndex = findFork(boardCopy, board.getComputer(), 2);
		if (computerIndex != -1) {
			return computerIndex;
		}
		// Return index of best move against player's fork
		playerIndex = findFork(boardCopy, board.getPlayer(), 2);
		if (playerIndex != -1) {
			// Play two in a row to counter fork
			if (boardCopy.getBoard()[4] == boardCopy.getPlayer()) {

				return findFork(boardCopy, board.getComputer(), 1);
				// Play into fork position of player
			} else {
				return playerIndex;
			}
		}
		// Return index of opposite corners to player
		for (int i=0; i<boardCopy.getLength(); i+= 2) {
			if (boardCopy.getBoard()[i] == board.getPlayer() && 
					i != 4 && boardCopy.spotAvailable(8 - i)) {
				return 8 - i;
			}
		}
		// Return index of first available corner
		for (int i=0; i<boardCopy.getLength(); i+= 2) {
			if (i != 4 && boardCopy.spotAvailable(i)) {
				return i;
			}
		}
		// Return index of first open spot
		for (int i=0; i<boardCopy.getLength(); i++) {
			if (boardCopy.spotAvailable(i)) {
				return i;
			}
		}
		return -1;
	}
	// Returns index of first position that wins the game for piece
	public int findWinPosition(Board board, char piece) {
		Board boardCopy = board.copy();
		Board newBoardCopy;

		// Return index of first winning spot for piece
		for (int i=0; i<boardCopy.getLength(); i++) {
			newBoardCopy = boardCopy.copy();
			if (newBoardCopy.spotAvailable(i)) {
				newBoardCopy.newPiece(piece, i);
				if (newBoardCopy.isWinner(piece) == true) {
					return i;
				}
			}
		}
		// No win position found
		return -1;
	}
	// Return index of position that leads to a particular number of possible 
	// wins on the next turn (Only works with 1 or 2 wins)
	public int findFork(Board board, char piece, int wins) {
		Board boardCopy = board.copy();
		Board newBoardCopy;
		Board newBoardCopy2;

		int totalWins;

		for (int i=0; i<boardCopy.getLength(); i++) {
			totalWins = 0;
			newBoardCopy = boardCopy.copy();
			if (newBoardCopy.spotAvailable(i)) {
				newBoardCopy.newPiece(piece, i);
			}
			for (int j=0; j<boardCopy.getLength(); j++) {
				newBoardCopy2 = newBoardCopy.copy();
				if (newBoardCopy2.spotAvailable(j)) {
					newBoardCopy2.newPiece(piece, j);
					if (newBoardCopy2.isWinner(piece)) {
						totalWins++;
					}
					if (totalWins >= wins) {
						return i;
					}
				}
			}
		}
		return -1;
	}
}
