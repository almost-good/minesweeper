import database
from modules.game.minesweeper import Minesweeper


def main():
    """
    Starts the program.
    """
    game = Minesweeper(10, 10, 8)
    game.run()


if __name__ == "__main__":
    main()
