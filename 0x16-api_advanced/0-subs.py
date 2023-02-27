#!/usr/bin/pyhton3
"""a function that queries the Reddit API and returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns the number of subscribers"""
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers={'User-Agent': 'My User Agent 1.0'}, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
