#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a gven subreddit.
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts for a given subreddit"""

    # intializes the reddit api client
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Extract the JSON data from the response
            data = response.json()

            # extract posts from the JSON data
            posts = data["data"]["children"]

            # print titles of the posts
            for post in posts:
                print(post["data"]["title"])
        else:
            print('None')
    except requests.exceptions.RequestException as e:
        print("Error:", e)
