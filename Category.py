class Category:
    id = -1
    title = ""
    clues_count = -1

    def __init__(self, id, title, clues_count):
        self.id = id
        self.title = title.upper()
        self.clues_count = clues_count
