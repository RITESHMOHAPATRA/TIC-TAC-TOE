using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Random random = new Random();
        string[,] board = new string[3, 3] { { "0", "0", "0" }, { "0", "0", "0" }, { "0", "0", "0" } };
        public Form1()
        {
            InitializeComponent();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void tableLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private bool checkifcomplete()
        {
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (board[i, j] == "0")
                    {
                        return false;
                    }
                }
            }
            //MessageBox.Show("complete");
            return true;
        }

        private string aiplay(string[,] tempboard, char player)
        {
            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    if (board[i, j] == "0")
                    {
                        if (player == 'c')
                        {
                            board[i, j] = "COMPUTER";
                            if (aiplay(board, 'u') != "NULL")
                            {
                                board[i, j] = "0";
                            }
                            else
                            {
                                board[i, j] = "COMPUTER";
                                setthebox(i, j);
                                return "done";
                            }
                        }
                        else if (player == 'u')
                        {
                            board[i, j] = "USER";
                            if (checkifuserwon() == true)
                            {
                                board[i, j] = "0";
                                return "iamwinning";
                                //return (i.ToString() + j.ToString());
                            }
                            else
                            {
                                board[i, j] = "0";
                            }
                        }
                    }
                }
            }
            return "NULL";
        }

        private void setthebox(int randrow, int randcol)
        {
            if (randrow == 0 && randcol == 0)
                button00.Text = "0";
            if (randrow == 0 && randcol == 1)
                button01.Text = "0";
            if (randrow == 0 && randcol == 2)
                button02.Text = "0";
            if (randrow == 1 && randcol == 0)
                button10.Text = "0";
            if (randrow == 1 && randcol == 1)
                button11.Text = "0";
            if (randrow == 1 && randcol == 2)
                button12.Text = "0";
            if (randrow == 2 && randcol == 0)
                button20.Text = "0";
            if (randrow == 2 && randcol == 1)
                button21.Text = "0";
            if (randrow == 2 && randcol == 2)
                button22.Text = "0";
        }

        private void computerplay()
        {
            //MessageBox.Show("computerplay");
            string chosen;
            int randrow, randcol;
            do
            {
                randrow = random.Next(0, 3);
                randcol = random.Next(0, 3);
                //MessageBox.Show(randrow.ToString());
                chosen = board[randrow, randcol];
                //MessageBox.Show(chosen);
            }
            while (chosen != "0");

            board[randrow, randcol] = "COMPUTER";

            setthebox(randrow, randcol);
        }

        private bool checkifuserwon()
        {
            for (int i = 0; i < 3; i++)
            {
                if ((board[i, 0] == "USER") && (board[i, 1] == "USER") && (board[i, 2] == "USER"))
                    return true;
            }
            for (int i = 0; i < 3; i++)
            {
                if ((board[0, i] == "USER") && (board[1, i] == "USER") && (board[2, i] == "USER"))
                    return true;
            }
            if ((board[0, 0] == "USER") && (board[1, 1] == "USER") && (board[2, 2] == "USER"))
                return true;
            if ((board[0, 2] == "USER") && (board[1, 1] == "USER") && (board[2, 0] == "USER"))
                return true;
            return false;
        }

        private bool checkifcompwon()
        {
            for (int i = 0; i < 3; i++)
            {
                if ((board[i, 0] == "COMPUTER") && (board[i, 1] == "COMPUTER") && (board[i, 2] == "COMPUTER"))
                    return true;
            }
            for (int i = 0; i < 3; i++)
            {
                if ((board[0, i] == "COMPUTER") && (board[1, i] == "COMPUTER") && (board[2, i] == "COMPUTER"))
                    return true;
            }
            if ((board[0, 0] == "COMPUTER") && (board[1, 1] == "COMPUTER") && (board[2, 2] == "COMPUTER"))
                return true;
            if ((board[0, 2] == "COMPUTER") && (board[1, 1] == "COMPUTER") && (board[2, 0] == "COMPUTER"))
                return true;
            return false;
        }

        private void button00_Click(object sender, EventArgs e)
        {
            button00.Text = "X";
            board[0, 0] = "USER";

            if (checkifuserwon() == true)
            {
                MessageBox.Show("USER WON!");
                System.Windows.Forms.Application.Exit();
            }

            if (checkifcomplete() == false)
            {
                //computerplay();
                aiplay(board, 'c');
                if (checkifcompwon() == true)
                {
                    MessageBox.Show("COMPUTER WON!");
                    System.Windows.Forms.Application.Exit();
                }
            }
            else
            {
                MessageBox.Show("Game complete");
            }
        }

        private void button01_Click_1(object sender, EventArgs e)
        {
            button01.Text = "X";
            board[0, 1] = "USER";

            if (checkifuserwon() == true)
            {
                MessageBox.Show("USER WON!");
                System.Windows.Forms.Application.Exit();
            }

            if (checkifcomplete() == false)
            {
                aiplay(board, 'c');
                if (checkifcompwon() == true)
                {
                    MessageBox.Show("COMPUTER WON!");
                    System.Windows.Forms.Application.Exit();
                }
            }
            else
            {
                MessageBox.Show("Game complete");
            }
        }

        private void button02_Click_1(object sender, EventArgs e)
        {
            button02.Text = "X";
            board[0, 2] = "USER";

            if (checkifuserwon() == true)
            {
                MessageBox.Show("USER WON!");
                System.Windows.Forms.Application.Exit();
            }
            if (checkifcomplete() == false)
            {
                aiplay(board, 'c');
                if (checkifcompwon() == true)
                {
                    MessageBox.Show("COMPUTER WON!");
                    System.Windows.Forms.Application.Exit();
                }
            }
            else
            {
                MessageBox.Show("Game complete");
            }
        }

        private void button10_Click_1(object sender, EventArgs e)
        {
            button10.Text = "X";
            board[1, 0] = "USER";

            if (checkifuserwon() == true)
            {
                MessageBox.Show("USER WON!");
                System.Windows.Forms.Application.Exit();
            }
            if (checkifcomplete() == false)
            {
                aiplay(board, 'c');
                if (checkifcompwon() == true)
                {
                    MessageBox.Show("COMPUTER WON!");
                    System.Windows.Forms.Application.Exit();
                }
            }
            else
            {
                MessageBox.Show("Game complete");
            }
        }

        private void button11_Click_1(object sender, EventArgs e)
        {
            button11.Text = "X";
            board[1, 1] = "USER";

            if (checkifuserwon() == true)
            {
                MessageBox.Show("USER WON!");
                System.Windows.Forms.Application.Exit();
            }
            if (checkifcomplete() == false)
            {
                aiplay(board, 'c');
                if (checkifcompwon() == true)
                {
                    MessageBox.Show("COMPUTER WON!");
                    System.Windows.Forms.Application.Exit();
                }
            }
            else
            {
                MessageBox.Show("Game complete");
            }
        }

        private void button12_Click_1(object sender, EventArgs e)
        {
            button12.Text = "X";
            board[1, 2] = "USER";

            if (checkifuserwon() == true)
            {
                MessageBox.Show("USER WON!");
                System.Windows.Forms.Application.Exit();
            }
            if (checkifcomplete() == false)
            {
                aiplay(board, 'c');
                if (checkifcompwon() == true)
                {
                    MessageBox.Show("COMPUTER WON!");
                    System.Windows.Forms.Application.Exit();
                }
            }
            else
            {
                MessageBox.Show("Game complete");
            }
        }

        private void button20_Click_1(object sender, EventArgs e)
        {
            button20.Text = "X";
            board[2, 0] = "USER";

            if (checkifuserwon() == true)
            {
                MessageBox.Show("USER WON!");
                System.Windows.Forms.Application.Exit();
            }
            if (checkifcomplete() == false)
            {
                aiplay(board, 'c');
                if (checkifcompwon() == true)
                {
                    MessageBox.Show("COMPUTER WON!");
                    System.Windows.Forms.Application.Exit();
                }
            }
            else
            {
                MessageBox.Show("Game complete");
            }
        }

        private void button21_Click_1(object sender, EventArgs e)
        {
            button21.Text = "X";
            board[2, 1] = "USER";

            if (checkifuserwon() == true)
            {
                MessageBox.Show("USER WON!");
                System.Windows.Forms.Application.Exit();
            }
            if (checkifcomplete() == false)
            {
                aiplay(board, 'c');
                if (checkifcompwon() == true)
                {
                    MessageBox.Show("COMPUTER WON!");
                    System.Windows.Forms.Application.Exit();
                }
            }
            else
            {
                MessageBox.Show("Game complete");
            }
        }

        private void button22_Click_1(object sender, EventArgs e)
        {
            button22.Text = "X";
            board[2, 2] = "USER";

            if (checkifuserwon() == true)
            {
                MessageBox.Show("USER WON!");
                System.Windows.Forms.Application.Exit();
            }
            if (checkifcomplete() == false)
            {
                aiplay(board, 'c');
                if (checkifcompwon() == true)
                {
                    MessageBox.Show("COMPUTER WON!");
                    System.Windows.Forms.Application.Exit();
                }
            }
            else
            {
                MessageBox.Show("Game complete");
            }
        }

    }
}
