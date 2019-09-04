import praw
import pandas as pd

# Reddit’s request limit* is 1000
# promoted posts are filtered out, automatically


def get_credits(file_name='not_a_secret_key'):
    creds = []
    with open(file_name,'r') as fp:
        for line in fp:
            words = line.strip().split()
            creds.append(words[1])
    return creds

def get_reddit(cred):
    reddit = praw.Reddit(client_id=creds[0], client_secret=creds[1], user_agent=creds[2],
                    username=creds[3], password=creds[4])
    return reddit

def get_subreddit(reddit,subreddit='FloridaMan'):
    sub = reddit.subreddit(subreddit)
    return sub

def print_hot_comments(submission, number_of_comments=5):
    '''
    print the requested number of top commnets
    '''
    for comment in submission.comments[:number_of_comments]:
        print('{}\' comment: \t{}'.format(comment.author, comment.body))
        print()


# topics_dict = { "title":[], 
#                 "score":[], 
#                 "id":[], "url":[], 
#                 "comms_num": [], 
#                 "created": [], 
#                 "body":[]}
# top all-time
# for submission in subreddit.top(limit=1):
#     # print(submission.title, submission.id)
#     topics_dict["title"].append(submission.title)
#     topics_dict["score"].append(submission.score)
#     topics_dict["id"].append(submission.id)
#     topics_dict["url"].append(submission.url)
#     topics_dict["comms_num"].append(submission.num_comments)
#     topics_dict["created"].append(submission.created)
#     topics_dict["body"].append(submission.selftext)

if __name__ == "__main__":
    creds = get_credits()
    reddit = get_reddit(creds)
    # subreddit = reddit.subreddit('worldnews')
    subreddit = get_subreddit(reddit)
    all_time_top_10_posts = []
    for submission in subreddit.top(limit=10):
        print(submission.title)
        if not submission.stickied:
            all_time_top_10_posts.append(submission.title)
    # top_10_df = pd.DataFrame(all_time_top_10_posts)
    # top_10_df.to_csv('top_10_florida_man.csv', index=False) 