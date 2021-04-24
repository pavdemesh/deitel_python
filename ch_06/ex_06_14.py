# Exercise 06_14 from Deitel: Intro to Python for CS

"""
Modify your coin tossing simulation from Exercise 5.31:
Update the bar plot dynamically as you flip the coin.
Use the techniques you learned in Section 6.4.2.
"""

import random
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns
import sys


def plot_update(current_frame, times_to_flip_coins, toss_frequencies):
    """
    Calculates and displays next frame of the animation
    :param current_frame: int, required param from FuncAnimation - number of current frame
    :param times_to_flip_coins: int, how many times the coin-flipping will be simulated
    :param toss_frequencies: Dictionary to keep track of total frequencies for each coin state.
    :return: Displays updated frame of the barplot. Returns None.
    """
    # Clear previous chart
    plt.cla()

    # Flip coin required number of times and update the dictionary with frequencies
    for i in range(times_to_flip_coins):
        current_flip = ["heads", "tails", "edge"][random.randrange(3)]
        toss_frequencies[current_flip] = toss_frequencies.get(current_flip, 0) + 1

    # Get lists of coin states and corresponding frequencies
    coin_states = list(toss_frequencies.keys())
    frequencies_per_coin_state = list(toss_frequencies.values())

    # Define whitegrid and plot chart with coin states and corresponding frequencies
    sns.set_style("whitegrid")
    my_chart = sns.barplot(x=coin_states, y=frequencies_per_coin_state, palette="bright")

    # Add title
    running_total_flips = (current_frame + 1) * times_to_flip_coins
    chart_title = f"Displaying Results for Frame No. {current_frame + 1}\nTotal Flips So Far: {running_total_flips}"
    my_chart.set_title(chart_title)

    # Add labels for x and y axes
    my_chart.set(xlabel='Coin State', ylabel='Frequency')

    # Add space above to accommodate text for each patch
    my_chart.set_ylim(top=max(frequencies_per_coin_state) * 1.10)

    for bar, frequency in zip(my_chart.patches, frequencies_per_coin_state):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text_above_bar = f"{frequency:,} times\n{frequency / sum(frequencies_per_coin_state):.1%}"
        my_chart.text(text_x, text_y, text_above_bar, fontsize=11, ha="center", va="bottom")


# Provide default values for 2 command line arguments
if len(sys.argv) == 1:
    sys.argv.append('5000')
    sys.argv.append('10')

# Define total number of frames and number of flips per frame based on cmd line arguments
number_total_frames = int(sys.argv[1])
number_flips_per_frame = int(sys.argv[2])

# Define dictionary to keep track of heads, tails and edges
coin_state_frequencies = dict()

# Draw window for the barplot
my_figure = plt.figure(f"Flipping the Coin {number_total_frames * number_flips_per_frame:,} Times")

my_animation = animation.FuncAnimation(my_figure, plot_update, frames=number_total_frames, interval=200, repeat=False,
                                       fargs=(number_flips_per_frame, coin_state_frequencies))

plt.show()
