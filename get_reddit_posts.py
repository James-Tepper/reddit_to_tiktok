import os
import praw
import requests
import time
import settings
import shutil
from text_to_speech import get_audio
from validator_collection import validators, checkers
import random

__author__ = "James Tepper <jamesatepper@gmail.com>"
__github__ = "https://github.com/James-Tepper"

VOICEOVERS_PATH = f"/mnt/c/Users/James/OneDrive/Desktop/Voiceovers/"

USED_POSTS = {}
USED_COMMENTS = {}

def get_subreddit_name():
    '''
    Gets a random subreddit name from a list of subreddits
    '''
    subreddits = ("Jokes", "Showerthoughts", "TellMeAFact", "TIFU", "TodayILearned")
    
    chosen_subreddit = subreddits[random.randint(0, len(subreddits) - 1)]
    
    return chosen_subreddit


def find_and_read_post(reddit, chosen_subreddit):
    '''
    Gets Reddit Title and Submission
    Reads them aloud
    If post exceeds 260 words, skip
    '''
    subreddit = reddit.subreddit(chosen_subreddit)
    hot_posts = subreddit.hot(limit=10)

    for post in hot_posts:
        if not post.stickied and not post.over_18:
        # and not post in used_posts
            #TODO RECORD
            title_audio = get_audio(post.id, post.title, format="title")
            post_audio = get_audio(post.id, post.selftext, format="post")
            
            shutil.copy(title_audio, VOICEOVERS_PATH)
            shutil.copy(post_audio, VOICEOVERS_PATH)

            get_comments_from_post(post)

def get_comments_from_post(post):
    for amount, comment in enumerate(post.comments):
        if len(comment.body.split()) < 100:
            comment_audio = get_audio(comment.id, comment.body, format="comment")
            shutil.copy(comment_audio, VOICEOVERS_PATH)
            
            if amount > 5:
                return

def main():
    reddit = praw.Reddit(client_id=settings.CLIENT_ID,
                         client_secret=settings.CLIENT_SECRET,
                         reddit_name=settings.REDDIT_NAME,
                         password=settings.PASSWORD,
                         user_agent=settings.USER_AGENT)

    chosen_subreddit = get_subreddit_name()
    find_and_read_post(reddit, chosen_subreddit)



if __name__ == "__main__":
    main()
