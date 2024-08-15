#!/usr/bin/python3
"""
Function that queries Reddit API and prints
the 1st-ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """ function that queries Reddit API and prints the titles
    of the 1st-ten hot posts listed for a  subreddit """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    dictn = response.json()
    hot_post = dictn['data']['children']
    if len(hot_post) is 0:
        print(None)
    else:
        for post in hot_post:
            print(post['data']['title'])
