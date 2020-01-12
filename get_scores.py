# -------------------------------------------------------------------------------
#   Description: This file takes refined result sets, and produces a score for each
#   word suggested.  This score is a measure of how highly the program recommends that
#   particular word.  The SCORE_THRESHOLD determines how correlated a board word must be
#   to a suggested word to be considered related.
#
#   Why is this score required?
#       The previous method that created the result set also gave a correlation score which
#       indicated how well it matched to the board words.  One may think this is a good measure
#       to determine which words to recommend, but this system has one big flaw: it doesn't
#       prioritize making connections with as many words as possible.  Instead it prioritizes
#       making very strong connections with one or two words.  Since we would prefer a lot of weak
#       connections over a small amount of strong connections, we need to come up with a different
#       scoring scheme.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

# If it is too hard to connect suggested words to the board words, raise this number.
SCORE_TRESHOLD = 0.2

# This method takes a refined result set and the board words and gets a score for each result set
# word.  A list of list is returned.  The first list in the outer list containes the words.  The
# second list in the outer list contains the scores.
def get_scores(model, result_set, board_words):
    words = []
    scores = []

    # For every word in the result set...
    for tup in result_set:
        # Go ahead and append it to the words list.
        words.append(tup[0])
        # Assign a temporary score of 0.
        score = 0

        # Now go through every word in the board words.
        for word in board_words:
            # Try to get a similarity score between the result set word and board word.
            # Similarity scores are from -1 to 1.
            try:
                similarity = model.similarity(tup[0], word)
            # Some words which were previously recommended by our model are not valid words in the
            # similarity method.  Only strange words or non word abbreviations (like asx) are not valid.
            # In those cases, give them a similarity score of 0, which will put them at the end of the
            # recommendations, which is OK.
            except:
                similarity = 0

            # Now if the similarity score is greater than the threshold, we add one to the score to indicate
            # that there is an additional connection between the result set word and the words on the board.
            if similarity > SCORE_TRESHOLD:
                score = score + 1
        # Append the score to the scores list.
        scores.append(score)

    # Form a list of list containing the words and scores.
    words_and_scores = [words, scores]
    return words_and_scores
