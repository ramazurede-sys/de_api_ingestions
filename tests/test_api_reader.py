import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from api_reader import fetch_api_data


def test_fetch_api_data():
    data = fetch_api_data("https://jsonplaceholder.typicode.com/posts")
    assert isinstance(data, list)
    assert len(data) > 0