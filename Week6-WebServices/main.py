#bing python dot env

from dotenv import load_dotenv
import os

import urllib.request
import json



# Load variables from the .env file
load_dotenv()

# Access variables
API_KEY = os.getenv('API_KEY')

print(f'API_KEY: {API_KEY}')


def get_json_from_url(url):

    # try and get from dictionary cache
    if url in results:
        return results[url]

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

results = {}

if os.path.exists('results.json'):
    with open('results.json') as results_file:
        results = json.load(results_file)



url = f"https://api.massive.com/v3/reference/tickers?ticker=MSFT&market=stocks&active=true&order=asc&limit=100&sort=ticker&apiKey={API_KEY}"
json_data = get_json_from_url(url)

results[url] = json_data

if json_data is not None:
    print(json.dumps(json_data, indent=4))  # Pretty-print JSON
else:
    print("Failed to fetch JSON.")

with open('results.json', 'w') as results_file:
    json.dump(results, results_file, indent=4)

