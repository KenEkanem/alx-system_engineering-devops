#!/usr/bin/python3

"""
Function that queries the Reddit API and returns the number of subscribers 
for a given subreddit, handling both existing and non-existing subreddits.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: Number of subscribers, or 0 if the subreddit does not exist, 
         there is an error, or the input is invalid.
    """
    if not isinstance(subreddit, str) or subreddit == '' or ' ' in subreddit:
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data.get("data", {}).get("subscribers", 0)
            return subscribers
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Reddit API: {e}")
        return 0


if __name__ == "__main__":
    # Example subreddits for testing
    subreddits = ["python", "nonexistentsubreddit123"]

    for subreddit in subreddits:
        subscribers = number_of_subscribers(subreddit)
        if subscribers > 0:
            print(f"Output: Existing Subreddit '{subreddit}' has {subscribers} subscribers.")
        else:
            print(f"Output: Non-existing Subreddit '{subreddit}' or an error occurred.")
