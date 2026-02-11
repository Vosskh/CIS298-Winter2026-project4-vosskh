

# bing - python urllib get json

import urllib.request
import json


def get_json_from_url(url):
    """
    Fetch JSON data from a given URL using urllib.
    Returns a Python object (dict/list) if successful, None otherwise.
    """
    try:
        # Open the URL
        with urllib.request.urlopen(url) as response:
            # Check for HTTP success
            if response.status != 200:
                print(f"Error: HTTP {response.status}")
                return None

            # Read and decode the response
            data = response.read().decode('utf-8')

            # Parse JSON safely
            try:
                return json.loads(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return None

    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None



test_url = "https://pokeapi.co/api/v2/pokemon/ditto"  # Public API returning JSON
json_data = get_json_from_url(test_url)

if json_data is not None:
    print("Fetched JSON successfully:")
    print(json.dumps(json_data, indent=4))  # Pretty-print JSON
else:
    print("Failed to fetch JSON.")