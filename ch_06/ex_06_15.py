# Exercise 06_15 from Deitel: Intro to Python for CS

"""
Modify your simulation of rolling two dice from Exercise 5.32:
Update the bar plot dynamically as you roll the dice.
Use the techniques you learned in Section 6.4.2.
"""

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import sys


def plot_update(current_frame, num_rolls_to_make, rolls_frequencies):
    """
    Updates the barplot via FuncAnimation.
    :param current_frame: Int, number of current frame being processed
    :param num_rolls_to_make: Int, how many times to roll two dice
    :param rolls_frequencies: Dict, contains two-dice sums and their frequencies
    :return: Updated barplot.
    """
    # Clear the axes
    plt.cla()

    # Roll two dices required number of times, on each roll calculate sum and update the frequencies dict
    for i in range(num_rolls_to_make):
        current_roll_sum = random.randrange(1, 7) + random.randrange(1, 7)
        rolls_frequencies[current_roll_sum] = rolls_frequencies.get(current_roll_sum, 0) + 1

    # Define style, draw barplot, define axes labels and chart title
    sns.set_style("whitegrid")
    my_frame = sns.barplot(x=[rolls_frequencies[k] for k in sorted(rolls_frequencies.keys())],
                           y=sorted(rolls_frequencies.keys()), orient="horizontal", palette="bright")
    my_frame.set(xlabel="Frequencies", ylabel="Two-Dice Sums")
    title = f"Displaying Frame No. {current_frame + 2}\nTotal Rolls so far: {sum(rolls_frequencies.values()):,}"
    my_frame.set_title(title)

    # Provide additional space to the right to accommodate annotations
    my_frame.set_xlim(right=max(rolls_frequencies.values()) * 1.15)

    # Calculate coordinates for and display annotations
    for bar, frequency in zip(my_frame.patches, [rolls_frequencies[k] for k in sorted(rolls_frequencies.keys())]):
        text = f"{frequency:,}\n{frequency / sum(rolls_frequencies.values()):.2%}"
        text_x = bar.get_width() + 1
        text_y = bar.get_y() + bar.get_height() / 2.0
        my_frame.text(text_x, text_y, text, ha="left", va="center")


# Provide default value for the total number of frames to be displayed
# Provide default value for the number of two-dice rolls per frame
if len(sys.argv) == 1:
    sys.argv.append("600")
    sys.argv.append("100")

# Get total number of frames and rolls per frame from provided command line arguments
total_num_frames = int(sys.argv[1])
rolls_per_frame = int(sys.argv[2])

# Create empty dict tto store frequencies of rolled two-dice sums
two_dice_sums_frequencies = {}

# Draw window for the chart
my_window = plt.figure(f"Rolling Two Dice {total_num_frames * rolls_per_frame:,} Times")

# Define FuncAnimation to draw the animation
my_animation = animation.FuncAnimation(my_window, plot_update, frames=total_num_frames, repeat=False, interval=33,
                                       fargs=(rolls_per_frame, two_dice_sums_frequencies))

plt.show()
