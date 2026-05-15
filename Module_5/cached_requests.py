import requests

requests_cache = {}

def get(url, *args, **kwargs):
    if url in requests_cache:
        print(f"Fetching URL from cache: {url}")
        return requests_cache[url]
    else:
        print(f"Fetching URL: {url}")
        response = requests.get(url, *args, **kwargs)
        requests_cache[url] = response
        return response
    

def __getattr__(attr):
    return getattr(requests, attr)
