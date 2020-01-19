# -------------------------------------------------------------------------------
#   Description: The raw words outputted by the model have a lot of issues with them.
#   To remove the issues, a series of transformations is performed.  The goal of this
#   file is to perform all of the transformations in sequence, thus forming a pipeline.
#
#   Author: Ryan Hood (ryanchristopherhood@gmail.com)
# -------------------------------------------------------------------------------

import helper_methods
import get_result_set
import get_scores
import get_final_suggestions

FIRST_NUM_WORDS = 9
SECOND_NUM_WORDS = 8

def play_two_sided_game(model):
    # Get team who's going first.
    going_first = input("Who is going first? Enter either 'red' or 'blue'")
    going_first_num = helper_methods.convert_team_to_number(going_first)

    # Get the board.  First get blue words.
    board = helper_methods.create_board(going_first, FIRST_NUM_WORDS, SECOND_NUM_WORDS)

    current_turn = going_first_num
    while ((len(board['red']) != 0) and (len(board['blue']) != 0)):
        print("It is now ", helper_methods.convert_number_to_team(current_turn), "'s turn.")

        if current_turn == 1:
            result_set = get_result_set.get_red_result_set(model, board)
        elif current_turn == 2:
            result_set = get_result_set.get_blue_result_set(model, board)
        else:
            print("CANNOT GET RESULT SET.")

        scores = get_scores.get_scores(model, result_set, board[helper_methods.convert_number_to_team(current_turn)])

        suggestions = get_final_suggestions.scores_to_complete_suggestions(scores)

        print("Here are suggested words:")
        print(suggestions)

        # Determine which words need to be removed from the board.
        all_scored_words = helper_methods.get_scored_words()

        # Now, words scored contains all of the words we need to remove from the board.
        board = helper_methods.remove_scored_words_from_board(board, all_scored_words)

        # Change the turns.
        current_turn = helper_methods.flip_turns(current_turn)

        # Determine Winner.
        if len(board['red']) == 0:
            print("The Winner is Red Team.  Thanks for playing!")
        if len(board['blue']) == 0:
            print("The Winner is Blue Team.  Thanks for playing!")

def play_one_sided_game(model):
    # Get the team.
    team = input("Which team are you on? Type 'red' or 'blue'.")
    team_num = helper_methods.convert_team_to_number(team)

    # Get team going first.
    going_first = input("Who is going first? Enter either 'red' or 'blue'")
    going_first_num = helper_methods.convert_team_to_number(going_first)

    # Get the board.
    board = helper_methods.create_board(going_first, FIRST_NUM_WORDS, SECOND_NUM_WORDS)

    current_turn = going_first_num
    while ((len(board['red']) != 0) and (len(board['blue']) != 0)):
        if current_turn == team_num:
            print("It is your team's turn.  Below are the recommended words.")
            if team_num == 1:
                result_set = get_result_set.get_red_result_set(model, board)
            elif team_num == 2:
                result_set = get_result_set.get_blue_result_set(model, board)
            else:
                print("ERROR: RESULT SET CANNOT BE GATHERED.")
            scores = get_scores.get_scores(model, result_set, board[team])
            suggestions = get_final_suggestions.scores_to_complete_suggestions(scores)
            print(suggestions)

            # Determine which words need to be removed from the board.
            all_scored_words = helper_methods.get_scored_words()

            # Now, words scored contains all of the words we need to remove from the board.
            board = helper_methods.remove_scored_words_from_board(board, all_scored_words)

            # Change the turns.
            current_turn = helper_methods.flip_turns(current_turn)
        else:
            print("It is the other team's turn.")
            # Determine which words need to be removed from the board.
            all_scored_words = helper_methods.get_scored_words()
            # Now, words scored contains all of the words we need to remove from the board.
            board = helper_methods.remove_scored_words_from_board(board, all_scored_words)
            # Change the turns.
            current_turn = helper_methods.flip_turns(current_turn)
        # Determine Winner.
        if len(board['red']) == 0:
            print("The Winner is Red Team.  Thanks for playing!")
        if len(board['blue']) == 0:
            print("The Winner is Blue Team.  Thanks for playing!")

def get_quick_suggestions(model):
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
