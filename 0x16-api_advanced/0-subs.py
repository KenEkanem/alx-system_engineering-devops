#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscriber"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers (not active users, total
        subscribers) for a given subreddit
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            # Extract the JSON data from the response
            data = response.json()

            # extract subscribers from the JSON data
            subscribers = data["data"]["subscribers"]
            return subscribers
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
