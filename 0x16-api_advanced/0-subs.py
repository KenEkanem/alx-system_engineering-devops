#!/usr/bin/python3
"""
Module to fetch the number of subscribers for a given subreddit using the Reddit API.
If the subreddit is invalid, the function returns 0.
"""

from requests import get

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to retrieve the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The total number of subscribers if the subreddit exists.
             Returns 0 if the subreddit does not exist or if an error occurs.
    
    Example:
        >>> number_of_subscribers('programming')
        756024

        >>> number_of_subscribers('this_is_a_fake_subreddit')
        0
    """
    
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Define the User-Agent and the URL for the subreddit's JSON data
    user_agent = {"User-agent": "Google Chrome Version 81.0.4044.129"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Send the GET request to the Reddit API
    response = get(url, headers=user_agent)
    
    try:
        # Parse the JSON response and return the subscriber count
        results = response.json()
        return results.get("data").get("subscribers")
    
    except Exception:
        # If any error occurs (e.g., subreddit doesn't exist), return 0
        return 0
