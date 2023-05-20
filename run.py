
import os
from art import tprint
from modules.minesweeper import Minesweeper
from modules.user_alert import ContinueAlert


def print_screen(screen):
    os.system("clear")

    header = " "*3 + "MINESWEEPER"
    tprint(header, font="avatar")

    ContinueAlert().call_alert("screen")


def main():
    """
    Starts the program.
    """
    print_screen('welcome screen')
    print_screen('info screen')

    game = Minesweeper(10, 10, 4)
    game.run()


if __name__ == "__main__":
    main()
