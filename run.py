import database
from modules.game.minesweeper import Minesweeper


def main():
    """
    Starts the program.
    """
    print(database.call_db())
    game = Minesweeper(6, 5, 5)
    game.run()


if __name__ == "__main__":
    main()
