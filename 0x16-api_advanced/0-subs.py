#!/usr/bin/python3
""" Implements function for number of subscribers for a given subreddit """
import requests


def number_of_subscribers(subreddit):
    """ Returns number of subscribers for subreddit """
    try:
        r = requests.get('https://www.reddit.com/r/' + subreddit +
                         '/about.json',
                         headers={'User-Agent': '0-subs'})
        r.raise_for_status()
        return r.json().get('data').get('subscribers')
    except requests.exceptions.RequestException as e:
        return 0
