"""
User alert.

User alert module represents alert messages which prompt for
user action.

UserAlert functionalities include:
    - displaying the alerts
    - taking and validating user input.

The file contains following classes:
    - ContinueAlert
"""


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
            "display": "You suspected there is a MINE on this field!"
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

        while True:
            try:
                print(self.alerts[alert])
                user_input = input("Continue (y/n)?: \n")
                user_input = user_input.strip()

                match user_input:
                    case 'y':
                        return True
                    case 'n':
                        return False
                    case _:
                        raise ValueError
            except ValueError:
                print("Incorrect value entered!")
