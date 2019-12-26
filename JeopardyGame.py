from Jeopardy import Game
from HTML_Creator import html_creator
from string import Template

def __main__():
    my_game = Game(0)

    print("Created Jeopardy Game")

    # Main Game Board Creation
    html_creator(my_game)


if __name__ == "__main__":
    __main__()