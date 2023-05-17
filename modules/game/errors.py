"""
Errors

Errors module represents and houses all errors.

Player errors functionalities include:
    - displaying the error.

The file contains following classes:
    - PlayerAction
"""


class PlayerActionError():
    """
    PlayerActionError class handles errors made during
    player action.

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

        self.errors = {}

    def display(self,  errs, vals):
        """
        Displays all applicable errors.

        :param errs: List of different player action errors.
        :type errs: list
        :param vals: Number of values provided.
        :type vals: int
        """

        self.errors = {
            "arg num": self._arg_num(vals),
            "action val": "Incorrect action choosen!",
            "field val": "Incorrect values entered for field selection!",
            "range": "The values are out of range!"
        }

        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nOh no!", end=" ")

        for err in errs:
            print(self.errors[err])

        self._general()

    def _arg_num(self, vals):
        """
        Checks how many values are provided and returns
        corrseponding string.

        :param vals: Number of values provided.
        :type vals: int
        :return: Error message.
        :rtype: str
        """

        match vals:
            case 0:
                return "No value provided!"
            case 1:
                return "Only one value provided!"
            case _:
                return "Too many values provided!"

    def _general(self):
        """
        General error text which is printed with every PlayerActionError.
        """

        print("\n\nExpected: \n")
        print("> For DISPLAYING the field enter 2 digital values only!")
        print(">>> row, col | 2, 3 | 2 3\n")
        print("> For FLAGGING the field enter \"flag\" "
              "followed by 2 digital values!")
        print(">>> flag, row, col | flag, 2, 3 | FlAg 2 3\n")
        print("> For removing a FLAG simply repeat FLAGGING command!")
        print(">>> flag, row, col | flag, 2, 3 | FlAg 2 3\n")
        print(f"> ROW should be between: 0 - {self.rows}")
        print(f"> COLUMN should be between: 0 - {self.cols}")
        print("\nTry again!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
