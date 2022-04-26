#!/usr/bin/python3
"""Top 10 Module"""

import requests


def top_ten(subreddit):
    """Queries Reddit API and prints top ten hot posts of the subreddit
    """
    user_agent = 'kidusmik'
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        print('None')
    else:
        data = r.json()['data']
        posts = data['children']
        for post in posts:
            print(post['data']['title'])
