#!/usr/bin/python3
"""
Implements function for printing first 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ Prints title of first 10 hot posts for subreddit """
    if not isinstance(subreddit, str):
        print(None)
    url = 'https://www.reddit.com/r/'
    headers = {'User-Agent': __name__}
    cparams = {'limit': 10}
    t_list = []
    try:
        r = requests.get('{}{}/hot.json'.format(url, subreddit),
                         headers=headers,
                         params=cparams,
                         allow_redirects=False)
        r.raise_for_status()
        t_list = r.json().get('data').get('children')
    except requests.exceptions.RequestException as e:
        print(None)
    if t_list:
        for i in t_list:
            if not i.get('data').get('stickied'):
                print(i.get('data').get('title'))
    else:
        print(None)
