#!/usr/bin/python3
""" Module for storing the count_words function. """

import requests

def count_words(subreddit, word_list, word_count=[], page_after=None):
    headers = {'User-Agent': 'HolbertonSchool'}

    word_list = [word.lower() for word in word_list]

    if bool(word_count) is False:
        for word in word_list:
            word_count.append(0)

    if page_after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        r = requests.get(url, headers=headers, allow_redirects=False)
        
        if r.status_code == 200:
            for child in r.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1

            if r.json()['data']['after'] is not None:
                count_words(subreddit, word_list, word_count, r.json()['data']['after'])
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, page_after)
        r = requests.get(url, headers=headers, allow_redirects=False)

        if r.status_code == 200:
            for child in r.json()['data']['children']:
                i = 0
                for i in range(len(word_list)):
                    for word in [w for w in child['data']['title'].split()]:
                        word = word.lower()
                        if word_list[i] == word:
                            word_count[i] += 1
                    i += 1
            if r.json()['data']['after'] is not None:
                count_words(subreddit, word_list, word_count, r.json()['data']['after'])
            else:
                # Create a dictionary to store word counts
                dicto = {}
                
                # Calculate word counts considering duplicates
                for key_word in list(set(word_list)):
                    i = word_list.index(key_word)
                    if word_count[i] != 0:
                        dicto[key_word] = word_count[i]
                
                # Sort the dictionary based on counts and then alphabetically
                sorted_dicto = dict(sorted(dicto.items(), key=lambda item: (-item[1], item[0])))

                # Print the sorted word counts
                for key, value in sorted_dicto.items():
                    print('{}: {}'.format(key, value))
