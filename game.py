import random


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


game = Minesweeper(6, 5, 5)
game.run()
