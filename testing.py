import praw
import pandas as pd

creds = []

with open('not_a_secret_key','r') as fp:
    for line in fp:
        words = line.strip().split()
        creds.append(words[1])

reddit = praw.Reddit(client_id=creds[0], client_secret=creds[1], user_agent=creds[2],
                    username=creds[3], password=creds[4])
subreddit = reddit.subreddit('FloridaMan')

# top all-time
# Reddit’s request limit* is 1000
for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)