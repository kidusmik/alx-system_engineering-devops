#!/usr/bin/python3
"""Subscribers module"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns number of subscribers"""
    user_agent = 'kidusmik'
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return 0

    data = r.json()['data']
    pages = data['children']
    page_data = pages[0]['data']
    return page_data['subreddit_subscribers']
