# -------------------------------------------------------------------------------
#   Description: This file provides the most basic transformations that are to be
#   applied to the result set to improve it.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

# This method remove words in the result set such as "high_five".
# It also removes "words" that have numbers in them, such as "V8"
def keep_single_words(result_set):
    new_list = []
    for index in range(0, len(result_set)):
        # If the word is composed of only alphabetical letters...
        if result_set[index][0].isalpha():
            # ...then it's a good word and needs to stay in the list.
            new_list.append(result_set[index])
    return new_list

# This method sets all of the words to all lowercase. For example,
# "America" would become "america".
def set_lowercase(result_set):
    new_list = []
    for index in range(0, len(result_set)):
        old_word = result_set[index][0]
        # Make a new word which is all lowercase.
        new_word = old_word.lower()
        # To the new tuple, add the new lowercase word and the old score.
        new_tuple = (new_word, result_set[index][1])
        # Append the new tuple to our new list.
        new_list.append(new_tuple)
    return new_list

# This method removes one copy of words that are identical, so that only one
# copy of repeating words remains.
def remove_repeats(result_set):
    new_result_set = []
    # A word bank will hold all words that have been seen.
    word_bank = []
    for tup in result_set:
        if tup[0] not in word_bank:
            new_result_set.append(tup)
            word_bank.append(tup[0])
    return new_result_set
