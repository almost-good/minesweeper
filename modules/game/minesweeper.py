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

        while True:
            self.pl_board.display()

            # Player field choice.
            field = input("Select a field: ")
            field = field.split(',')

            # Check if field is MINE.
            if self.gm_board.is_mine(int(field[0]), int(field[1])):
                print("GAME OVER")
                break

            self.pl_board.set_field(int(field[0]), int(field[1]))
