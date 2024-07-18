import tkinter as tk
from Board import Board  # Ensure Board class has required methods
from minimax import Minimax  # Ensure Minimax is implemented correctly
from player import Player  # Ensure Player class has necessary attributes
import random

class Game:
    def __init__(self, root, rows, cols, player1, player2):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.board = Board(root, rows, cols)
        self.player1 = player1
        self.player2 = player2
        self.min_player = player1
        self.max_player = player2
        self.current_player = random.choice([player1, player2])  # Randomly select starting player
        self.starting_player = self.current_player  # Track who started the game
        self.minimax = Minimax(self)
        self.root.title(f"{self.current_player}'s turn")
        self.board.canvas.bind("<Button-1>", self.on_click)
        self.root.resizable(False, False)
        
        # If computer starts, make the first move
        if self.current_player == self.player2:
            self.root.after(100, self.make_computer_move)

    def on_click(self, event):
        if self.current_player == self.player1:
            self.make_move(self.player1, event)

    def make_move(self, player, event):
        row, col = self.get_clicked_cell(event)
        if self.board.board[row][col] == " ":
            self.board.draw(row, col, player.symbol)
            self.board.board[row][col] = player.symbol
            if self.is_winner(self.board.board, player):
                self.end_game(player)
            elif self.is_tie():
                self.end_game(None)
            else:
                self.current_player = self.player2
                self.root.title(f"{self.current_player}'s turn")
                self.root.after(100, self.make_computer_move)

    def make_computer_move(self):
        depth = len(self.get_moves(self.board.board))
        if depth == 9:
            move = random.choice(self.get_moves(self.board.board))
        else:
            move = self.minimax.get_best_move(self.board.board, depth, self.current_player)
        if move is not None:
            row, col = move
            self.board.draw(row, col, self.current_player.symbol)
            self.board.board[row][col] = self.current_player.symbol
            if self.is_winner(self.board.board, self.current_player):
                self.end_game(self.current_player)
            elif self.is_tie():
                self.end_game(None)
            else:
                self.current_player = self.player1
                self.root.title(f"{self.current_player}'s turn")
        else:
            print("No valid move returned by Minimax")

    def is_winner(self, state, player):
        return self.board.is_winner(state, player)

    def is_tie(self):
        return self.board.is_full() and self.board.evaluate() == 0

    def end_game(self, winner):
        if winner is None:
            self.root.title("It's a tie!")
            self.board.canvas.create_text(self.board.canvas.winfo_width() // 2, self.board.canvas.winfo_height() // 2, text="It's a tie!", font=("Helvetica", 32), fill="yellow", tags="tie")
        else:
            self.root.title(f"{winner} wins!")
            self.board.highlight_winner()
            self.board.canvas.create_text(self.board.canvas.winfo_width() // 2, self.board.canvas.winfo_height() // 2, text=f"{winner} wins!", font=("Helvetica", 32), fill="yellow", tags="winner")
        self.board.canvas.unbind("<Button-1>")
        self.board.canvas.bind("<Button-1>", self.restart_game)

    def restart_game(self, event):
        self.board.canvas.delete("restart")
        self.board.clear_board()
        self.board.canvas.bind("<Button-1>", self.on_click)
        # Switch starting player for next game
        self.current_player = self.player2 if self.starting_player == self.player1 else self.player1
        self.starting_player = self.current_player
        self.root.title(f"{self.current_player}'s turn")
        if self.current_player == self.player2:
            self.root.after(100, self.make_computer_move)

    def get_clicked_cell(self, event):
        width = self.board.canvas.winfo_width()
        height = self.board.canvas.winfo_height()
        cell_size = min(width // self.cols, height // self.rows)
        col = event.x // cell_size
        row = event.y // cell_size
        return row, col

    def get_moves(self, state):
        # Calculate available moves from current state
        moves = []
        for row in range(self.rows):
            for col in range(self.cols):
                if state[row][col] == " ":
                    moves.append((row, col))
        return moves

    def apply_move(self, state, move, player):
        row, col = move
        new_state = [row[:] for row in state]
        new_state[row][col] = player.symbol
        return new_state

    def evaluate(self, state, player):
        if self.is_winner(state, player):
            return 1
        elif self.is_winner(state, self.get_opponent(player)):
            return -1
        else:
            return 0

    def get_opponent(self, player):
        return self.player1 if player == self.player2 else self.player2

    def is_over(self, state):
        return self.board.is_winner(state, self.player1) or self.board.is_winner(state, self.player2) or self.board.is_full()

    def print_board(self):
        self.board.print_board()

    def highlight_winner(self):
        self.board.highlight_winner()

if __name__ == "__main__":
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    width = 300
    height = 300

    center_x = (screen_width - width) // 2
    center_y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{center_x}+{center_y}")

    root.title("Tic Tac Toe")
    
    game = Game(root, 3, 3, Player(1, "O"), Player(2, "X"))
    root.mainloop()
