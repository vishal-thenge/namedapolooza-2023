# In main.py
import os
import json
from scripts import AI_CALL

token = "";

def read_data_from_file():
    # Get the current script directory
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Define the data file path
    data_file_path = os.path.join(script_dir, 'data', 'data.txt')

    # Open the file and read the data
    with open(data_file_path, 'r') as file:
        data = file.read()

    return data

# Read the data from the file

context = read_data_from_file()
# If the data is in JSON format, convert it to a Python dictionary

body = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": context
        },
        {
            "role": "user",
            "content": "how is snyk data encrypted? "
        }
    ]
}

# call the function
AI_CALL.make_post_request(token,
                          'https://api.openai.com/v1/chat/completions', body)
