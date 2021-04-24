# Exercise 06_16 from Deitel: Intro to Python for CS


"""
In this exercise, you’ll modify Chapter 4’s script that simulates the dice game craps.
The script should receive a command-line argument indicating the number of games of craps to execute.
Use two lists to track the total numbers of games won and lost on the first roll, second roll, third roll, etc.
Summarize the results as follows:
a) Display a horizontal bar plot indicating how many games are won and how many are lost
on the first roll, second roll, third roll, etc.
Since the game could continue indefinitely, you might track wins and losses through
the first dozen rolls (of a pair of dice),
then maintain two counters that keep track of wins and losses after 12 rolls—no matter how long the game gets.
Create separate bars for wins and losses.
"""

import random
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import statistics as stats
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


# If command line argument for number of games is not given, use default value = 1_000 games
if len(sys.argv) == 1:
    sys.argv.append("1000")

number_of_games = int(sys.argv[1])

# List to store winning and losing games, where [index] + 1 is the number of corresponding roll
winning_rolls_frequencies = [0] * 13
losing_rolls_frequencies = [0] * 13
number_of_rolls = list(range(1, 14))

# Run play(craps) required amount of time and update track of winning and losing rolls
for i in range(number_of_games):
    # Unpack play_craps() return value into game_outcome (True or False) and num_of_last_roll (int)
    game_outcome, num_of_last_roll = play_craps()

    # If game outcome is True == winning Craps
    if game_outcome:
        # Store winning roll number at indices 0 to 11 for rolls 1 to 12
        if num_of_last_roll - 1 <= 11:
            winning_rolls_frequencies[num_of_last_roll - 1] += 1
        # Store winning rolls number over 12 under index [12]
        else:
            winning_rolls_frequencies[12] += 1

    # If game_outcome is False, update track of losing rolls
    else:
        # Store losing rolls numbers at indices 0 to 11 for rolls 1 to 12
        if num_of_last_roll - 1 <= 11:
            losing_rolls_frequencies[num_of_last_roll - 1] += 1
        # Store losing rolls numbers over 12 under index [12]
        else:
            losing_rolls_frequencies[12] += 1

# Calculate and display the chances of winning:
total_games_won = sum(winning_rolls_frequencies)
winning_chance = total_games_won / number_of_games
print(f"The chance of winning at Craps is approx.: {winning_chance:.2%}")
print()

sns.set_style("whitegrid")

# Draw chart for wins
# wins_chart = sns.barplot(x=number_of_rolls, y=winning_rolls_frequencies, palette='bright')
# wins_chart_title = f"Winning at Craps Sorted by Roll after {number_of_games:,} Games"
# wins_chart.set_title(wins_chart_title)
# wins_chart.set(xlabel="Number of Winning Roll", ylabel="Games Won")

# Draw chart for losses
# loss_chart = sns.barplot(x=number_of_rolls, y=losing_rolls_frequencies, palette='bright')
# loss_chart_title = f"Losing at Craps Sorted by Roll after {number_of_games:,} Games"
# loss_chart.set_title(loss_chart_title)
# loss_chart.set(xlabel="Number of Losing Roll", ylabel="Games Lost")

# Draw combined chart for wins and losses
# Create pandas DataFrame based on game results
data_tuple = list(zip(number_of_rolls, winning_rolls_frequencies, losing_rolls_frequencies))
data_pd = pd.DataFrame(data_tuple, columns=["Ending Roll", "Wins", "Losses"])
data_pd = pd.melt(data_pd, id_vars="Ending Roll", var_name="Game Outcome", value_name="Frequencies")

# Draw Grouped Barchart
groped_chart = sns.barplot(x="Ending Roll", y="Frequencies", hue="Game Outcome", data=data_pd)

# Calculate total frequencies for ending game at rolls 1 through 12+
game_length_freqs_summarized = [sum(x) for x in zip(winning_rolls_frequencies, losing_rolls_frequencies)]

# Unpack aggregated frequencies into two lists of individual ending rolls
game_length_freqs_unpacked = []
for roll_num, freq in enumerate(game_length_freqs_summarized):
    game_length_freqs_unpacked.extend([roll_num + 1] * freq)

# Determine mean, mode and median
game_length_mean = stats.mean(game_length_freqs_unpacked)
game_length_mode = stats.mode(game_length_freqs_unpacked)
game_length_median = stats.median(game_length_freqs_unpacked)

# Display mean, mode and median
print(f"Mean of game length is: {game_length_mean:.2f}")
print(f"Median of game length is: {game_length_median:.2f}")
print(f"Mode of game length is: {game_length_mode}")

plt.show()
