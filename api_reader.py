import requests


def fetch_api_data(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
