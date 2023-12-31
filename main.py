"""This code is written by the Author Saif Chishti. It can be used by anyone who have access to it."""

# Import required libraries
import requests
import sys


def function():
    for word in sys.stdin:
        # Replace the URL under with the api URl to be tested.
        response = requests.get(url=f"https://api.example.com/{word}")
        if response.status_code == 404:
            loop()
        else:
            data = response.json()
            print(data)
            print(response.status_code)
            print(word)


function()

# For any query feel free to contact.
