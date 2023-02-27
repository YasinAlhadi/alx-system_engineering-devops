#!/usr/bin/pyhton3
"""
    a function that queries the Reddit API
    and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    redit_url = 'https://api.reddit.com/r/{}/about'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(redit_url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
