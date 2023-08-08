#!/usr/bin/python3
"""
2-recurse
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API recursively and returns a list containing the titles of all hot articles for a given subreddit."""
    headers = {
        'User-Agent': 'MyRedditBot'
    }

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else None

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']
        if after:
            recurse(subreddit, hot_list, after)

        return hot_list
    else:
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")

