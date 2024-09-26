#!/usr/bin/python3
""" A script to fetch number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers """

    headers = {'user-agent': 'My user agent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        if response.status_code == 200:
            data = response.json()
            subs = data.get('data').get('subscribers')
            return subs
        elif response.status_code == 429:
            # handle rate limit
            print('Rate limited, try again later')
        elif response.status_code == 403:
            # handle forbidden
            print(f'HTTP Status code: {response.status_code}')
    except requests.RequestException as e:
        print(f'Error occured: {e}')

    return 0
