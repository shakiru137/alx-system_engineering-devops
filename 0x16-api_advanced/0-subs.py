#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to find the number of subscribers for a given
    subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. If the subreddit
        is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if not response:
        return 0

    result = response.json()
    data = result.get("data")
    return data.get("subscribers", 0)
