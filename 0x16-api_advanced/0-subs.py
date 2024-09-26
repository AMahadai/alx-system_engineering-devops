#!/usr/bin/python3
""" A script to fetch number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers """

    headers = {'user-agent': 'My user agent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subs = data.get('data').get('subscribers')
        return subs
    else:
        return(0)
