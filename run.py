"""
Minesweeper app.

Main module of the application.
Runs the app.

Functions:
    - print_screen()
    - main()
"""

import os
from art import tprint
from modules.minesweeper import Minesweeper
from modules.user_alert import ContinueAlert, YesOrNoAlert


def print_screen(screen):
    """
    Prints the screen information.

    :param screen: Represents the screen to be printed.
    :type screen: str
    """
    os.system("clear")

    header = " "*3 + "MINESWEEPER"
    tprint(header, font="avatar")

    ContinueAlert().call_alert(screen)


def main():
    """
    Main program function.

    Creates welcome and info screen and runs a a game
    until the player decides to exit.
    """
    print_screen('welcome screen')
    print_screen('info screen')

    while True:
        game = Minesweeper(10, 10, 1)
        game.run()

        play_again = YesOrNoAlert().call_alert('play again')

        if not play_again:
            break


if __name__ == "__main__":
    main()
