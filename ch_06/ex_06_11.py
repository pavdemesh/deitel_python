# Exercise 06_11 from Deitel: Intro to Python for CS
import random

"""
Modify the script of Fig. 4.2 to play 1,000,000 games of craps.
Use a wins dictionary to keep track of the number of games won for a particular  number of rolls.
Similarly, use a losses dictionary to keep track of the number of games lost for a particular number of rolls.
As the simulation proceeds, keep updating the  dictionaries.
A typical key–value pair in the wins dictionary might be {4: 50217}
indicating that 50217 games were won on the 4th roll.

Display a summary of the results including:
a) the percentage of the total games played that were won.
b) the percentage of the total games played that were lost.
c) the percentages of the total games played that were won or lost on a given roll (column 2 of the sample output).
d) the cumulative percentage of the total games played that were won or lost up to and including a given number of rolls
(column 3 of the sample output).

Percentage of wins: 50.2%
Percentage of losses: 49.8%

Percentage of wins/losses based on total number of rolls
Rolls   % Resolved on this roll     Cumulative% of games resolved
1       30.10%                      30.10%
2       20.80%                      50.90%
3       14.10%                      65.00%
4       9.90%                       74.90%
5       7.40%                       82.30%
6       4.60%                       86.90%
7       3.70%                       90.60%
8       2.40%                       93.00%
9       1.90%                       94.90%
10      1.10%                       96.00%
11      0.90%                       96.90%
12      0.80%                       97.70%
13      0.80%                       98.50%
14      0.30%                       98.80%
15      0.30%                       99.10%
16      0.30%                       99.40%
17      0.50%                       99.90%
25      0.10%                       100.00%
"""


# Simulating the dice game Craps.
def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2  # pack die face values into a tuple


def play_craps():
    """
    Plays one game of craps
    :return: A tuple containing True if won else False AND number of resolving roll as int
    """
    roll_counter = 1
    my_point = 0
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

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        roll_counter += 1
        die_values = roll_dice()
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'

    # display "wins" or "loses" message
    if game_status == 'WON':
        return True, roll_counter
    else:
        return False, roll_counter


# Define the number of games to be played
number_of_games = 1_000_000
# Create dictionaries to hold game results
wins = {}
loss = {}

# Play craps 1_000_000 times and update counts of winning and losing rolls
for i in range(number_of_games):
    has_won, resolving_roll = play_craps()
    if has_won:
        wins[resolving_roll] = wins.get(resolving_roll, 0) + 1
    else:
        loss[resolving_roll] = loss.get(resolving_roll, 0) + 1

# Display percentage of wins
print(f"Percentage of wins: {sum(wins.values()) / number_of_games:.2%}")

# Display percentage of losses
print(f"Percentage of losses: {sum(loss.values()) / number_of_games:.2%}")

# Display summarizing table
print("Percentage of wins/losses based on total number of rolls:\n")
print(f"{'% Resolved':>22}{'% Cumulative':>20}")
print(f"{'Rolls': >6}{'on this roll':>16}{'of games resolved':>20}")

cumulative_games_resolved = 0

# Iterate over sorted set of unique resolving roll numbers
for roll in sorted(set(wins.keys()).union(loss.keys())):
    # Calculate number of games resolved on current roll: wins + losses on current roll
    games_resolved_on_current_roll = wins.get(roll, 0) + loss.get(roll, 0)
    # Update total number of games resolved so far
    cumulative_games_resolved += games_resolved_on_current_roll

    # Calculate percentage for current roll and cumulative percentage so far
    percent_resolved_on_current_roll = games_resolved_on_current_roll / number_of_games
    percent_resolved_cumulative = cumulative_games_resolved / number_of_games

    # Display roll number, % of games resolved on this roll, cumulative % of games resolved so far
    print(f"{roll:>6}{percent_resolved_on_current_roll:>16.4%}{percent_resolved_cumulative:>20.4%}")
