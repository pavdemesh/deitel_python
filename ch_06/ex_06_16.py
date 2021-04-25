# Exercise 06_16 from Deitel: Intro to Python for CS


"""
Reimplement
your solution to Exercise 5.33, using the techniques you learned in Section 6.4.2
to create a dynamic bar chart showing the wins and losses on the first roll, second roll, third
roll, etc.
"""

import random
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import matplotlib.animation as animation
import pandas as pd


# Define helper functions for the game of Craps
def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2  # pack die face values into a tuple


def play_craps():
    """
    Plays one party of Craps
    :return: Tuple: (True, number of winning rolls) or (False, number of losing roll)
    """
    my_point = 0
    counter_rolls = 1
    die_values = roll_dice()  # first roll

    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11):  # win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        # print('Point is', my_point)

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        sum_of_dice = sum(die_values)
        counter_rolls += 1

        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'

    # display "wins" or "loses" message
    if game_status == 'WON':
        return True, counter_rolls
    else:
        return False, counter_rolls


# If command line argument are not given, use default values = 600 frames with 100 games per frame
if len(sys.argv) == 1:
    sys.argv.append("600")
    sys.argv.append('100')

# Define total nums of frames for the animation and number of games per frame
total_of_frames = int(sys.argv[1])
games_per_frame = int(sys.argv[2])

# List to store winning and losing games, where [index] + 1 is the number of corresponding roll
winning_rolls_frequencies = {k: 0 for k in range(1, 14)}
losing_rolls_frequencies = {k: 0 for k in range(1, 14)}


def plot_update(current_frame, num_games_to_play, wins, loss):
    """
    Updates barplot for displaying winning and losing frequencies for each resolving (ending) roll
    :param current_frame: Int, current frame number to be processed
    :param num_games_to_play: Int, how many times to simulate craps for this frame
    :param wins: Dict, contains {winning_roll: frequency} pairs
    :param loss: Dict, contains {losing_roll: frequency} pairs
    :return: Updated barchart
    """
    # Clear axes
    plt.cla()

    # Simulate game of craps required num of times and update dictionaries with frequencies
    for i in range(games_per_frame):
        # Unpack play_craps() return value into game_outcome (True or False) and num_of_last_roll (int)
        game_outcome, num_of_last_roll = play_craps()

        # If game outcome is True == winning Craps
        if game_outcome:
            # Update dictionary of wins for rolls 1 through 12
            if num_of_last_roll <= 12:
                wins[num_of_last_roll] += 1
            # Summarize all winning roll numbers over 12 under key {13}
            else:
                wins[13] += 1

        # If game_outcome is False, update frequencies of losing rolls
        else:
            # Store losing rolls numbers 1 through 12
            if num_of_last_roll <= 12:
                loss[num_of_last_roll] += 1
            # Store losing rolls numbers over 12 under key {13}
            else:
                loss[13] += 1

    # Draw combined chart for wins and losses
    # Create pandas DataFrame based on game results
    data_tuples = list(zip(range(1, 14), [wins[k] for k in range(1, 14)], [loss[k] for k in range(1, 14)]))
    data_pd = pd.DataFrame(data_tuples, columns=["Ending Roll", "Wins", "Losses"])
    data_pd = pd.melt(data_pd, id_vars="Ending Roll", var_name="Game Outcome", value_name="Frequencies")

    # Draw Grouped Barchart
    grouped_chart = sns.barplot(x="Ending Roll", y="Frequencies", hue="Game Outcome", data=data_pd)
    grouped_chart.set_title(f"Displaying Results for Frame No. {current_frame + 1}")


my_window = plt.figure(f"Outcomes of Craps Based on {total_of_frames * games_per_frame:,} Games")
my_animation = animation.FuncAnimation(my_window, plot_update, frames=total_of_frames, repeat=False, interval=33,
                                       fargs=(games_per_frame, winning_rolls_frequencies, losing_rolls_frequencies))

plt.show()
