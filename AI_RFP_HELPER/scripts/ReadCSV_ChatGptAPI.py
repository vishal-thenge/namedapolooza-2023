import csv
import openai

# Set your OpenAI API key here
openai.api_key = "YOUR_KEY/env variable"


def read_csv(filename):
    messages = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            message = row['Questions'].strip()
            if message:
                messages.append({'role': 'user', 'content': message})
    return messages

def chat_gpt_api_call(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-3.5-turbo" for faster response times
        messages=messages
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    csv_filename = 'questions.csv'
    messages = read_csv(csv_filename)

    if messages:
        api_response = chat_gpt_api_call(messages)
        print(api_response)
    else:
        print("No messages found in the CSV file.")
