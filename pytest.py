import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Let's Play Super Tic Tac Toe 4 in a row")
        self.player = "X"
        self.board = [""] * 16
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(16): 
            button = tk.Button(self.root, text="", font=('Arial', 24), width=5, height=2, bg="tan",
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i//4, column=i%4)
            self.buttons.append(button)

        reset_button = tk.Button(self.root, text="Restart", font=('Arial', 18), command=self.reset_game)
        reset_button.grid(row=4, column=0, columnspan=4, sticky="nsew")

    def button_click(self, index):
        if self.board[index] == "":
            self.buttons[index].config(text=self.player, )
            self.board[index] = self.player
            if self.check_winner():
                self.end_game(f"Player {self.player} wins!")
            elif "" not in self.board:
                self.end_game("It's a draw!")
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2, 3), ( 4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15),
                                (0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15),
                                (0, 5, 10, 15), (3, 6, 9, 12)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == self.board[combo[3]] != "":
                return True
        return False

    def end_game(self, result):
        messagebox.showinfo("Game Over", result)
        self.reset_game()

    def reset_game(self):
        self.board = [""] * 16
        for button in self.buttons:
            button.config(text="", bg= "tan")
        self.player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
