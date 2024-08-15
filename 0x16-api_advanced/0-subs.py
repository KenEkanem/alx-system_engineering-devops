#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
to return the number of subscribers for a given subreddit.
The function returns 0 if the subreddit doesn't exist.
"""

import requests


def number_of_subscribers(subreddit):
    """ 
    Queries the Reddit API and returns the number of subscribers
    for a subreddit. Returns 0 if the subreddit doesn't exist.
    """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    data = res.json()
    if 'data' not in data or 'subscribers' not in data['data']:
        return 0
    return data['data']['subscribers']
