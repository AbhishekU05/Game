import tkinter as tk
import random

class TicTacToe:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # Create the buttons for the game board
        self.buttons = []
        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(self.root, width=10, height=4, font=("Arial", 20),  command=lambda row=i, col=j: self.play(row, col))
                button.grid(row=i, column=j)
                button_row.append(button)
            self.buttons.append(button_row)

        # Create a label for displaying the game status
        self.status_label = tk.Label(self.root, text="User's turn", font=("Arial", 20))
        self.status_label.grid(row=3, column=0, columnspan=3)

        # Create a label for displaying the scores
        self.score_label = tk.Label(self.root, text="User: 0  Computer: 0", font=("Arial", 20))
        self.score_label.grid(row=4, column=0, columnspan=3)

        # Create a restart button
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart, font = ("Arial",20))
        self.restart_button.grid(row=5, column=0, columnspan=3)

        # Initialize the game variables
        self.player = 1
        self.game_over = False
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.scores = [0, 0]

        # Start the main loop
        self.root.mainloop()

    def play(self, row, col):
        if self.game_over or self.board[row][col] != 0:
            return

        # Update the game board
        self.board[row][col] = self.player
        self.buttons[row][col]['text'] = 'X' if self.player == 1 else 'O'

        # Check for a win
        if self.check_win():
            if self.player ==1:
                self.status_label['text'] = "User wins!".format(self.player)
                self.scores[self.player - 1] += 1
                self.update_scores()
            elif self.player == 2:
                self.status_label['text'] = "Computer Wins!".format(self.player)
                self.scores[self.player - 1] += 1
                self.update_scores()
                #print(self.scores[0],self.scores[1])
            self.game_over = True
            return

        # Check for a draw
        if self.check_draw():
            self.status_label['text'] = "It's a draw!"
            self.game_over = True
            return

        # Switch to the other player
        if self.player == 1:
            self.player = 2
            self.computer_play()
        else:
            self.player = 1
            self.status_label['text'] = ""

    def computer_play(self):
        if self.game_over:
            return

        available_positions = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]
        computer_choice = random.choice(available_positions)
        self.play(computer_choice[0], computer_choice[1])

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != 0:
                if self.player == 2:
                    self.status_label['text'] = "Computer wins!"
                    self.update_scores()

                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != 0:
                if self.player == 2:
                    self.status_label['text'] = "Computer wins!"
                    self.update_scores()

                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != 0:
            if self.player == 2:
                self.status_label['text'] = "Computer wins!"
                self.update_scores()

            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != 0:
            if self.player == 2:
                self.status_label['text'] = "Computer wins!"
                self.update_scores()

            return True
        return False

    def check_draw(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def update_scores(self):
        self.score_label['text'] = "User: {}  Computer: {}".format(self.scores[0], self.scores[1])

    def restart(self):
        self.player = 1
        self.game_over = False
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        #self.scores = [0, 0]
        self.status_label['text'] = "User's turn"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""


if __name__ == '__main__':
    game = TicTacToe()
