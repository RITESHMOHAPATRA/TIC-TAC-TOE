import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class TicTacToeGUI extends JFrame {

	private static final long serialVersionUID = -5034718198692604252L;
	JButton[] boardButtons = new JButton[9];
	JButton resetButton = new JButton("Reset");
	JFrame frame = new JFrame("Mitch's Tic Tac Toe");

	Board board = new Board('X', 'O');
	Opponent opponent = new Opponent();

	public TicTacToeGUI() {
		frame.setSize(600, 600);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
		frame.setResizable(false);
	}
	private void initialise() {
		JPanel mainPanel = new JPanel(new BorderLayout());
		JPanel gameBoard = new JPanel(new GridLayout(3,3));		

		frame.add(mainPanel);

		gameBoard.setPreferredSize(new Dimension(500,500));

		mainPanel.add(gameBoard, BorderLayout.NORTH);
		mainPanel.add(resetButton);

		resetButton.addActionListener(new myActionListener());

		// Initialise all the buttons
		for(int i=0; i<9; i++) {
			boardButtons[i] = new JButton();
			boardButtons[i].setBackground(Color.BLUE);
			boardButtons[i].setText("");
			boardButtons[i].setVisible(true);

			gameBoard.add(boardButtons[i]); 
			boardButtons[i].addActionListener(new myActionListener());
			boardButtons[i].setFont(new Font("Tahoma", Font.BOLD, 100));
		}
	}
	// Listen for when the buttons are clicked
	private class myActionListener implements ActionListener {
		public void actionPerformed(ActionEvent action) {
			int computerMove;

			//Display the player's piece on the buttons
			for (int i=0; i<9; i++) {
				if (action.getSource() == boardButtons[i] && 
						board.spotAvailable(i)) {

					// Player turn
					board.newPiece(board.getPlayer(), i);
					boardButtons[i].setText(Character.toString(board.getPlayer()));
					boardButtons[i].setForeground(Color.GREEN);

					// If player has won, end game
					if (board.isWinner(board.getPlayer())) {
						gameOver();
					}

					// Computer turn
					computerMove = opponent.getMove(board);

					// If computer has a legal move
					if (computerMove != -1) {
						board.newPiece(board.getComputer(), computerMove);
						boardButtons[computerMove].setText(Character.toString(board.getComputer()));
						boardButtons[computerMove].setForeground(Color.YELLOW);

						// If computer has won, end game
						if (board.isWinner(board.getComputer())) {
							gameOver();
						}
						// Game was a tie
					} else {
						gameOver();
					}
				}
			}
			// When the reset button is clicked, reset the board & the display
			if(action.getSource() == resetButton) {
				for (int i=0; i<9; i++) { 
					boardButtons[i].setText(""); 
					boardButtons[i].setEnabled(true);
					frame.setTitle("Mitch's Tic Tac Toe");
				}
				board.reset();
			}
		}
	}
	// When the game is over, display any winners in the title
	public void gameOver() {
		for (int i=0; i<9; i++) {
			boardButtons[i].setEnabled(false);
		}
		if (board.isWinner(board.getPlayer())) {
			JOptionPane.showMessageDialog(frame, "CONGRATULATIONS! YOU WIN!");						
			frame.setTitle("Mitch's Tic Tac Toe: ***** PLAYER WINS *****");
		} else if (board.isWinner(board.getComputer())) {
			frame.setTitle("Mitch's Tic Tac Toe: ***** COMPUTER WINS *****");
			JOptionPane.showMessageDialog(frame, "Bad luck. You Lose.");						

		} else {
			JOptionPane.showMessageDialog(frame, "Draw.");						
			frame.setTitle("Mitch's Tic Tac Toe: ***** IT'S A DRAW *****");
		}
	}
	public static void main(String[] args) {
		TicTacToeGUI game = new TicTacToeGUI();
		game.initialise();
	}
}
