#!/usr/bin/python3
"""
    function that queries the Reddit API
    and prints the titles of the first 10 hot posts listed
    for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
        queries the Reddit API
        and prints the titles of the first 10 hot posts
    """
    redit_url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(redit_url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for i in range(10):
            print(data[i].get('data').get('title'))
    else:
        print(None)
