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
        - EMPTY - represents empty value of the field.
            Meaning there are no mines nearby to the field.
        - OFFSETS - formula for getting adjacent fields.

The file contains following classes:
    - Board
    - GameBoard(Board)
    - PlayerBoard(Board)
"""

import random
from modules.game.consts import HIDDEN, MINE, EMPTY, OFFSETS


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

    Public methods:
        is_mine()
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
        self._place_values()

    def is_mine(self, row, col):
        """
        Checks if the field contains MINE or not.

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        :return: Returns True if it is mine, False otherwise.
        :rtype: bool
        """

        if self.board[row][col] == MINE:
            return True

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

            if self.is_mine(row, col):
                continue

            self.board[row][col] = MINE
            mine_count += 1

    def _place_values(self):
        """
        Places values on the game board.
        The values indicate the number of nearby mines.
        """

        for row in range(self.rows):
            for col in range(self.cols):
                # If field value is not MINE assign a value.
                if self.board[row][col] == MINE:
                    continue

                self.board[row][col] = self._get_value(row, col)

    def _get_value(self, row, col):
        """
        Calculates the number of nearby mines to the current field.

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        :return: Number of nearby mines to the current field
            or EMPTY if not found.
        :rtype: int/str
        """

        count = 0

        # Check each field around current board field.
        for offset in OFFSETS:
            offset_row = offset[0] + row
            offset_col = offset[1] + col

            # Make sure the field is inside of the board and is a MINE.
            if (offset_row in range(0, self.rows)) and \
                    (offset_col in range(0, self.cols)) and \
                    (self.board[offset_row][offset_col] == MINE):
                count += 1

        if count == 0:
            return EMPTY

        return count


class PlayerBoard(Board):
    """
    PlayerBoard class which inherits the Board class, it is a Board object
    of the PlayerBoard type.
    Adds additional functionality specific to PlayerBoard.

    Public methods:
        set_field()
    """

    def __init__(self, rows, cols, gm_board):
        """
        Constructor method.

        :param rows: Number of Board grid rows.
        :type rows: int
        :param cols: Number of Board grid columns.
        :type cols: int
        :param gm_board: GameBoard object's board.
            Allows PlayerBoard to look at GameBoard.
        :type gm_board: GameBoard object.
        """

        super().__init__(rows, cols)
        self.gm_board = gm_board

    def set_field(self, row, col):
        """
        Set the field value to the game grid field value.
        If the value is EMPTY keep checking.

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        """

        self.board[row][col] = self.gm_board[row][col]

        # If the field is empty, check other fields.
        if self.board[row][col] == EMPTY:
            self._set_connected_fields(row, col)

    def _set_connected_fields(self, row, col):
        """
        Set the connected fields value, until all
        connected EMPTY field values are set.

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        """

        fields = [(row, col)]

        while len(fields) > 0:
            # Field on which the operation takes place.
            field = fields.pop()

            # Check each field around current board field.
            for offset in OFFSETS:
                row = offset[0] + field[0]
                col = offset[1] + field[1]

                # Field must be in range, HIDDEN and game field can't be mine.
                if (row in range(0, self.rows)) and \
                        (col in range(0, self.cols)) and \
                        (self.board[row][col] == HIDDEN) and \
                        (self.gm_board[row][col] != MINE):

                    # Set the field value.
                    self.board[row][col] = \
                            self.gm_board[row][col]

                    # If the field is EMPTY we need to check
                    # it's adjacent fields too.
                    if (self.board[row][col] == EMPTY) and \
                            ((row, col) not in fields):
                        fields.append((row, col))
