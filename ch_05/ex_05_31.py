"""
Simulate the flipping a coin. Use randomly generated 1s and 2s to represent heads and tails, respectively.
Initially, do not include the frequencies and percentages above the bars.
Then modify your code to include the frequencies and percentages.
Run simulations for 200, 20,000 and 200,000 coin flips.
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

coin_flips = [["heads", "tails", "edge"][random.randrange(3)] for x in range(200_000)]

# Get unique ratings and their frequencies both as ndarrays
coin_states, coin_states_frequencies = np.unique(coin_flips, return_counts=True)

# Define whitegrid and plot my chart
sns.set_style("whitegrid")
my_chart = sns.barplot(x=coin_states, y=coin_states_frequencies, palette="bright")

# Add title
chart_title = f"Tossing a Coin {len(coin_flips):,} Times"
my_chart.set_title(chart_title)

# Add labels for x and y axes
my_chart.set(xlabel='Coin State', ylabel='Frequency')

# Add space above to accommodate text for each patch
my_chart.set_ylim(top=max(coin_states_frequencies) * 1.10)

for bar, frequency in zip(my_chart.patches, coin_states_frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text_above_bar = f"{frequency:,} times\n{frequency / len(coin_flips):.1%}"
    my_chart.text(text_x, text_y, text_above_bar, fontsize=11, ha="center", va="bottom")

plt.show()
