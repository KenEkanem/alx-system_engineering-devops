#!/usr/bin/python3

"""Function that queries the Reddit API and returns the number of subscribers for a given subreddit."""
import requests  # 'r' comes before 's' so we import 'requests' before any other 's' imports


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: Number of subscribers, or 0 if the subreddit does not exist, there is an error, or the input is invalid.
    """

    # Ensure the subreddit name is valid (non-empty and contains no invalid characters)
    if not isinstance(subreddit, str) or subreddit == '' or ' ' in subreddit:
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            # Extract the JSON data from the response
            data = response.json()

            # Extract subscribers from the JSON data
            subscribers = data.get("data", {}).get("subscribers", 0)
            return subscribers
        else:
            return 0
    except requests.exceptions.RequestException as e:
        # Log the error message here for debugging
        print(f"Error fetching data from Reddit API: {e}")
        return 0


if __name__ == "__main__":
    subreddit = "python"  # Example subreddit
    subscribers = number_of_subscribers(subreddit)
    print(f"The number of subscribers for the subreddit '{subreddit}' is: {subscribers}")
