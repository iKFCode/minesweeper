--- Minesweeper Game ---
This is a console-based implementation of the classic Minesweeper game. 
The player is prompted to enter the number of rows, columns, and mines for the game board and then can begin playing by entering coordinates to uncover squares on the board. 
If a square containing a mine is uncovered, the game is over, and the player loses. If all non-mine squares are uncovered, the player wins.


 --- Installation ---
Clone this repository to your local machine using the following command:
git clone https://github.com/exampleuser/minesweeper.git


 --- Usage  ---
To play the game, navigate to the directory where the repository was cloned and run the following command:
python minesweeper.py

The game will prompt you for input to set up the game board, and then allow you to enter coordinates to uncover squares on the board. Enter 'quit' at any time to end the game.


 --- Dependencies  ---
This module requires Python 3.x to run. There are no other dependencies.


 --- Code Structure  ---
The code is organized into two modules:
minesweeper_classes.py: contains the classes for the Minesweeper game.
minesweeper.py: contains the main game loop and user interface.


 --- Minesweeper Classes ---

-- MinesweeperBoard --
A class to represent the Minesweeper game board.

Attributes:
num_rows (int): The number of rows in the board.
num_cols (int): The number of columns in the board.
num_mines (int): The number of mines on the board.
num_uncovered_cells (int): The number of cells that have been uncovered.
is_game_over (bool): Whether the game is over or not.
board (List[List[MinesweeperCell]]): A 2D list of MinesweeperCell objects representing the game board.

Methods:
__init__(self, num_rows: int, num_cols: int, num_mines: int) -> None: Initializes a new instance of the MinesweeperBoard class with the specified number of rows, columns, and mines.
__str__(self) -> str: Returns a string representation of the game board.
get_adjacent_cells(self, row: int, col: int) -> List[MinesweeperCell]: Returns a list of all adjacent cells to the cell at the specified row and column.
uncover(self, row: int, col: int) -> None: Uncover the cell at the specified row and column.


-- MinesweeperCell --
A class to represent a single cell on a Minesweeper game board.

Attributes:
is_mine (bool): Whether or not the cell contains a mine.
is_uncovered (bool): Whether or not the cell has been uncovered by the player.
num_adjacent_mines (int): The number of mines adjacent to this cell.

Methods
__init__(self) -> None: Initializes a new instance of the MinesweeperCell class. The new cell is not a mine and is initially covered.
display_value(self) -> str: Returns the current value of the cell.
uncover(self) -> None: Sets the is_uncovered instance variable to True, indicating that the cell has been uncovered.