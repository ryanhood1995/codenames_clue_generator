# -------------------------------------------------------------------------------
#   Description: This file is the main driver of the entire program.  Changing the
#   board will affect the outcomes given.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

import gensim
import get_result_set
import json
import get_scores
import get_final_suggestions

# ----------------------------
# -----------MAIN-------------
# ----------------------------

# First, load the model that contains the web of connections.
model = gensim.models.KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin.gz', binary=True, limit=500000
)

# Input the board.
board = {
    'blue': [
        'berry', 'opera', 'day', 'plastic',
        'undertaker', 'tower', 'fan', 'stream'
    ],
    'red': [
        'kangaroo', 'stock', 'centaur', 'web',
        'crane', 'europe', 'jack', 'engine', 'bottle'
    ],
    'assassin': 'helicopter'
}

# Get the "result set" which is a set of words that are most related to the board words.
result_set = get_result_set.get_both_result_set(model, board)

# Convert the result set into scores for each word in the result set.
blue_scores = get_scores.get_scores(model, both_result_sets['blue'], board['blue'])
red_scores = get_scores.get_scores(model, both_result_sets['red'], board['red'])

# Use the scores to get the final suggestions.
blue_suggestions = get_final_suggestions.scores_to_complete_suggestions(blue_scores)
red_suggestions = get_final_suggestions.scores_to_complete_suggestions(red_scores)

# Display those suggestions.
print("BLUE SUGGESTIONS:")
print(blue_suggestions)

print("RED SUGGESTIONS")
print(red_suggestions)
