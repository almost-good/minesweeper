
import os
from art import tprint
from modules.minesweeper import Minesweeper
from modules.user_alert import ContinueAlert


def main():
    """
    Starts the program.
    """
    os.system("clear")
    header = " "*3 + "MINESWEEPER"
    tprint(header, font="avatar")

    ContinueAlert().call_alert("welcome screen")
    os.system("clear")
    header = " "*3 + "MINESWEEPER"
    tprint(header, font="avatar")

    ContinueAlert().call_alert("info screen")

    game = Minesweeper(10, 10, 4)
    game.run()


if __name__ == "__main__":
    main()
