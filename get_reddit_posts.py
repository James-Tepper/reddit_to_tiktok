import os
import praw
import requests
import time
import settings
from text_to_speech import read_aloud_and_print
from validator_collection import validators, checkers


__author__ = "James Tepper <jamesatepper@gmail.com>"
__github__ = "https://github.com/James-Tepper"



def get_subreddit_name():
    # TODO: use https://www.reddit.com/subreddits/popular.json perhaps?

    subreddits = ("Jokes" , "Showerthoughts", "Confessions", "Pettyrevenge", "Prorevenge")

    while True:
        print(subreddits)
        chosen_subreddit = input(f"Pick one of the {len(subreddits)} subreddits and create your Tiktok:\n").title()

        if not chosen_subreddit in subreddits:
            print("INVALID INPUT")
            continue

        return chosen_subreddit



def find_and_read_post(reddit, chosen_subreddit):
    '''
    Gets Reddit Title and Submission
    Reads them aloud
    If post exceeds 260 words, skip
    '''
    subreddit = reddit.subreddit(chosen_subreddit)
    hot_posts = subreddit.hot(limit=10)

    for posts in hot_posts:
        if not posts.stickied:
            post_title = posts.title
            post_body = posts.selftext

            if 60 <= len(post_body.split()) <= 260:
                read_aloud_and_print(post_title, post_body)
                audio_and_text_post = read_aloud_and_print(post_title, post_body)
            else:
                print("Submission is invalid")

    return audio_and_text_post



def main():
    reddit = praw.Reddit(client_id=settings.CLIENT_ID,
                         client_secret=settings.CLIENT_SECRET,
                         reddit_name=settings.REDDIT_NAME,
                         password=settings.PASSWORD,
                         user_agent=settings.USER_AGENT)

    chosen_subreddit = get_subreddit_name()
    find_and_read_post(reddit, chosen_subreddit)



if __name__ == "__main__": # https://www.youtube.com/watch?v=g_wlZ9IhbTs
    main()
