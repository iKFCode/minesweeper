import random

class MinesweeperBoard:
    """
    This class represents a Minesweeper board, with a two-dimensional array of `MinesweeperCell` objects.

    Attributes:
        num_mines (int): The total number of mines on the board.
        num_uncovered (int): The number of cells that have been uncovered.
        is_game_over (bool): Indicates whether the game is over (either won or lost).
        board (list[list[MinesweeperCell]]): The two-dimensional array of `MinesweeperCell` objects.
    """
    def __init__(self, rows, cols, num_mines):
        """
        Initializes a new `MinesweeperBoard` object with the specified number of rows, columns, and mines.

        Args:
            rows (int): The number of rows in the board.
            cols (int): The number of columns in the board.
            num_mines (int): The number of mines to place on the board.
        """
        self.num_mines = num_mines
        self.num_uncovered = 0
        self.is_game_over = False
        self.board = self._create_board(rows, cols)
        self._place_mines()

    def __str__(self):
        """
        Returns a string representation of the current state of the board.
        """
        rows = []
        header = "    " + "   ".join(str(i) for i in range(1, len(self.board[0]) + 1))
        rows.append(header)
        for i, row in enumerate(self.board):
            letter = chr(i + ord('A'))
            row_str = " | ".join(cell.display_value() for cell in row)
            rows.append(f"{letter} | {row_str} |")
        return "\n".join(rows)

    def uncover(self, row, col):
        """
        This function uncovers the cell at the specified row and column.

        If the cell contains a mine, the game is over (is_game_over will be set to True).
        Otherwise, the cell is uncovered and the number of uncovered cells is incremented.
        If all non-mine cells have been uncovered, the game is over (is_game_over will be set to True).

        Args:
            row (int): The row of the cell to uncover.
            col (int): The column of the cell to uncover.
        """
        cell = self.board[row][col]
        if cell.is_mine:
            cell.is_uncovered = True
            self.is_game_over = True
            return
        cell.uncover()
        self.num_uncovered += 1
        if self.num_uncovered == len(self.board) * len(self.board[0]) - self.num_mines:
            self.is_game_over = True

    def _create_board(self, rows, cols):
        """
        Creates a new board with the specified number of rows and columns, initialized with `MinesweeperCell` objects.

        Args:
            rows (int): The number of rows in the board.
            cols (int): The number of columns in the board.

        Returns:
            list[list[MinesweeperCell]]: A two-dimensional array of `MinesweeperCell` objects.
        """
        return [[MinesweeperCell() for _ in range(cols)] for _ in range(rows)]

    def _place_mines(self):
        """
        Private method to randomly place mines on the board.

        This method is called when the `MinesweeperBoard` object is created. It generates a list of all cells on the board and
        randomly selects a specified number of them to be mines. For each mine, it updates the `is_mine` attribute of the
        corresponding `MinesweeperCell` object to `True`, and then iterates through the adjacent cells (up to a maximum of
        8) and increments their `num_adjacent_mines` attribute.

        Returns:
            None.
        """
        cells = [(row, col) for col in range(len(self.board[0])) for row in range(len(self.board))]
        mines = random.sample(cells, self.num_mines)
        for row, col in mines:
            self.board[row][col].is_mine = True
            for i in range(max(0, row - 1), min(row + 2, len(self.board))):
                for j in range(max(0, col - 1), min(col + 2, len(self.board[0]))):
                    self.board[i][j].num_adjacent_mines += 1


class MinesweeperCell:
    """
    A class to represent a single cell on a Minesweeper game board.

    Each `MinesweeperCell` object represents a single cell on the game board, which may or may not contain a mine.
    The cell can be in one of two states: covered or uncovered. If the cell is uncovered, the value of the cell is
    displayed, which may be a blank space (if there are no adjacent mines), a number (if there are adjacent mines), or an
    asterisk (if the cell contains a mine). If the cell is covered, the value is displayed as a hyphen.

    Attributes:
        is_mine (bool): Whether or not the cell contains a mine.
        is_uncovered (bool): Whether or not the cell has been uncovered by the player.
        num_adjacent_mines (int): The number of mines adjacent to this cell.
    """

    def __init__(self):
        """
        Initializes a new instance of the MinesweeperCell class.

        The new cell is not a mine and is initially covered.
        """
        self.is_mine = False
        self.is_uncovered = False
        self.num_adjacent_mines = 0

    def display_value(self):
        """
        Returns the current value of the cell.

        If the cell is uncovered, the value of the cell is displayed, which may be a blank space (if there are no adjacent
        mines), a number (if there are adjacent mines), or an asterisk (if the cell contains a mine). If the cell is
        covered, the value is displayed as a hyphen.

        Returns:
            str: The current value of the cell.
        """
        if self.is_uncovered:
            if self.is_mine:
                return "*"
            elif self.num_adjacent_mines == 0:
                return " "
            else:
                return str(self.num_adjacent_mines)
        else:
            return "-"

    def uncover(self):
        """
        This method sets the is_uncovered instance variable to True, indicating that the cell has been uncovered.
        """
        self.is_uncovered = True