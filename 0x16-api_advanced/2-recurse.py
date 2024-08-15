#!/usr/bin/python3
"""
A function that queries Reddit API and prints
the 1st-ten hot posts of a specific subreddit
"""
import requests


def add_title(hot_list, hot_post):
    """ This function adds an item into a list """
    if len(hot_post) == 0:
        return
    hot_list.append(hot_post[0]['data']['title'])
    hot_post.pop(0)
    add_title(hot_list, hot_post)


def recurse(subreddit, hot_list=[], after=None):
    """ This function queries Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dicn = res.json()
    hot_post = dicn['data']['children']
    add_title(hot_list, hot_post)
    after = dicn['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
