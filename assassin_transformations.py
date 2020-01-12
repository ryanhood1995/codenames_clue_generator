# -------------------------------------------------------------------------------
#   Description: This file provides some methods of imporving the result set by
#   avoiding words relating to the assassin.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

# This method uses the model to get the top 1000 words relating to the assassin.
def get_bad_words(model, assassin):
    bad_set = model.similar_by_word(assassin, topn=1000)
    return bad_set

# This method takes a result set and a bad set and removes words from the result set
# that are in the bad set.
def remove_bad_words(result_set, bad_set):
    # We create a fresh result_set.
    new_result_set = []

    # Outer loop is result set.
    for tup_good in result_set:
        # Assume there will not be a match initially.
        there_is_match = False
        # Inner loop is bad set.
        for tup_bad in bad_set:
            if tup_good[0] == tup_bad[0]:
                # If the words agree, then there is a match.
                there_is_match = True
        # After comparing a good word with all of the bad words...
        if not there_is_match:
            # If there is no match, the good word can stay in the result set.
            new_result_set.append(tup_good)
    return new_result_set
