"""
Minesweeper.

Minesweeper module represents the game Minesweeper and
is in charge of Minesweeper functionalities.

Minesweeper functionalities include:
    - running the game.

Values required in order to play the game:
    (rows, int), (cols, int), (mines, int).
    - Rows - represent number of rows the board grid has.
    - Cols - represent number of columns the board grid has.
    - Mines - represent number of mines present on board.

The script depends on "board" module from the same directory.

The file contains following classes:
    - Minesweeper
"""

from modules.game import board


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

        # Create game and player board objects.
        self.gm_board = board.GameBoard(self.rows, self.cols, self.mines)
        self.pl_board = board.PlayerBoard(
            self.rows, self.cols, self.gm_board.board
            )

    def run(self):
        """
        Runs the Minesweeper game.
        """

        self.gm_board.display()
        self.pl_board.display()

        while True:
            # Player field choice.
            field = input("Select a field: ")
            field = field.split(',')
            
            self.pl_board.set_field(int(field[0]), int(field[1]))
            
            # Check if the game is over.
            if self._game_over(int(field[0]), int(field[1])):
                break

            self.pl_board.display()

    def _game_over(self, row, col):
        """
        Checks if the game is over, and if it's
        victory or defeat.

        :param row: Current field row of the grid.
        :type row: int
        :param col: Current field column of the grid.
        :type col: int
        :return: True if the game is over, False otherwise.
        :rtype: bool
        """

        # If the selected field is mine game is lost.
        if self.gm_board.is_mine(row, col):
            self._game_lose()
            return True

        hidden_count = self.pl_board.num_of_hidden_fields()
        # If number of remaining fields is equal
        # to number of bombs, the game is won.
        if hidden_count == self.mines:
            self._game_win()
            return True

        return False

    def _game_lose(self):
        """
        Displays that the game is lost.
        """

        print("GAME LOST")

    def _game_win(self):
        """
        Displays that the game is won.
        """

        print("GAME WIN")
