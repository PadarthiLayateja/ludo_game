import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Define the board
class LudoBoard:
    def __init__(self):
        self.board = np.zeros(52)  # 52 positions on the board (excluding home and safe zones)
        self.home = np.zeros(4)    # 4 home positions
        self.safe_zones = np.zeros(4)  # 4 safe zones

    def display_board(self):
        print("Board:", self.board)
        print("Home:", self.home)
        print("Safe Zones:", self.safe_zones)

# Define the player
class Player:
    def __init__(self, name):
        self.name = name
        self.pieces = np.zeros(4)  # 4 pieces per player

    def roll_dice(self):
        return random.randint(1, 6)

    def move_piece(self, piece_index, steps):
        if self.pieces[piece_index] == 0:
            if steps == 6:
                self.pieces[piece_index] = 1  # Move piece out of home
        else:
            self.pieces[piece_index] += steps
            if self.pieces[piece_index] > 52:
                self.pieces[piece_index] = 52  # Move to safe zone

    def display_pieces(self):
        print(f"Player {self.name}'s pieces:", self.pieces)

# Game logic
class LudoGame:
    def __init__(self, players):
        self.board = LudoBoard()
        self.players = [Player(name) for name in players]
        self.current_player = 0

    def play_turn(self):
        player = self.players[self.current_player]
        print(f"\n{player.name}'s turn")
        dice_roll = player.roll_dice()
        print(f"Dice roll: {dice_roll}")
        player.display_pieces()
        piece_index = int(input(f"Choose a piece to move (0-3): "))
        player.move_piece(piece_index, dice_roll)
        player.display_pieces()
        self.check_winner()
        self.current_player = (self.current_player + 1) % len(self.players)

    def check_winner(self):
        for player in self.players:
            if all(piece == 52 for piece in player.pieces):
                print(f"Player {player.name} wins!")
                return True
        return False

    def start_game(self):
        while True:
            self.play_turn()
            if self.check_winner():
                break

# Main function to start the game
if __name__ == "__main__":
    players = ["Alice", "Bob", "Charlie", "Diana"]
    game = LudoGame(players)
    game.start_game()