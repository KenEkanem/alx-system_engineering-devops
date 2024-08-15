#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
to return the number of subscribers for a given subreddit.
The function returns 0 if the subreddit doesn't exist.
"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subs = data.get('data').get('subscribers')
        return subs
    else:
        return 0
