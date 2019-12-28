from string import Template


def round_html_creator(my_game, curr_round, categories):
    actual_round = curr_round + 1
    template_file_name = "site/template.html"
    # read it
    template_file = open(template_file_name)
    template_txt = Template(template_file.read())
    template_file.close()
    category_titles = []
    for category in my_game.Categories[curr_round]:
        category_titles.append(category.title)
    # document data
    categories_dict = dict(zip(categories, category_titles))
    game_dict = categories_dict
    clue_counter = 0
    clue_variables = []
    clue_values = []
    for curr_clue in range(my_game.amt_of_clues):
        category_counter = 0
        for category in categories:
            spot = (category + str(curr_clue))
            clue_variables.append((category + str(curr_clue)))
            clue_values.append(my_game.Clues[curr_round][category_counter][clue_counter].value_txt)
            category_counter += 1
        clue_counter += 1
    clues_dict = dict(zip(clue_variables, clue_values))
    round_dict = {'actual_round': actual_round}
    game_dict.update(round_dict)
    game_dict.update(clues_dict)
    # do the substitution
    dest_txt = template_txt.substitute(game_dict)
    dest_filename = "site/round" + str(actual_round) + ".html"
    dest_file = open(dest_filename, 'w+')
    dest_file.write(dest_txt)
    dest_file.close()


def clue_ans_html_creator(my_game, curr_round, categories):
    actual_round = curr_round + 1
    clue_template_filename = "site/clue_template.html"
    clue_locations = "site/clue/round" + str(actual_round) + "/"
    template_file = open(clue_template_filename)
    template_txt = Template(template_file.read())
    template_file.close()
    category_counter = 0
    for clues in my_game.Clues[curr_round]:
        letter = categories[category_counter]
        clue_counter = 0
        for clue in clues:
            letter_number = letter + str(clue_counter)
            answer_link = letter_number + "_answer.html"
            clue_link = letter_number + ".html"
            board_link = "javascript:window.close();"
            clue_dict = {
                'link': answer_link,
                'clue': clue.question
            }
            dest_txt = template_txt.substitute(clue_dict)
            clue_filename = clue_locations + clue_link
            answer_filename = clue_locations + answer_link

            clue_file = open(clue_filename, 'w+')
            clue_file.write(dest_txt)
            clue_file.close()

            # Writing answer file

            answer_dict = {
                'link': board_link,
                'clue': clue.answer
            }
            dest_txt = template_txt.substitute(answer_dict)

            answer_file = open(answer_filename, 'w+')
            answer_file.write(dest_txt)
            answer_file.close()
            clue_counter += 1
        category_counter += 1


def html_creator(my_game):
    categories = ['a', 'b', 'c', 'd', 'e', 'f']
    for curr_round in range(my_game.rounds):
        actual_round = curr_round + 1

        round_html_creator(my_game, curr_round, categories)

        print("  Finished Round " + str(actual_round) + " Board HTML Page")

        # Clue Page Creations
        clue_ans_html_creator(my_game, curr_round, categories)

        print("  Finished Round " + str(actual_round) + " Clue and Answers HTML Pages")