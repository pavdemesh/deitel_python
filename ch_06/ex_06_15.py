# Exercise 06_15 from Deitel: Intro to Python for CS

"""Modify the script RollDie.py that we provided with this chapter’s examples to simulate rolling two dice.
Calculate the sum of the two values.
Each die has a value from 1 to 6, so the sum of the values will vary from 2 to 12,
with 7 being the most frequent sum, and 2 and 12 the least frequent.
If you roll the dice 36,000 times:
• The values 2 and 12 each occur 1/36th (2.778%) of the time, so you should expect about 1000 of each.
• The values 3 and 11 each occur 2/36ths (5.556%) of the time, so you should expect about 2000 of each, and so on.
Use a command-line argument to obtain the number of rolls.
Display a bar plot summarizing the roll frequencies.
The following screen captures show the final bar plots for sample executions of 360, 36,000 and 36,000,000 rolls.
Use the Seaborn barplot function’s optional orient keyword argument to specify a horizontal bar plot.
"""

import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys


if len(sys.argv) == 1:
    sys.argv.append("36000")

two_dice_rolls = [random.randrange(1, 7) + random.randrange(1, 7) for x in range(int(sys.argv[1]))]

roll_sums, sums_frequencies = np.unique(two_dice_rolls, return_counts=True)

sns.set_style("whitegrid")

my_chart = sns.barplot(y=roll_sums, x=sums_frequencies, palette="bright", orient="horizontal")
title = f"Rolling Two Dice {len(two_dice_rolls):,} Times"
my_chart.set_title(title)
my_chart.set(xlabel="Frequency", ylabel="Two Dice Sum")

my_chart.set_xlim(right=max(sums_frequencies) * 1.1)

for bar, frequency in zip(my_chart.patches, sums_frequencies):
    text_x_coord = bar.get_width() * 1.01
    text_y_coord = bar.get_y() + 0.5 * bar.get_height()
    text = f'{frequency:,}\n{frequency / len(two_dice_rolls):.1%}'
    my_chart.text(text_x_coord, text_y_coord, text, fontsize=10, va="center", ha="left")

plt.show()
