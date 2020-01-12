# -------------------------------------------------------------------------------
#   Description: This file provides methods for removing plural copies from the
#   reuslt set.  For instance, we do not want to suggest both "book" and "books".
#   We also want to avoid suggesting words which are the plural versions of words
#   found in the board.  For instance, saying "books" and a clue when "book" is on
#   the board is clearly against the rules, so those words should be avoided.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

import inflect
import helper_methods

# This method removes plural copies from the result set.
def remove_plural_copies(result_set):
    # We use the inflect library to get plural forms.
    p = inflect.engine()

    # trouble_indices will hold the indices that need to be removed.
    trouble_indices = []
    # The first step is to figure out which entries need to be removed from the result set.
    for first_index in range(0, len(result_set)):
        # If index is in trouble indices then move along.
        if first_index in trouble_indices:
            continue

        # If not... start by getting the word.
        word = result_set[first_index][0]

        # Get the plural opposite.  That is, if word is already plural, then the plural
        # opposite will be singular.
        plural_opposite = p.plural(word)

        # Figure out if and where the plural opposite shows up in result set.
        for second_index in range(0, len(result_set)):
            if plural_opposite == result_set[second_index][0]:
                # Then add it to trouble_indices.
                trouble_indices.append(second_index)

    # Now trouble_indices should contain the indices we need to remove from the result set.
    new_result_set = []
    for number in range(0, len(result_set)):
        if number not in trouble_indices:
            new_result_set.append(result_set[number])
    return new_result_set


# This method removes the plural versions of board words from the reuslt set.
def remove_board_words(board, result_set):
    # As before, we use inflect to get plural forms.
    p = inflect.engine()

    # Get a list of all the board words.
    board_words = helper_methods.get_board_words(board)

    # The first step is to pluralize all of the board words.
    plural_board_words = []
    for word in board_words:
        plural_word = p.plural(word)
        plural_board_words.append(plural_word)

    # Now, we need to go through and make sure that none are in our result set.
    trouble_indices = []
    for plural_word in plural_board_words:
        for index in range(0, len(result_set)):
            if plural_word == result_set[index][0]:
                trouble_indices.append(index)

    # Second, we go through the regular board words.
    for word in board_words:
        for index in range(0, len(result_set)):
            if (word == result_set[index][0]) and (index not in trouble_indices):
                trouble_indices.append(index)

    # Now we have the bad indices and we can remove them from the results set.
    new_result_set = []
    for num in range(0, len(result_set)):
        if num not in trouble_indices:
            new_result_set.append(result_set[num])
    return new_result_set
