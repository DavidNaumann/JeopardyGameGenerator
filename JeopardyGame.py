from Jeopardy import Game
from HTML_Creator import html_creator

def __main__():
    # Begins making game
    print("Generating random Jeopardy game...")
    my_game = Game(0)
    print("Finished generating random Jeopardy game.")

    # Begins Game Board HTML creation
    print("Generating HTML structure for Jeopardy game...")
    html_creator(my_game)
    print("Finished generating HTML structure for Jeopardy game.")


if __name__ == "__main__":
    __main__()