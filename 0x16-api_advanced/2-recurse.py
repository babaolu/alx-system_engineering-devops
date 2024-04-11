#!/usr/bin/python3
"""
Implements function for printing first 10 hot posts for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Prints title of first 10 hot posts for subreddit """
    if not isinstance(subreddit, str):
        return hot_list
    url = 'https://www.reddit.com/r/'
    headers = {'User-Agent': __name__}
    cparams = {'limit': 100}
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
        hot_list.extend([i.get('data').get('title') for i in t_list
                        if not i.get('data').get('stickied')])
        recurse(subreddit, hot_list, after)
    return hot_list
