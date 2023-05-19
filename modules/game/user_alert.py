"""
User alert.

User alert module represents alert messages which prompt for
user action.

UserAlert functionalities include:
    - displaying the alerts
    - taking and validating user input.

The script requires:
    - Built in utility "os" for getting the terminal width.
    - Built in utility "time" and it's method "sleep" for delay,

The file contains following classes:
    - Alert
    - YesOrNoAlert
    - ContinueAlert
    - PlayerActionAlert
"""

import os
from time import sleep


class Alert():
    """
    Alert class with purpose of handling alerts.
    """

    def __init__(self):
        """
        Constructor method.
        """

        self.alerts = {}

    def _display_alert(self, alert):
        """
        Prints out all alert messages.

        :param alert: Represents the alert messages.
        :type alert: list
        """

        self._display_separator()

        # Loop over each item in one alert.
        for item in alert:
            sleep(.15)
            print(item)

    def _display_separator(self):
        """
        Displays separator between sections.
        """

        terminal_width = os.get_terminal_size()[0]

        separator = ['=' for d in range(terminal_width)]
        separator = f"\n\033[37;2m{''.join(separator)}\033[0m\n"

        sleep(.15)
        print(separator)


class YesOrNoAlert(Alert):
    """
    YesOrNoAlert class with purpose of handling all alerts
    where the user is asked if they wish to continue.

    Public methods:
        call_alert()
    """

    def __init__(self):
        super().__init__()

        self.alerts = {
            "display": ["\033[31;1mYou suspected there is a MINE" +
                        " on this field!\033[0m\n"]
            }

    def call_alert(self, alert):
        """
        Calls and runs the alert script for
        the specified alert.

        :param alert: Represents the alert in question
        :type alert: str
        :return: Returns whether the user selected "yes" or "no".
        :rtype: bool
        """

        self._display_alert(self.alerts[alert])
        return self._take_input()

    def _take_input(self):
        """
        Takes input and preforms validation.

        :raises ValueError: Incorrect input.
        :return: True if the input is "y", false otherwise.
        :rtype: bool
        """

        while True:
            try:
                sleep(.15)

                user_input = input("Continue \033[33;1m(y/n)\033[0m?: \n\t")
                user_input = user_input.strip()

                match user_input:
                    case 'y':
                        return True
                    case 'n':
                        return False
                    case _:
                        raise ValueError
            except ValueError:
                sleep(.15)
                print("\n\033[31;1mIncorrect value entered!\033[0m")


class ContinueAlert(Alert):
    """
    ContinueAlert class with purpose of handling alerts
    where the user is prompted to "continue".

    Public methods:
        call_alert()
        take_input()
    """

    def call_alert(self, alert, score=0):
        """
        Calls and runs the alert script for
        the specified alert.

        :param alert: Represents the alert in question
        :type alert: str
        :param score: Represents the score achieved.
        :type score: int
        """

        alert_text = self._get_alert(alert, score)
        self._display_alert(alert_text)
        self.take_input()

    def take_input(self):
        """
        Takes input for app's continuation.
        """

        sleep(.15)

        input("\nTo continue \033[33;1mpress any key...\033[0m \n\t")

    def _get_alert(self, alert, score):
        """_summary_

        :param alert: Represents the alert in question
        :type alert: str
        :param score: Represents the score achieved.
        :type score: int
        :return: Specified alert list from possible alerts.
        :rtype: list
        """
        self.alerts = {
            "field visible": ["\033[31;1mSelected field is not" +
                              " hidden!\033[0m",
                              "\033[37;2mThis field cannot take" +
                              " further actions.",
                              "Pick another!\033[0m"],
            "defeat": ["DEFEAT!",
                       "BOOM! The mine exploded!",
                       f"SCORE: {score}",
                       "Practice equals mastery!"],
            "victory": ["VICTORY",
                        "YAY! All mines are located!",
                        f"SCORE: {score}",
                        "Can you win in less time?"]
            }

        return self.alerts[alert]


class PlayerActionAlert(Alert):
    """
    PlayerActionAlert class handles alerts raised during
    the player action.

    Depends on ContinueAlert.

    Public methods:
        call_alert()
    """

    def __init__(self, rows, cols, received_alerts, vals=0):
        """
        Constructor method.

        :param rows: Number of Board grid rows.
        :type rows: int
        :param cols: Number of Board grid columns.
        :type cols: int
        param vals: Number of incorrect arguments passed.
        :type vals: int
        """

        super().__init__()

        self.rows = rows
        self.cols = cols
        self.received_alerts = received_alerts

        self.alerts = {
            "arg num": self._arg_num(vals),
            "action val": "\033[31;1mIncorrect action choosen!",
            "field val": "Incorrect values entered for field selection!",
            "range": "The values are out of range!\033[0m"
        }

        self.action_info = self._action_info()

    def call_alert(self):
        """
        Calls and runs the alert scripts for the specified alerts.
        """

        self._display_separator()

        # Display player action specific alerts.
        self._display_pl_alerts()
        # Display general player action alert text.
        self._display_alert(self.action_info)

        # Display alert for continuation.
        ContinueAlert().take_input()

    def _display_pl_alerts(self):
        """
        Prints out all player alert messages.

        :param alerts: Represents a list of different alerts.
        :type alerts: list
        """

        for alert in self.received_alerts:
            sleep(.15)
            print(self.alerts[alert])

    def _action_info(self):
        """
        Contains information about player actions.
        """

        info = ["\033[33;1mExpected: \033[0m\n",
                "\033[37;2mFor \033[0m\033[33;1mDISPLAYING\033[37;2m" +
                " the field enter 2 digital values!\033[0m",
                "\033[32;1mrow, col | 2, 3 | 2 3\033[0m",
                "\033[37;2mFor \033[0m\033[33;1mFLAGGING\033[37;2m the field" +
                " enter \"flag\" followed by 2 digital values!\033[0m",
                "\033[32;1mflag, row, col | flag, 2, 3 | FlAg 2 3\033[0m",
                "\033[37;2mFor \033[0m\033[33;1mREMOVING a FLAG\033[37;2m " +
                "simply repeat \033[0m\033[33;1mFLAGGING" +
                "\033[37;2m command!\033[0m",
                "\033[32;1mflag, row, col | flag, 2, 3 | FlAg 2 3\n\033[0m",
                "\033[33;1mROW\033[0m should be between:" +
                f" \033[32;1m0 - {self.rows}\033[0m",
                "\033[33;1mCOLUMN\033[0m should be between:" +
                f" \033[32;1m0 - {self.cols}\033[0m\n"]

        return info

    def _arg_num(self, vals):
        """
        Checks how many values are provided and returns
        corrseponding string.

        :param vals: Number of values provided.
        :type vals: int
        :return: Alert message.
        :rtype: str
        """

        match vals:
            case 0:
                return "\033[31;1mNo value provided!\033[0m"
            case 1:
                return "\033[31;1mOnly one value provided!\033[0m"
            case _:
                return "\033[31;1mToo many values provided!\033[0m"
