"""
Minesweeper Game

This module provides a console-based implementation of the classic Minesweeper game. The player
is prompted to enter the number of rows, columns, and mines for the game board, and then can 
begin playing by entering coordinates to uncover squares on the board. If a square containing a
mine is uncovered, the game is over and the player loses. If all non-mine squares are uncovered,
the player wins.

Functions:
    get_user_input(prompt: str, pattern: str) -> str:
        Prompts the user to enter input, validates the input against a regular expression pattern,
        and returns the input if it is valid.

    play_game() -> None:
        Runs the main game loop, prompting the user for input and updating the game board
        accordingly. Displays the game board after each update, and ends the game when the player
        wins or uncovers a mine.

Example Usage:
    To play the game, simply run this module using the command line:
    `python minesweeper.py`

    The game will prompt you for input to set up the game board, and then allow you to enter
    coordinates to uncover squares on the board. Enter 'quit' at any time to end the game.

    Note: This module requires the MinesweeperBoard class from the minesweeper_classes module.
"""

from minesweeper import MinesweeperBoard
import re


def get_user_input(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        print("Invalid input.")


def play_game():
    print("Welcome to Minesweeper!")
    print("To play, enter the coordinates of a square to uncover.")
    print("For example, 'A1' uncovers the square in the first row and first column.")
    print("Enter 'quit' at any time to quit the game.")
    rows = get_user_input("Enter the number of rows (1-26): ", r'^[1-9]$|^[1-2][0-6]$')
    cols = get_user_input("Enter the number of columns (1-26): ", r'^[1-9]$|^[1-2][0-6]$')
    num_mines = get_user_input("Enter the number of mines: ", r'^[1-9]$|^[1-9][0-9]$|^1[0-9][0-9]$|^2[0-4][0-9]$')
    board = MinesweeperBoard(int(rows), int(cols), int(num_mines))
    print(board)
    while not board.is_game_over:
        user_input = get_user_input("Enter a coordinate to uncover: ", r'^[A-Za-z][1-9][0-9]*$')
        if user_input.lower() == 'quit':
            break
        row = ord(user_input[0].lower()) - ord('a')
        col = int(user_input[1:]) - 1
        board.uncover(row, col)
        print(board)
    if board.is_game_over:
        print("Game over! You uncovered a mine.")
    else:
        print("Congratulations, you win!")


if __name__ == '__main__':
    play_game()