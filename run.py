import database
from modules.game.minesweeper import Minesweeper


def main():
    """
    Starts the program.
    """
    print(database.call_db())
    game = Minesweeper(9, 10, 20)
    game.run()


if __name__ == "__main__":
    main()
