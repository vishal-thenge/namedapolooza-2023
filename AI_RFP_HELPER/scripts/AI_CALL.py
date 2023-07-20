import requests
import json
import os
def make_post_request(token, endpoint, body):
    # Set the headers
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    # Make the POST request
    response = requests.post(endpoint, headers=headers, data=json.dumps(body))

    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful.")
        print("Response: " + response.text)
    else:
        print("Request not successful.")
        print("Status code: " + str(response.status_code))
        print("Error: " + response.text)

