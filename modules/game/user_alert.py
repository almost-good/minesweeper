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
    - ContinueAlert
"""

import os
from time import sleep


class ContinueAlert():
    """
    ContinueAlert class with purpose of handling alerts.

    Public methods:
        take_input()
    """

    def __init__(self):
        """
        Constructor method.
        """

        self.alerts = {
            "display": ["\n\033[31;2mYou suspected there is a MINE" +
                        " on this field!\033[0m\n"]
            }

    def take_input(self, alert):
        """
        Takes input and preforms validation.

        :param alert: Represents the trigger for alert.
        :type alert: str
        :raises ValueError: Incorrect input.
        :return: True if the input is "y", false otherwise.
        :rtype: bool
        """

        self._display_separator()
        while True:
            try:
                self._display_alert(alert)
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

    def _display_alert(self, alert):
        """
        Prints out all alert messages.

        :param alert: Represents the trigger for alert.
        :type alert: list
        """

        for item in self.alerts[alert]:
            sleep(.15)
            print(item)

    def _display_separator(self):
        """
        Displays separator between sections.
        """

        terminal_width = os.get_terminal_size()[0]

        separator = ['=' for d in range(terminal_width)]
        separator = f"\n\033[37;2m{''.join(separator)}\033[0m"

        sleep(.15)
        print(separator)
