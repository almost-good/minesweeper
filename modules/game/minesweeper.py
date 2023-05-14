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

    def run(self):
        """
        Runs the Minesweeper game.
        """

        # Create game and player board objects.
        game_board = board.GameBoard(self.rows, self.cols, self.mines)
        player_board = board.Board(self.rows, self.cols)

        game_board.display()
        player_board.display()
