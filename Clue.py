class Clue:
    id = -1
    answer = ""
    question = ""
    value = -1
    category_id = -1
    value_txt = ""

    def __init__(self, id, answer, question, value, category_id):
        self.id = id
        self.answer = answer
        self.question = question
        self.value = value
        self.value_txt = ('$' + str(value))
        self.category_id = category_id
