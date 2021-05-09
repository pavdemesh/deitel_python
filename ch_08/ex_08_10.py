# Exercise 08_10 from Deitel: Intro to Python and CS

"""
Search online for lists of positive sentiment words and negative sentiment words.
Create a script that inputs text, then determines whether that text is positive or negative,
based on the total number of positive words and the total number of negative words.
Test your script by searching for Twitter tweets on a topic of your choosing, then entering the text for several tweets.
"""

import numpy as np
import pandas as pd
import random

# Import txt files containing positive / negative words into corresponding numpy arrays
positive_words = np.loadtxt("ex_08_10_positive_words.txt", dtype=str)
negative_words = np.loadtxt("ex_08_10_negative_words.txt", dtype=str)


def is_text_positive(text, positives, negatives):
    """
    Determines if the text is positive or negative connoted.
    :param text: String of words.
    :param positives: NumPy array of positive words.
    :param negatives: NumPy array of negative words.
    :return: True if text is positive else False.
    """
    # Convert text to a list of individual words
    words_from_tweet = text.split()

    # Initialize counters for positive and negative words
    count_positives = 0
    count_negatives = 0

    # Iterate over words, check against lists of pos/neg and update corresponding counters
    for word in words_from_tweet:
        if word in positives:
            count_positives += 1
        elif word in negatives:
            count_negatives += 1
        else:
            continue

    # Display result
    return count_positives > count_negatives


# Load positive and negative tweets into 2 NumPy arrays
tweets_positive = np.loadtxt("ex_08_10_tweets_positive.txt", dtype=str, delimiter="\n")
tweets_negative = np.loadtxt("ex_08_10_tweets_negative.txt", dtype=str, delimiter="\n")

# Convert arrays into pandas Series
ds_tweets_positive = pd.Series(tweets_positive)
ds_tweets_negative = pd.Series(tweets_negative)

# Clean negative tweets
ds_tweets_negative = ds_tweets_negative.str.replace(r"[.,'()?!]+", "", regex=True)
ds_tweets_negative = ds_tweets_negative.str.lower().str.strip()

# Clean positive tweets
ds_tweets_positive = ds_tweets_positive.str.replace(r"[.,'()?!]+", "", regex=True)
ds_tweets_positive = ds_tweets_positive.str.lower().str.strip()

# Join positive and negative tweets into one Series
ds_tweets = pd.concat([ds_tweets_negative, ds_tweets_positive], ignore_index=True)

# Check 100 randomly selected tweets:
for i in range(1, 101):
    tweet_index = random.randrange(ds_tweets.size)
    tweet_text = ds_tweets[tweet_index]
    print(f"Tweet No. {i:0>3}: {tweet_text}")
    print(f"The above mentioned tweet is: "
          f"{'Positive' if is_text_positive(tweet_text, positive_words, negative_words) else 'Negative (or Neutral)'}")
    print("----------------------")