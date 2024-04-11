#!/usr/bin/python3
"""
Implements function for printing first 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ Prints title of first 10 hot posts for subreddit """
    if not isinstance(subreddit, str):
        print(None)
    t_list = []
    try:
        r = requests.get('https://www.reddit.com/r/' + subreddit +
                         '/hot.json?limit=10',
                         headers={'User-Agent': '0-subs'},
                         allow_redirects=False)
        r.raise_for_status()
        t_list = r.json().get('data').get('children')
    except requests.exceptions.RequestException as e:
        print(None)
    if t_list:
        [print(i.get('data').get('title')) for i in t_list
         if not i.get('data').get('stickied')]
    else:
        print(None)
