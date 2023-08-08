#!/usr/bin/python3
""" This is a function that queries Reddit API recursively to count words."""


import requests


def count_words(subreddit, word_list, after='', word_dict=None):
""" This function querries Reddit API for word counts
"""
    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f'{word}: {count}')
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json()['data']
        posts = data['children']
        next_after = data['after']

        for post in posts:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict:
                word_dict[word] += lower.count(word)

    except Exception:
        return

    count_words(subreddit, word_list, next_after, word_dict)


# Example usage
# subreddit = 'example_subreddit'
# word_list = ['word1', 'word2', 'word3']
# count_words(subreddit, word_list)
