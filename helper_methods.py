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
