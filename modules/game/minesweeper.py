"""
Minesweeper.

Minesweeper module represents the game Minesweeper and
is in charge of Minesweeper functionalities.

Minesweeper functionalities include:
    - running the game.

The script requires:
    - built in utility "time" for elapsed time measurement,
    - "board" module from the same directory, and it's classes:
        - GameBoard,
        - PlayerBoard,
    - "player_action" module from the same directory, and it's class:
        - PlayerAction.
    - consts from consts module:
        (HIDDEN, str, const), (MINE, str, const)
        - HIDDEN - represents hidden value of the field.
        - FLAG - represents flag value of the field.

The file contains following classes:
    - Minesweeper
"""

import time
from modules.game.board import GameBoard, PlayerBoard
from modules.game.player_action import PlayerAction
from modules.game.consts import HIDDEN, FLAG


class Minesweeper:
    """
    Minesweeper class used to create and execute game object.

    Public methods:
        run()
    """

    def __init__(self, rows, cols, mines):
        """
        Constructor method.

        :param rows: Number of Minesweeper grid rows.
        :type rows: int
        :param cols: Number of Minesweeper grid columns.
        :type cols: int
        :param mines: Number of Minesweeper mines in the grid.
        :type mines: int
        """

        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.flags = mines

        # Create game and player board objects.
        self.gm_board = GameBoard(self.rows, self.cols, self.mines)
        self.pl_board = PlayerBoard(
            self.rows, self.cols, self.gm_board.board
            )

        # Player action object.
        self.pl_action = PlayerAction(self.rows, self.cols)

    def run(self):
        """
        Runs the Minesweeper game.
        """

        self.gm_board.display()
        self.pl_board.display()

        # Time tracker.
        game_timer = time.time()
        self._display_game_footer(game_timer)

        while True:
            # Player action.
            action_type, action_row, action_col = self.pl_action.new_action()

            # Check if the field is visible, if not proceed.
            if self.pl_board.field_visible(action_row, action_col):
                self._field_visible_warning(action_row, action_col)
                continue

            if action_type == "flag":
                self.pl_board.flag_field(action_row, action_col)
                self.flags = self.mines - self.pl_board.num_of_fields(FLAG)
            else:
                self.pl_board.set_field(action_row, action_col)

            # Check if the game is over.
            if self._game_over(action_row, action_col, action_type):
                break

            self.pl_board.display()
            self._display_game_footer(game_timer)

    def _display_game_footer(self, timer_start):
        """
        Displays game footer.
        Game footer contains information:
            - Number of MINES on the board.
            - Number of remaining FLAGS.
            - Time elapsed from beginning of the game.

        :param timer_start: Number representing the time when the game started.
        :type timer_start: Time object.
        """

        timer = round(time.time() - timer_start)
        print(f"\nMINES: {self.mines}\tFLAGS: {self.flags}\tTIMER: {timer}s\n")

    def _field_visible_warning(self, row, col):
        """
        Displays field already visible warning.

        :param row: Selected player board field row.
        :type row: int
        :param col: Selected player board field column.
        :type col: int
        """

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n{row+1} {col+1} field is not hidden!"
              "\nThis field cannot take further actions."
              "\nPick another!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    def _game_over(self, row, col, action_type):
        """
        Checks if the game is over, and if it's
        victory or defeat.

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        :param action_type: Player action.
        :type action_type: str
        :return: True if the game is over, False otherwise.
        :rtype: bool
        """

        if self._game_lose(row, col, action_type):
            self._defeat()
            return True

        if self._game_win():
            self._victory()
            return True

        return False

    def _game_lose(self, row, col, action_type):
        """
        Checks if the game is indeed lost.
        The game is lost if selected field is mine, and
        player action is "display".

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        :param action_type: Player action.
        :type action_type: str
        :return: True if the game is lost, False otherwise.
        :rtype: bool
        """

        if self.gm_board.is_mine(row, col) and \
                (action_type in "display"):
            return True

        return False

    def _game_win(self):
        """
        Checks if the game is indeed won.
        The game is won if number of remaining fields if equal
        to mine count, or if count of mines flagged is equal to mine
        count and flag count is 0.

        :return: True if the game is won, False otherwise.
        :rtype: bool
        """

        hidden_count = self.pl_board.num_of_fields(HIDDEN)
        remaining_fields = hidden_count + self.mines - self.flags

        # If number of remaining fields is equal to mine count -> victory.
        # If count of mines flagged is equal to mine count, and flag count
        if (remaining_fields) == self.mines or \
                (self.pl_board.mine_flagged == self.mines and
                 self.flags == 0):
            return True

        return False

    def _defeat(self):
        """
        Displays that the game is lost.
        """

        print("GAME LOST")

    def _victory(self):
        """
        Displays that the game is won.
        """

        print("GAME WIN")
