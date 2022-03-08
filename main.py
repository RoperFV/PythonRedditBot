# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("amitheasshole")

for submission in subreddit.hot(limit=10):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("URL: ", submission.url)
    print("---------------------------------\n")
    print("---------------------------------\n")