# -------------------------------------------------------------------------------
#   Description: This file takes the words_and_scores and formats it into a final
#   recommendations list.
#
#   There are two methods:
#       scores_to_suggestions: This method sorts the scores from high to low, so that
#           the best suggestions are presented first.  Since the lists involved are so
#           short, runtime considerations are ignored.
#       scores_to_complete_suggestions: The only difference here is the score becomes
#           part of the suggestions so the user knows what number to say when giving
#           their clues.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

def scores_to_suggestions(words_and_scores):
    suggestions = []

    while len(words_and_scores[1]) != 0:
        # First, we need to find index of max score.
        index_max = max(range(len(words_and_scores[1])), key=words_and_scores[1].__getitem__)

        # Now, add the word with that index to suggestions, and then remove the elements with that index in both lists.
        suggestions.append(words_and_scores[0][index_max])
        del words_and_scores[0][index_max]
        del words_and_scores[1][index_max]

    return suggestions

def scores_to_complete_suggestions(words_and_scores):
    complete_suggestions = []

    while len(words_and_scores[1]) != 0:
        index_max = max(range(len(words_and_scores[1])), key=words_and_scores[1].__getitem__)

        # The only difference is with the below line of code.  The score as a string is concatenated with the suggestion.
        complete_suggestions.append(words_and_scores[0][index_max] + " " + str(words_and_scores[1][index_max]))
        del words_and_scores[0][index_max]
        del words_and_scores[1][index_max]

    return complete_suggestions
