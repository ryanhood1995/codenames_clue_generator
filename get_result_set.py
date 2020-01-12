# -------------------------------------------------------------------------------
#   Description: This file performs the full pipeline on the initial result set
#   to obtain a new result set.  Either one result set is desired (red or blue),
#   or both result sets are desired.  This file contains a method for every option.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

import transformation_pipeline
import assassin_transformations

# This method gets both results sets.
def get_both_result_sets(model, board):
    # First, get the raw result set for blue.  To get the raw result set, positive contribution
    # are added from blue cards and negative contributions are subtracted from the red cards.
    # This discourages the model from suggesting a word relating to another teams cards.
    result_set_blue = model.most_similar(
        positive=board['blue'],
        negative=board['red'],
        restrict_vocab=50000,
        topn=50
    )

    # Then the raw results for red.
    result_set_red = model.most_similar(
        positive=board['red'],
        negative=board['blue'],
        restrict_vocab=50000,
        topn=50
    )

    # We use the assassin to get the bad set.
    bad_set = assassin_transformations.get_bad_words(model, board['assassin'])

    # Now we perform the full pipeline on both result sets.  The outputs are better result sets!
    result_set_blue = transformation_pipeline.full_pipeline(board, result_set_blue, bad_set)
    result_set_red = transformation_pipeline.full_pipeline(board, result_set_red, bad_set)

    # Combine the better result sets into a dictionary.
    results_dict = {'blue': result_set_blue, 'red': result_set_red}
    return results_dict

def get_red_result_set(model, board):

    result_set_red = model.most_similar(
        positive=board['red'],
        negative=board['blue'],
        restrict_vocab=50000,
        topn=50
    )

    bad_set = assassin_transformations.get_bad_words(model, board['assassin'])

    result_set_red = transformation_pipeline.full_pipeline(board, result_set_red, bad_set)
    return result_set_red

def get_blue_result_set(model, board):

    result_set_blue = model.most_similar(
        positive=board['blue'],
        negative=board['red'],
        restrict_vocab=50000,
        topn=50
    )

    bad_set = assassin_transformations.get_bad_words(model, board['assassin'])

    result_set_blue = transformation_pipeline.full_pipeline(board, result_set_blue, bad_set)
    return result_set_blue
