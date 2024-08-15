#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
to return the number of subscribers for a given subreddit.
The function returns 0 if the subreddit doesn't exist.
"""

import requests
import logging

logging.basicConfig(level=logging.DEBUG)

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a subreddit."""
    u_agent = 'Mozilla/5.0 (compatible; my_script/0.1; +http://mywebsite.com)'
    headers = {
        'User-Agent': u_agent
    }

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            logging.debug(f"Request failed with status code: {res.status_code}")
            return 0
        data = res.json()
        if 'data' not in data or 'subscribers' not in data['data']:
            logging.debug("Response missing 'data' or 'subscribers' key")
            return 0
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return 0
