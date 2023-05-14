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

    def run(self):
        """
        Runs the Minesweeper game.
        """

        # Create game and player board objects.
        player_board = _Board(self.rows, self.cols)

        player_board.display()


class _Board:
    """
    Private Board class available for use only inside __ module.
    Creates and structures board object.

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
        self.value = '-'  # Value of one field.
        self.board = []

        self._create_board()

    def display(self):
        """
        Displays the board on the screen.
        """

        for row in range(self.rows):

            for col in range(self.cols):
                # Prints the value of the board field.
                print(self.board[row][col], end='  ')

            print()

    def _create_board(self):
        """
        Constructs the board using self.value for every field.
        """
        self.board = [[self.value for _ in range(self.cols)]
                      for _ in range(self.rows)]


game = Minesweeper(6, 5, 5)
game.run()
