#!/usr/bin/python3
"""
Implements function for printing first 10 hot posts for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """ Prints title of first 10 hot posts for subreddit """
    if not isinstance(subreddit, str):
        return hot_list
    url = 'https://www.reddit.com/r/'
    t_list = []
    try:
        if url in subreddit:
            r = requests.get(subreddit, headers={'User-Agent': '0-subs'},
                             allow_redirects=False)
        else:
            subreddit = url + subreddit + '/hot.json?limit=1'
            r = requests.get(subreddit, headers={'User-Agent': '0-subs'},
                             allow_redirects=False)
        r.raise_for_status()
        t_list = r.json().get('data').get('children')
    except requests.exceptions.RequestException as e:
        pass

    if t_list:
        hot_list.append(t_list[0].get('data').get('title'))
        subreddit = subreddit[:subreddit.find('?')]
        post_id = t_list[0].get('kind') + '_' + t_list[0].get('data').get('id')
        subreddit = subreddit + "?limit=1&after=" + post_id
        recurse(subreddit, hot_list)
    return hot_list
