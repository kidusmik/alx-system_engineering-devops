#!/usr/bin/python3
"""Recurse It Module"""

import requests


def recurse(subreddit, hot_list=[], next_page=None, count=0):
    """recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit
    """
    user_agent = 'kidusmik'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if next_page:
        url += '?after={}'.format(next_page)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return None
    data = r.json()['data']
    posts = data['children']
    for post in posts:
        count += 1
        hot_list.append(post['data']['title'])

    next_page = data['after']
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    else:
        return hot_list
