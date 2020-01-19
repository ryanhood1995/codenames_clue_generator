# -------------------------------------------------------------------------------
#   Description: This file provides some simple helper methods that did not fit
#   into any other category.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

import inflect

# This functions finds the plural version of all words in the board and returns it.
def pluralize_board(board):
    # We will use the inflect library to get each word's plural variant.
    p = inflect.engine()

    # Break down the singular board into the three categories.
    singular_blue_list = board['blue']
    singular_red_list = board['red']
    singular_assassin = board['assassin']

    plural_blue_list = []
    plural_red_list = []

    # For each word in each singular list, we append its plural version on its plural list.
    for word in singular_blue_list:
        plural_blue_list.append(p.plural(word))
    for word in singular_red_list:
        plural_red_list.append(p.plural(word))

    # There's only one assassin.
    plural_assassin = p.plural(singular_assassin)

    # Construct the plural board from the plural list.
    plural_board = {'blue': plural_blue_list, 'red': plural_red_list, 'assassin': plural_assassin}
    return plural_board

# This function returns a list of all the words found in the board.
def get_board_words(board):
    # Get each list seperately.
    blue_list = board['blue']
    red_list = board['red']
    assassin = board['assassin']

    # Combine the red and blue list.
    all_words = blue_list + red_list

    # The assassin is just one word, so simply append it to the end.
    all_words.append(assassin)
    return all_words

def convert_team_to_number(team):
    if team == 'red':
        return 1
    elif team == 'blue':
        return 2
    else:
        print("INVALID TEAM NAME.")
        return -1

def create_board(going_first, first_number_of_words, second_number_of_words):
    red_list = []
    blue_list = []
    board = {}

    going_first_num = convert_team_to_number(going_first)

    if going_first_num == 1:
        # Red is the first player.
        count_red = 0
        while count_red != first_number_of_words:
            red_word = input("Enter the next red word in all lowercase.")
            red_list.append(red_word)
            count_red = count_red + 1
        board['red'] = red_list
        count_blue = 0
        while count_blue != second_number_of_words:
            blue_word = input("Enter the next blue word in all lowercase.")
            blue_list.append(blue_word)
            count_blue = count_blue + 1
        board['blue'] = blue_list
    elif going_first_num == 2:
        # Blue is the first player.
        count_blue = 0
        while count_blue != first_number_of_words:
            blue_word = input("Enter the next blue word in all lowercase.")
            blue_list.append(blue_word)
            count_blue = count_blue + 1
        board['blue'] = blue_list
        count_red = 0
        while count_red != second_number_of_words:
            red_word = input("Enter the next red word in all lowercase.")
            red_list.append(red_word)
            count_red = count_red + 1
        board['red'] = red_list
    else:
        # Something is wrong.
        print("BOARD CANNOT BE CREATED")
        return

    # We just need to get the assassin now.
    assassin = input("Enter the assassin in all lowercase.")
    board['assassin'] = assassin

    return board

def flip_turns(current_turn):
    if current_turn == 2:
        return 1
    elif current_turn == 1:
        return 2
    else:
        print("CANNOT FLIP TURNS. CURRENT TURN IS INVALID")
        return -1
def convert_number_to_team(number):
    if number == 1:
        return 'red'
    elif number == 2:
        return 'blue'
    else:
        print("INVALID NUMBER")
        return -1

def get_scored_words():
    words_scored = []
    word = "init"
    while word != "DONE":
        word = input("Type in words that were scored during that round.  When finished, type in 'DONE'")
        if word != "DONE":
            words_scored.append(word)
    return words_scored

def remove_scored_words_from_board(board, scored_words):
    blue_board = board['blue']
    red_board = board['red']
    assassin = board['assassin']
    new_blue_board = []
    new_red_board = []
    for word in blue_board:
        if word not in scored_words:
            new_blue_board.append(word)
    for word in red_board:
        if word not in scored_words:
            new_red_board.append(word)
    new_board = {'red': new_red_board, 'blue': new_blue_board, 'assassin': assassin}
    return new_board
