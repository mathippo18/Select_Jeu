import tkinter as tk
from tkinter import messagebox
import numpy as np
import random

class ReversiGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Reversi")

        self.board_size = 8
        self.board = np.zeros((self.board_size, self.board_size))
        self.board[self.board_size // 2 - 1:self.board_size // 2 + 1, self.board_size // 2 - 1:self.board_size // 2 + 1] = [[-1, 1], [1, -1]]

        self.player = 1  # Le joueur commence
        self.computer = -1
        self.symbols = {-1: "⚫", 0: " ", 1: "⚪"}  # Symboles correspondant à chaque joueur

        self.button_grid = []
        for i in range(self.board_size):
            row_buttons = []
            for j in range(self.board_size):
                button = tk.Button(master, text="", width=4, height=2, command=lambda i=i, j=j: self.play_move(i, j))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.button_grid.append(row_buttons)

        self.update_board()

    def update_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.is_valid_move(i, j, self.player):
                    self.button_grid[i][j].config(text=self.symbols[self.board[i][j]], bg="lightgreen")
                else:
                    self.button_grid[i][j].config(text=self.symbols[self.board[i][j]], bg="grey")

    def play_move(self, i, j):
        if self.board[i][j] != 0:
            return

        if self.is_valid_move(i, j, self.player):
            self.make_move(i, j, self.player)
            self.player = -self.player
            self.update_board()
            if not self.is_any_valid_move(self.player) and not self.is_any_valid_move(-self.player):
                self.show_winner()
                return
            if not self.is_any_valid_move(self.player):
                messagebox.showinfo("Reversi", "No valid move for current player. Switching turn.")
                self.player = -self.player
                self.computer_move()
                self.update_board()

    def make_move(self, i, j, player):
        self.board[i][j] = player
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                r, c = i + di, j + dj
                to_flip = []
                while 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == -player:
                    to_flip.append((r, c))
                    r += di
                    c += dj
                    if 0 <= r < self.board_size and 0 <= c < self.board_size and self.board[r][c] == player:
                        for r, c in to_flip:
                            self.board[r][c] = player
                        break

    def is_valid_move(self, i, j, player):
        if self.board[i][j] != 0:
            return False
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                r, c = i + di, j + dj
                has_enemy_piece = False
                while 0 <= r < self.board_size and 0 <= c < self.board_size:
                    if self.board[r][c] == -player:
                        has_enemy_piece = True
                    elif self.board[r][c] == player and has_enemy_piece:
                        return True
                    elif self.board[r][c] == 0 or (self.board[r][c] == player and not has_enemy_piece):
                        break
                    r += di
                    c += dj
        return False

    def is_any_valid_move(self, player):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.is_valid_move(i, j, player):
                    return True
        return False

    def show_winner(self):
        black_count = np.count_nonzero(self.board == -1)
        white_count = np.count_nonzero(self.board == 1)
        if black_count > white_count:
            winner = "⚫"
        elif white_count > black_count:
            winner = "⚪"
        else:
            winner = "Tie"
        messagebox.showinfo("Reversi", f"Game Over! Winner is: {winner}")
        self.master.destroy()  # Fermer la fenêtre à la fin de la partie

    def computer_move(self):
        valid_moves = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.is_valid_move(i, j, self.computer):
                    valid_moves.append((i, j))
        if valid_moves:
            i, j = random.choice(valid_moves)
            self.make_move(i, j, self.computer)

def main():
    root = tk.Tk()
    reversi_game = ReversiGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
