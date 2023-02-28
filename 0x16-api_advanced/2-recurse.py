#!/usr/bin/python3
"""
    recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        recursive function that queries the Reddit API
        and returns a list containing the titles of all
        hot articles for a given subreddit.
    """
    redit_url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after}
    response = requests.get(redit_url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for i in range(len(data)):
            hot_list.append(data[i].get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
