#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all hot articles
        for a given subreddit.
        If no results are found for the given subreddit,
        the function should return None.
    """

    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
                               subreddit, after)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()

            # Extract the posts from the JSON data
            posts = data["data"]["children"]

            # Extract the after value for pagination
            after = data["data"]["after"]

            # Add the titles of the posts to the hot_list
            for post in posts:
                hot_list.append(post["data"]["title"])

            # If there is an after value, recursively call the function
            if after is not None:
                return recurse(subreddit, hot_list, after=after)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
