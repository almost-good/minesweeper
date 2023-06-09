"""
Board.

Board module represents Minesweeper board and is in charge of
board functionalities.

Board functionalities include:
    - creation of the board,
    - creation of board fields,
    - manipulation of field values,
    - displaying the board.

The script requires:
    - Built in utility "random" and it's method "randint"
        for generation of random numbers,
    - Built in utility "time" and it's method "sleep" for delay,
    - "consts" module from same directory and it's consts:
        - HIDDEN - represents hidden value of the field.
        - MINE - represents mine value of the field.
        - EMPTY - represents empty value of the field.
            Meaning there are no mines nearby to the field.
        - FLAG - represents flag value of the field.
        - OFFSETS - formula for getting adjacent fields.

The file contains following classes:
    - Board
    - GameBoard(Board)
    - PlayerBoard(Board)
"""

from random import randint
from time import sleep
from modules.consts import HIDDEN, MINE, EMPTY, OFFSETS, FLAG


class Board:
    """
    Board class with purpose of creating and structuring board objects.

    Public methods:
        display()
        num_of_fields()
        is_field_type()
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
        self.board = self._create()

        self.initial_run = True

    def display(self):
        """
        Displays the board on the screen.
        """

        self._display_col_indicators(self.cols)
        for row in range(self.rows):
            if self.initial_run:
                sleep(.05)

            self._display_row_indicators(row+1)
            for col in range(self.cols):
                # Prints the value of the board field.
                statement = self._value_to_print(self.board[row][col])
                print(statement, end='  ')

            print()

        self.initial_run = False

    def num_of_fields(self, field_type):
        """
        Checks how many fields are of field_type on the board.

        :return: Number of field_type fields on board.
        :rtype: int
        """

        count = 0

        for row in self.board:
            count += row.count(field_type)

        return count

    def is_field_type(self, row, col, field_type):
        """
        Checks if the field is of selected type.

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        :field_type: Represents type of a field.
        :type field_type: str
        :return: Returns True if it is mine, False otherwise.
        :rtype: bool
        """

        if self.board[row][col] == field_type:
            return True

    def _create(self):
        """
        Constructs the board using const HIDDEN for every field.
        """

        return [[HIDDEN for _ in range(self.cols)]
                for _ in range(self.rows)]

    def _display_row_indicators(self, row):
        """
        Displays row indicator to the left side of the board.

        :param row: Current board row.
        :type row: int
        """

        if row > 9:
            print(row, end=' | ')
        else:
            print(row, end='  | ')

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

    def _value_to_print(self, field):
        """
        Gets the value to print.

        :param field: Selected field.
        :type field: list
        :return: Value to print.
        :rtype: str
        """

        board_values = {
            HIDDEN: f'\033[39;2m{field}\033[0m',
            EMPTY: f'\033[39;2m{field}\033[0m',
            FLAG: f'\033[33;1m{field}\033[0m',
            MINE: f'\033[30;41;1m{field}\033[0m',
            1: f'\033[34;1m{field}\033[0m',
            2: f'\033[32;1m{field}\033[0m',
            3: f'\033[31;1m{field}\033[0m',
            4: f'\033[35;1m{field}\033[0m',
            5: f'\033[33;1m{field}\033[0m',
            6: f'\033[36;1m{field}\033[0m',
            7: f'\033[37;1m{field}\033[0m',
            8: f'\033[31;1m{field}\033[0m'
        }

        return board_values[field]


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

        # Set up.
        self._place_mines()
        self._place_values()

    def _place_mines(self):
        """
        Places mines on the game board.
        """

        mine_count = 1
        while mine_count <= self.mines:
            # 0 <= field <= (rows x cols)
            field = randint(0, (self.rows * self.cols)-1)
            row = field // self.cols
            col = field % self.cols

            if self.is_field_type(row, col, MINE):
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
        flag_field()
        is_visible()
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
        self.gm_board = gm_board  # GameBoard object.
        self.mines_flagged = 0

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

    def flag_field(self, row, col):
        """_summary_
        Set the HIDDEN field value to the FLAG value
        and vice versa.

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        """

        if self.board[row][col] == FLAG:
            self.board[row][col] = HIDDEN
            flag_action = False
        elif self.board[row][col] == HIDDEN:
            self.board[row][col] = FLAG
            flag_action = True

        self._mine_flagged(self.gm_board[row][col], flag_action)

    def is_visible(self, row, col):
        """
        Checks if the field is already visible.

        :param row: Selected board field row.
        :type row: int
        :param col: Selected board field column.
        :type col: int
        :return: If the field is visible True, False otherwise.
        :rtype: bool
        """

        if self.board[row][col] == HIDDEN or \
                self.board[row][col] == FLAG:
            return False

        return True

    def add_mines(self):
        """
        Add mines to the board if game board contains a mine.
        """

        for row in range(0, self.rows):
            for col in range(0, self.cols):
                if self.gm_board[row][col] == MINE:
                    self.board[row][col] = MINE

    def _set_connected_fields(self, row, col):
        """
        Set action on the connected fields value, until all
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

    def _mine_flagged(self, gm_board, flag_action):
        """
        Keeps count of correct fields being flagged.

        :param gm_board: Game board field.
        :type gm_board: str/int
        :param flag_action: Specifies if the flagging took place.
        :type flag_action: bool
        """

        if gm_board == MINE:
            if flag_action:
                self.mines_flagged += 1
            else:
                self.mines_flagged -= 1
