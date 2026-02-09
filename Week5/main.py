#bing - regex for aws key

import re
import os

# Sample keys
access_key = "AKIAIOSFODNN7EXAMPLE"
secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def check_for_key(text):
    # Regex patterns
    access_key_pattern = r'"(AKIA|ASIA)[A-Z0-9]{16}"'
    secret_key_pattern = r'"[A-Za-z0-9/+=]{40}"'

    return re.match(access_key_pattern, text) or re.match(secret_key_pattern, text)


directory = input("Enter a folder to scan for keys")

for root, dirs, files in os.walk(directory):
    print(root)
    for file in files:
        if file.endswith('.py'):
            try:
                with open(os.path.join(root, file)) as code:
                    lines = code.readlines()
                    for line in lines:
                        for token in line.split():
                            if check_for_key(token):
                                print(f"KEY FOUND IN {file}")
            except FileNotFoundError:
                pass



