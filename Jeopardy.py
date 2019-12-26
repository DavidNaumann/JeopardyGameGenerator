from Clue import Clue
from Category import Category
import requests
from random import randint



URL = "http://jservice.io/api/"

MAX_CATEGORIES = 10000

class Game:
    '''
    gametype (type of game):
        0 -> classic, 6 categories, 5 clues per category, 2 rounds
        1 -> practice, random amount of clues
        2 -> custom, ? categories, 5 clues per categories, ? rounds
    '''

    gametype = 0
    amt_of_categories = 6
    amt_of_clues = 5
    rounds = 2
    total_clues = 0

    '''
    [[round 1], [round 2], [round n]]
    '''
    Clues = []
    Categories = []

    def __init__(self, gametype, **kwargs):
        self.gametype = int(gametype)
        for kwarg in kwargs:
            if kwarg == "amt_of_categories":
                self.amt_of_categories = int(kwargs.get(kwarg, None))
            if kwarg == "amt_of_clues":
                self.amt_of_clues = int(kwargs.get(kwarg, None))
            if kwarg == "rounds":
                self.rounds = int(kwargs.get(kwarg, None))
            if kwarg == "total_clues":
                self.total_clues = int(kwargs.get(kwarg, None))

        self.set_game(gametype)

    def set_game(self, gametype):
        if gametype == 0:
            self.amt_of_categories = 6
            self.amt_of_clues = 5
            self.rounds = 2
        if gametype == 1:
            self.rounds = 1
            self.amt_of_categories = self.total_clues
            self.amt_of_clues = 1
        self.get_game()

    def get_game(self):
        self.get_categories()

    def get_categories(self):
        total_clues = 0
        for round_counter in range(self.rounds):
            self.Clues.append([])
            self.Categories.append([])
            for category_counter in range(self.amt_of_categories):
                curr_URL = URL + 'categories'
                offset = randint(1, MAX_CATEGORIES)
                total_clues = 0
                while total_clues < self.amt_of_clues:
                    # Resets/Sets Params
                    offset = randint(1, MAX_CATEGORIES)
                    PARAMS = {'offset': offset}

                    # Gets current category
                    r = requests.get(curr_URL, params=PARAMS)
                    data = r.json()
                    if str(data) != "[]":
                        total_clues = (data[0]['clues_count'])
                        id = (data[0]['id'])
                        title = title_cleaner(str(data[0]['title']))
                        clues_count = data[0]['clues_count']
                        if clues_count >= self.amt_of_clues:
                            total_clues = self.get_clues(id, round_counter)
                            curr_category = Category(id, title, clues_count)

                self.Categories[round_counter].append(curr_category)

    def get_clues(self, category_id, round_counter):
        total_clues = 0
        curr_URL = URL + 'category'
        PARAMS = {'id': category_id}
        CLUES = []
        r = requests.get(curr_URL, PARAMS)
        data = r.json()
        for clue in data['clues']:
            if total_clues < self.amt_of_clues:
                clue_id = clue['id']
                question = clue['question']
                answer = clue['answer']
                value = (total_clues + 1) * (round_counter + 1) * 100
                if question != '' and answer != '':
                    answer, question = cleaner(answer, question)
                    print(question)
                    clue = Clue(clue_id, answer, question, value, category_id)
                    CLUES.append(clue)
                    total_clues += 1
        if total_clues >= self.amt_of_clues:
            self.Clues[round_counter].append(CLUES)
        return total_clues


def checkKey(dict, key):
    if key in dict.keys():
        return True
    return False


def title_cleaner(title):
    if title.find('\\x92') != -1:
        title.replace('\\x92', "'")
    return title


def cleaner(answer, question):
    # Searches for <i> and </i> tags
    if answer.find("<i>") != -1:
        answer = answer.replace("<i>","")
        answer = answer.replace("</i>","")
        answer, question = cleaner(answer, question)

    if question.find("<i>") != -1:
        question = question.replace("<i>","")
        question = question.replace("</i>","")
        answer, question = cleaner(answer, question)

    # Searches for custom character tags
    if answer.find("") != -1:
        answer = answer.replace("", "\\'")
        answer, question = cleaner(answer, question)
    if question.find("") != -1:
        question = question.replace("", "\\'")
        answer, question = cleaner(answer, question)

    # Searches for \ tags
    if answer.find("\\") != -1:
        answer = answer.replace("\\","")
        answer, question = cleaner(answer, question)
    if question.find("\\") != -1:
        question = question.replace("\\","")
        answer, question = cleaner(answer, question)

    return answer, question

