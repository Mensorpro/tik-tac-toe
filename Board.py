import tkinter as tk

class Board:
    
    WIDTH = 300
    HEIGHT = 300

    def __init__(self, root, rows, cols) -> None:
        self.root = root
        self.rows = rows
        self.cols = cols
        self.canvas = tk.Canvas(root, width=self.WIDTH, height=self.HEIGHT, bg="gray")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.create_grid)
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        self.available = [(row, col) for row in range(self.rows) for col in range(self.cols)]
        self.root.resizable(False, False)

    def create_grid(self, event=None):
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        cell_size = min(width // self.cols, height // self.rows)
        for x in range(0, width, cell_size):
            self.canvas.create_line(x, 0, x, height, fill="white")
        for y in range(0, height, cell_size):
            self.canvas.create_line(0, y, width, y, fill="white")

    def draw_circle(self, row, col):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        cell_size = min(width // self.cols, height // self.rows)
        diameter = cell_size * 0.6
        x = col * cell_size
        y = row * cell_size
        start_x = x + (cell_size - diameter) / 2
        start_y = y + (cell_size - diameter) / 2
        end_x = start_x + diameter
        end_y = start_y + diameter
        self.canvas.create_oval(start_x, start_y, end_x, end_y, outline="blue", width=5)

    def draw_cross(self, row, col):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        cell_size = min(width // self.cols, height // self.rows)
        line_length = cell_size * 0.6
        x = col * cell_size
        y = row * cell_size
        start_x = x + (cell_size - line_length) / 2
        end_x = start_x + line_length
        start_y = y + (cell_size - line_length) / 2
        end_y = start_y + line_length
        self.canvas.create_line(start_x, start_y, end_x, end_y, fill="red", width=5)
        self.canvas.create_line(start_x, end_y, end_x, start_y, fill="red", width=5)

    def draw(self, row, col, player):
        if self.board[row][col] != " ":
            self.canvas.create_text(self.WIDTH // 2, self.HEIGHT // 2, text="Invalid move", fill="yellow", font=("Arial", 24), tag="invalid")
            self.canvas.update()
            self.canvas.after(1000, self.canvas.delete, "invalid")
            return
        if (row, col) in self.available:
            if player == "X":
                self.draw_cross(row, col)
            elif player == "O":
                self.draw_circle(row, col)
            self.board[row][col] = player
            self.available.remove((row, col))

    def get_cell(self, x, y):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        cell_size = min(width // self.cols, height // self.rows)
        col = x // cell_size
        row = y // cell_size
        return row, col
    
    def evaluate(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return -1 if self.board[i][0] == "X" else 1
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return -1 if self.board[0][i] == "X" else 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return -1 if self.board[1][1] == "X" else 1
        if all(cell != " " for row in self.board for cell in row):
            return 0
        return None
    
    def is_full(self):
        return len(self.available) == 0

    def is_winner(self, state, player):
        if isinstance(state, Board):
            state = state.board
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] == player.symbol:
                return True
            if state[0][i] == state[1][i] == state[2][i] == player.symbol:
                return True
        if state[0][0] == state[1][1] == state[2][2] == player.symbol or \
           state[0][2] == state[1][1] == state[2][0] == player.symbol:
            return True
        return False
    
    def print_board(self):
        for row in self.board:
            print(row)

    def reset(self):
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        self.available = [(row, col) for row in range(self.rows) for col in range(self.cols)]
        self.canvas.delete("winner")
        self.canvas.delete("tie")
        self.create_grid()

    def clear_board(self):
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        self.available = [(row, col) for row in range(self.rows) for col in range(self.cols)]
        self.canvas.delete("all")
        self.create_grid()

    def highlight_winner(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        cell_size = min(width // self.cols, height // self.rows)
        for row in range(self.rows):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                y = row * cell_size + cell_size // 2
                self.canvas.create_line(0, y, width, y, fill="green", width=5, tag="winner")
                break
        for col in range(self.cols):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                x = col * cell_size + cell_size // 2
                self.canvas.create_line(x, 0, x, height, fill="green", width=5, tag="winner")
                break
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.canvas.create_line(0, 0, width, height, fill="green", width=5, tag="winner")
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.canvas.create_line(0, height, width, 0, fill="green", width=5, tag="winner")
