import os
import praw
import time
import requests
import pandas
from dotenv import load_dotenv , find_dotenv
from validator_collection import validators , checkers

#TODO FIX URL VALIDATOR
##########################################################
# def is_string_a_url(url: str) -> bool:
#     '''
#     Check for URL validity
#     '''
#     print(url)

#     try:
#         checking = requests.get(url , timeout=5)
#         checking.raise_for_status()
#         return True

#     except requests.exceptions.HTTPError:
#         return False


# while True:
#         subreddit = input("Input the name of the desired subreddit:\n")
#         url = (f"https://www.reddit.com/r/{subreddit}/")

#         if not is_string_a_url(url):
#             continue

#         url = validators.url(url)
#########################################################


# Get .env info
load_dotenv(find_dotenv())

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
reddit_name = os.getenv("reddit_name")
password = os.getenv("password")
user_agent = os.getenv("user_agent")


# Instantiate API instance
reddit = praw.Reddit(client_id=client_id ,
                    client_secret=client_secret ,
                    reddit_name=reddit_name ,
                    password=password ,
                    user_agent=user_agent)


subreddits = ("Wallstreetbets", "Stocks", "Osugame", "Greentext", "Idiotsincars", "Unexpected", "Mademesmile")

BREAKER = True

#Pick a subreddit
while BREAKER:
    print(subreddits)
    chosen_subreddit = input(f"Pick one of the {len(subreddits)} subreddits above:\n").title()

    for sub in subreddits:
        if chosen_subreddit == sub:
            BREAKER = False
            break

#Number of searches API will make
while True:
    limit_amount = int(input("How many posts would you like to search? (MUST BE BETWEEN 15 - 10000): "))
    if 15 <= limit_amount <= 10000:
        break

    print("Please input a value between 15 and 10000")



get_subreddit = reddit.subreddit(chosen_subreddit)

top_subreddit = get_subreddit.top(limit=limit_amount)



if chosen_subreddit == "Stocks" or "Wallstreetbets":

    STOCKS : list[str] = []
    COUNTING = 1

    for submission in top_subreddit:

        time.sleep(0.0250)

        COUNTING += 1

        if not submission.stickied:

            submission_name = submission.title.split()

            for word in submission_name:
                if len(word) == 3 and word.isupper() and word.isalpha():
                    STOCKS.append(word)

    print(f"TOTAL SUBMITTIONS: {COUNTING}")

    counting_stocks = {stock: STOCKS.count(stock) for stock in STOCKS}

    sorting_stocks = dict(sorted(counting_stocks.items(), key=lambda item: item[1]))

    for stock in sorting_stocks:
        print(stock , sorting_stocks[stock])

