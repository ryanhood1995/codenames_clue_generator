# -------------------------------------------------------------------------------
#   Description: This file is the main driver of the entire program.  Changing the
#   board will affect the outcomes given.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

import gensim
import play_game

# ----------------------------
# -----------MAIN-------------
# ----------------------------

# First, load the model that contains the web of connections.
model = gensim.models.KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin.gz', binary=True, limit=500000
)

# Now it is time to choose the 'game-mode'.  The options are in the play_game.py file.
play_game.get_quick_suggestions(model)
