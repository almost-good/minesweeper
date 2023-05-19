import database
from modules.minesweeper import Minesweeper


def main():
    """
    Starts the program.
    """


    game = Minesweeper(10, 10, 4)
    game.run()


if __name__ == "__main__":
    main()
