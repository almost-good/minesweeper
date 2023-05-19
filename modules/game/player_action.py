"""
Player Action

Player action module represents player action and is in charge
of player action functionalities and it's alerts.

Player action functionalities include:
    - preforming the action,
    - formatting,
    - validating,
    - handling the errors.

The script requires:
    - "user alert" module from the same directory, and it's class:
        - PlayerActionAlert.

The file contains following classes:
    - PlayerAction
"""

from modules.game.user_alert import PlayerActionAlert


class PlayerAction():
    """
    PlayerAction class with purpose of taking player input(action).
    An action represents field selection and action taken on that field.
    The class formats, validates and returns an action.

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

        # Create Player Action Error object.

        # List of alerts.
        self.alerts = []

    def new_action(self):
        """
        Takes player input, and preforms formatting
        and validation on the input.

        :raises ValueError: ValueError for incorrect input.
        :return: Formatted tuple of input values.
        :rtype: tuple
        """

        while True:
            try:
                pl_action = input("\nDisplay or mark the field: \n\t")
                pl_action = pl_action.replace(',', ' ').split()

                self.alerts = []
                formatted_action = self._format(pl_action)

                # If it's validated break the loop.
                if self._validation(formatted_action):
                    return (formatted_action.get("action"),
                            formatted_action.get("row"),
                            formatted_action.get("col"))

                raise ValueError

            except ValueError:
                PlayerActionAlert(self.rows,
                                  self.cols,
                                  self.alerts,
                                  len(pl_action)).call_alert()
                return ()

    def _format(self, pl_action):
        """
        Checks the number of values passed as the player action.

        :param pl_action: User input representing player action.
        :type pl_action: list
        :return: If formatted return Formatted action, otherwise False.
        :rtype: dict(str, int, int)/False
        """

        match len(pl_action):
            case 2:
                # Return formatted values.
                return self._formatted("display", pl_action[0], pl_action[1])
            case 3:
                return self._formatted(pl_action[0],
                                       pl_action[1],
                                       pl_action[2])
            case _:
                # If the arg number in pl_action is not correct
                # cannot proceed with formatting.
                self.alerts.append("arg num")
                return False

    def _formatted(self, action, row, col):
        """
        Checks action and field values.

        :param action: Represents user action: display/flag.
        :type action: string
        :param row: Represents user selected board row.
        :type row: string
        :param col: Represents user selected board column.
        :type col: string
        :return: If row and col values are digits return formatted
            value, otherwise False.
        :rtype: dict(str, int, int)/False
        """

        # Row and col must be digits to be formatted.
        if row.isdigit() and col.isdigit():
            return {
                "action": action,
                "row": int(row)-1,
                "col": int(col)-1
            }

        # Add errors to the list.
        self._check_action_val(action)
        self.alerts.append("field val")

        return False

    def _validation(self, pl_action):
        """
        Preforms validation on formatted user action.
        Validation is successful if pl_action does exist and
        if there are no alerts.

        :param pl_action: Formatted player action.
            If the var is formatted successfully, contains a dict,
            otherwise contains value: False
        :type pl_action: dict(str, int, int)/bool
        :return: Returns True if the value is validated without errors,
        otherwise False.
        :rtype: bool
        """

        # Check if formatting was successful.
        if pl_action:
            # Check if values are correct.
            self._check_action_val(pl_action.get("action"))
            self._check_field_vals(pl_action.get("row"), pl_action.get("col"))

            # No errors = validation passed!
            if not self.alerts:
                return True

        return False

    def _check_action_val(self, action):
        """
        Checks if action value is "display" or "flag".

        :param action: Player selected action: display/flag.
        :type action: str
        """

        if action not in ("display", "flag"):
            self.alerts.append("action val")

    def _check_field_vals(self, row, col):
        """
        Checks if field values are in range of the board.

        :param row: Row picked by player.
        :type row: int
        :param col: Column picked by player.
        :type col: int
        """

        if row not in range(0, self.rows) or col not in range(0, self.cols):
            self.alerts.append("range")
