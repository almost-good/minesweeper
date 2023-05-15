"""
Player Action

Player action module represents player action and is in charge
of player action functionalities.

Player action functionalities include:
    - preforming the action,
    - formatting,
    - validating,
    - handling the errors.

Values required in order to use the PlayerAction:
    (rows, int), (cols, int).
    - Rows - represent number of rows the board grid has.
    - Cols - represent number of columns the board grid has.

The file contains following classes:
    - PlayerAction
"""


class PlayerAction:
    """
    PlayerAction class with purpose of taking player input(action).
    An action is formatted, validated and returned.

    Public methods:
        new_action()
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

    def new_action(self):
        """
        Takes player input, formats it, and validates it.

        :raises ValueError: Represents incorrect player input.
        :return: Formatted player action in dictionary with 3 key-val pairs.
            - action key contains player action (display or flag)
            - row key contains selected row
            - col key contains selected column.
        :rtype: dict
        """

        try:
            pl_action = input("Display or mark the field:  \n")
            pl_action = pl_action.split(',')

            formatted_action = self._format_action(pl_action)

            if self._check_action_vals(formatted_action.get("action"),
                                       formatted_action.get("row"),
                                       formatted_action.get("col")):
                raise ValueError
        except ValueError:
            self._error_msg()
            self.new_action()
        else:
            return formatted_action

    def _format_action(self, action):
        """
        Formats player input depending on what kind of action they choose.

        :param action: User input representing player action.
        :type action: list
        :return: Formatted action.
        :rtype: dict
        """

        match len(action):
            case 2:
                return {
                    "action": "display",
                    "row": int(action[0])-1,
                    "col": int(action[1])-1
                }
            case 3:
                return {
                    "action": action[0],
                    "row": int(action[1])-1,
                    "col": int(action[2])-1
                }
            case _:
                self._error_msg()
                self.new_action()

    def _check_action_vals(self, action, row, col):
        """
        Checks player entered values.
        Checks the type of action, row and col.
        Checks if row and col values are in range.
        If any of checks fails, return true.

        :param action: User input representing player action.
        :type action: string
        :param row: Row picked by player.
        :type row: int
        :param col: Column picked by player.
        :type col: int
        :return: True if any of checks passes, False otherwise.
        :rtype: bool
        """

        if (action != "display") and (action != "flag"):
            return True

        if (not isinstance(row, int)) or (not isinstance(col, int)):
            return True

        if row not in range(0, self.rows) or col not in range(0, self.cols):
            return True

    def _error_msg(self):
        """
        Displays error originated from incorrect player action.
        Displays action instructions for the player.
        """

        print("\n\nOh no! Incorrect value entered!")
        print("-------------------------\n")

        print("For DISPLAYING the field enter ----> row, col")
        print("For FLAGGING the field enter ----> flag, row, col")
        print("-------------------------\n")

        print("Examples:\n----> 2, 3\n----> flag, 2, 3\n")
        print("Restrictions: \n----> Row and col value must be in range!")
        print(f"----> ROW: 1-{self.rows}\n----> COL: 1-{self.cols}")
        print("-------------------------\n")

        print("You can do it!\n\n")
