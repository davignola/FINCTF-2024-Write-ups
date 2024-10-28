import requests
import string
import time

# Base URL with placeholders
base_url = "https://github.com/S1llyG00se/CheeseStealer/commit/?!dc"

# Possible characters (alphanumeric)
characters = string.ascii_letters + string.digits

# Iterate over all possible combinations of two missing characters
for char1 in characters:
    for char2 in characters:
        # Construct the URL
        url = base_url.replace('?', char1).replace('!', char2)
        
        response = requests.get(url)
        
        # Invalid URL gives 404
        if response.status_code == 200:
            print(f"Valid URL: {url}")
            break
        
        # Sleep a bit, rate limiter will be angry
        time.sleep(0.05)

