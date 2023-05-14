"""
Board.

Board module represents Minesweeper board and is in charge of
board functionalities.

Board functionalities include:
    - creation of the board,
    - creation of board fields,
    - manipulation of field values,
    - displaying the board.

Values required in order to use the board:
    (rows, int), (cols, int), (mines, int).
    - Rows - represent number of rows the board grid has.
    - Cols - represent number of columns the board grid has.
    - Mines - represent number of mines present on board.

The script requires:
    - built in utility "random" for generation of random numbers,
    - consts from consts module:
        (HIDDEN, str, const), (MINE, str, const)
        - HIDDEN - represents hidden value of the field.
        - MINE - represents mine value of the field.

The file contains following classes:
    - Board
    - GameBoard(Board)
"""

import random
from modules.game.consts import HIDDEN, MINE


class Board:
    """
    Board class with purpose of creating and structuring board objects.

    Public methods:
        display()
    """

    def __init__(self, rows, cols):
        """
        Constructor method.

        :param rows: Number of Board grid rows.
        :type rows: int
        :param cols: Number of Board grid columns.
        :type cols: int
        """

        self.rows = rows
        self.cols = cols
        self.board = []

        self._create_board()

    def display(self):
        """
        Displays the board on the screen.
        """

        self._display_col_indicators(self.cols)
        for row in range(self.rows):
            self._display_row_indicators(row)

            for col in range(self.cols):
                # Prints the value of the board field.
                print(self.board[row][col], end='  ')

            print()

    def _create_board(self):
        """
        Constructs the board using const HIDDEN for every field.
        """
        self.board = [[HIDDEN for _ in range(self.cols)]
                      for _ in range(self.rows)]

    def _display_col_indicators(self, col):
        """
        Displays column indicators on top of the board.

        :param cols: Board column count.
        :type cols: int
        """

        print('   ', end='  ')
        for i in range(1, col+1):
            print(i, end='  ')

        print('\n  ', end='  ')
        for i in range(col):
            print('_', end='__')

        print()

    def _display_row_indicators(self, row):
        """
        Displays row indicator to the left side of the board.

        :param row: Current board row.
        :type row: int
        """

        print(row+1, end='  | ')


class GameBoard(Board):
    """
    GameBoard class which inherits the Board class, it is a Board object
    of the GameBoard type.
    Adds additional functionality specific to GameBoard.
    """

    def __init__(self, rows, cols, mines):
        """
        Constructor method.

        :param rows: Number of Board grid rows.
        :type rows: int
        :param cols: Number of Board grid columns.
        :type cols: int
        :param mines: Number of Minesweeper mines on the board.
        :type mines: int
        """

        self.mines = mines
        super().__init__(rows, cols)

        self._place_mines()

    def _place_mines(self):
        """
        Places mines on the game board.
        """

        mine_count = 1
        while mine_count <= self.mines:
            # 0 <= field <= (rows x cols)
            field = random.randint(0, (self.rows * self.cols)-1)
            row = field // self.cols
            col = field % self.cols

            if self.board[row][col] == MINE:
                continue

            self.board[row][col] = MINE
            mine_count += 1
