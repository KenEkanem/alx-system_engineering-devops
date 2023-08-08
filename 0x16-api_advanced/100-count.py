#!/usr/bin/python3
"""recursive function that queries the Reddit API,
    parses the title of all hot articles,
    prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """function that prints a sorted count of given keywords from the hot
        articles titles parsed
    """
    if word_count is None:
        word_count = {}

    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
                               subreddit, after)

    headers = {
        "User-Agent": "ubuntu"
    }
    try:
        # Send the HTTP GET request
        response = requests.get(url, headers=headers,
                                allow_redirects=False)

        # Check the response status code
        if response.status_code == 200:
            # Extract the JSON data from the response
            data = response.json()

            # Extract the posts from the JSON data
            posts = data["data"]["children"]

            # Extract the after value for pagination
            after = data["data"]["after"]

            # Count the occurrences of keywords in the titles
            for post in posts:
                title = post["data"]["title"].lower()
                for word in word_list:
                    if word.lower() in title:
                        if word not in word_count:
                            word_count[word] = 1
                        else:
                            word_count[word] += 1

            # If there is an after value, recursively call the function
            if after:
                return count_words(subreddit, word_list, after=after,
                                   word_count=word_count)
            else:
                # Print the results in descending count order,
                # then alphabetically
                sorted_words = sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0].lower()))
                for word, count in sorted_words:
                    print("{}: {}".format(word.lower(), count))

        else:
            return None
    except requests.exceptions.RequestException:
        return None
