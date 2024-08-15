#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0  # Subreddit does not exist
        if response.status_code != 200:
            return 0  # Handle other errors (e.g., 500, 403)
        
        # Parse the JSON response
        data = response.json().get("data")
        if not data or "subscribers" not in data:
            return 0  # Handle case where 'subscribers' key is missing
        
        return data.get("subscribers", 0)
    
    except requests.RequestException:
        return 0  # Handle network-related errors

# Example usage:
# print(number_of_subscribers("nonexistingsubreddit"))  # Should return 0
