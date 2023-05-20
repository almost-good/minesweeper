"""
Minesweeper.

Minesweeper module represents the game Minesweeper and
is in charge of Minesweeper functionalities.

Minesweeper functionalities include:
    - running the game.

The script requires:
    - Built in utility "time" for elapsed time measurement and delay.
    - Built in utility "os" for clearing the terminal.
    - "board" module from the same directory, and it's classes:
        - GameBoard,
        - PlayerBoard.
    - "user_alert" module from the same directory, and it's classes:
        - ContinueAlert
        - YesOrNoAlert.
    - "player_action" module from the same directory, and it's class:
        - PlayerAction.
    - "const" module from the same directory and it's consts:
        - HIDDEN - represents hidden value of the field,
        - FLAG - represents flag value of the field.

The file contains following classes:
    - Minesweeper.
"""

import os
from time import time, sleep
from modules.board import GameBoard, PlayerBoard
from modules.player_action import PlayerAction
from modules.user_alert import ContinueAlert, YesOrNoAlert
from modules.consts import HIDDEN, FLAG, MINE


class Minesweeper:
    """
    Minesweeper class creates and executes the game.

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

        self.action_type = ""
        self.timer_start = None
        self.score = None

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

        Displays the content, gets the user action,
        checks if the board is visible, processes player
        move, checks for game over.
        """

        # Time tracker.
        self.timer_start = time()

        while True:
            # Clear the screen.
            os.system('clear')

            # Display game content.
            self._display_game()

            # Checks if the information is fetched correctly.
            action_bundle = self.pl_action.new_action()
            try:
                self.action_type, action_row, action_col = action_bundle
            except ValueError:
                continue

            # Check if the field is visible, if not proceed.
            if self.pl_board.is_visible(action_row, action_col):
                ContinueAlert().call_alert("field visible")
                continue

            self._player_move(action_row, action_col)

            # Check if the game is over.
            if self._game_over(action_row, action_col):
                break

    def _display_game(self):
        """
        Displays all game contents; the board and footer.
        """

        self.pl_board.display()

        self._display_game_footer()

    def _display_game_footer(self):
        """
        Displays game footer.
        Game footer contains information:
            - Number of MINES on the board.
            - Number of remaining FLAGS.
            - Time elapsed from beginning of the game.
        """

        timer = self._get_time_passed()

        print(f"\n\033[37;2mMINES:\033[0m \033[31;1m{self.mines}\033[0m"
              f"\t\033[37;2mFLAGS:\033[0m \033[32;1m{self.flags}\033[0m"
              f"\t\033[37;2mTIMER:\033[0m \033[33;1m{timer}\033[0m")

    def _player_move(self, row, col):
        """
        Runs the player selected move.

        :param row: Selected field's row.
        :type row: int
        :param col: Selected field's column.
        :type col: int
        """

        if self.action_type == "flag":
            self._flag_move(row, col)
        else:
            self._display_move(row, col)

    def _flag_move(self, row, col):
        """
        Calls the flagging of the field and updates flag count.

        :param row: Selected field's row.
        :type row: int
        :param col: Selected field's column.
        :type col: int
        """

        self.pl_board.flag_field(row, col)
        self.flags = self.mines - self.pl_board.num_of_fields(FLAG)

    def _display_move(self, row, col):
        """
        Calls the display action on the field if applicable.

        :param row: Selected field's row.
        :type row: int
        :param col: Selected field's column.
        :type col: int
        """

        # Check if the field is flagged.
        if self.pl_board.is_field_type(row, col, FLAG):
            # Ask for confirmation to proceed.
            to_continue = YesOrNoAlert().call_alert(self.action_type)
            sleep(.15)

            if not to_continue:
                self.action_type = ""  # Reset.
                return

            self.flags += 1

        # If the field is not flagged, set the field straight away.
        self.pl_board.set_field(row, col)

    def _game_over(self, row, col):
        """
        Checks if the game is over, and if it's
        victory or defeat. Displays the game over screen.

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        :return: True if the game is over, False otherwise.
        :rtype: bool
        """

        result = None

        if self._game_lose(row, col):
            result = self._defeat()
        elif self._game_win():
            result = self._victory()

        if result:
            os.system('clear')
            self._display_game()
            ContinueAlert().call_alert(result, self.score)
            return True

        return False

    def _game_lose(self, row, col):
        """
        Checks if the game is indeed lost.
        The game is lost if selected field is mine, and
        player action is "display".

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        :return: True if the game is lost, False otherwise.
        :rtype: bool
        """

        if self.gm_board.is_field_type(row, col, MINE) and \
                (self.action_type == "display"):
            return True

        return False

    def _game_win(self):
        """
        Checks if the game is indeed won.
        The game is won if number of remaining fields is equal
        to mine count, or if count of mines flagged is equal to mine
        count and flag count is 0.

        :return: True if the game is won, False otherwise.
        :rtype: bool
        """

        hidden_count = self.pl_board.num_of_fields(HIDDEN)
        remaining_fields = hidden_count + self.mines - self.flags

        if (remaining_fields) == self.mines or \
                (self.pl_board.mines_flagged == self.mines and
                 self.flags == 0):
            return True

        return False

    def _defeat(self):
        """
        Prepares the board for it's defeat mode,
        gets the score and returns that the game is indeed lost.
        """

        # The board uncovers where all the mines are.
        self.pl_board.add_mines()
        self.score = 0 - self._get_time_passed()

        return 'defeat'

    def _victory(self):
        """
        Prepares the board for it's victory mode,
        gets the score and returns that the game is indeed won.
        """

        # The board is equal to the game board.
        self.pl_board = self.gm_board
        self.score = self._get_time_passed()

        return 'victory'

    def _get_time_passed(self):
        """
        Calculates how much time has passed from starting the game.

        :return: Calculation how much time passed from starting the game.
        :rtype: Time obj
        """

        return round(time() - self.timer_start - 1)
