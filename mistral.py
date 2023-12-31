import sys
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os


if sys.argv[1]:
    model_type = sys.argv[1]
else:
    model_type = "small"

print("Enter Mistral Prompt:")
user_content = input()

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def get_mistral_response(user_content):
    api_key = open_file("mistralai_key.txt")
    model = "mistral-" + model_type
    client = MistralClient(api_key=api_key)
    
    messages = [ChatMessage(role="user", content=user_content)]
    
    chat_response = client.chat(model=model, messages=messages)
    
    try:
        response_content = chat_response.choices[0].message.content if chat_response.choices else ""
    except AttributeError as e:
        print(f"Error occurred: {e}")
        response_content = ""
    
    return response_content


if __name__ == "__main__":
    response = get_mistral_response(user_content)
    print(response)

