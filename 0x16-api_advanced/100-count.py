#!/usr/bin/python3
"""
Implements function for printing first 10 hot posts for a given subreddit
"""
import requests


def count_words(subreddit, word_list, after=None, hot_count={}):
    """ Prints title of first 10 hot posts for subreddit """
    if not isinstance(subreddit, str):
        return hot_list
    url = 'https://www.reddit.com/r/'
    headers = {'User-Agent': __name__}
    cparams = {'limit': 100}
    if not hot_count:
        hot_count = {word: 0 for word in word_list}
    if after:
        cparams['after'] = after
    t_list = []
    try:
        r = requests.get('{}{}/hot.json'.format(url, subreddit),
                         headers=headers,
                         params=cparams,
                         allow_redirects=False)
        r.raise_for_status()
        t_list = r.json().get('data').get('children')
        after = r.json().get('data').get('after')
    except requests.exceptions.RequestException as e:
        pass

    if t_list:
        t_list = [i.get('data').get('title') for i in t_list
                  if not i.get('data').get('stickied')]
        for title in t_list:
            for word in word_list:
                if word in title:
                    hot_count[word] = hot_count[word] + 1
        count_words(subreddit, word_list, after, hot_count)
    else:
        for word, count in hot_count.items():
            print('{}: {}'.format(word, count))
