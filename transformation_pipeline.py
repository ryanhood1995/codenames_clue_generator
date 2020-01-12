# -------------------------------------------------------------------------------
#   Description: The raw words outputted by the model have a lot of issues with them.
#   To remove the issues, a series of transformations is performed.  The goal of this
#   file is to perform all of the transformations in sequence, thus forming a pipeline.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

import simple_transformations
import plural_transformations
import assassin_transformations

# This method takes the board, the result set outputted by the model, and the bad set
# of words relating to the assassin and performs every transformation needed.  The
# output is the new and improved result set.
def full_pipeline(board, result_set, bad_set):
    # First, we want to perform all of the transformations on our result set.
    result_set = simple_transformations.keep_single_words(result_set)
    result_set = simple_transformations.set_lowercase(result_set)
    result_set = simple_transformations.remove_repeats(result_set)
    result_set = plural_transformations.remove_plural_copies(result_set)
    result_set = plural_transformations.remove_board_words(board, result_set)

    # Then, we want to perform most of the transformations on our bad set.  We do not perform the last two because we want our bad set to contain
    # as many variations as it can contain.
    bad_set = simple_transformations.keep_single_words(bad_set)
    bad_set = simple_transformations.set_lowercase(bad_set)
    bad_set = simple_transformations.remove_repeats(bad_set)

    # Now our bad set is ready to be contrasted with our good set.
    result_set = assassin_transformations.remove_bad_words(result_set, bad_set)

    return result_set
