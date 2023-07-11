import pip._vendor.requests
from sitepackages.dotenv import load_dotenv,find_dotenv
import json
import os

def main():
    source_language = input("Please choose the source language:(English, Luganda, Runyankole, Ateso, Lugbara or Acholi)\n")
    if source_language == "English":
        target_language = input ("Please choose the target language:(Luganda, Runyankole, Ateso, Lugbara or Acholi)\n")
        text = input("Enter the text to translate\n")
    else:
        target_language = "English"
        text = input("Enter the text to translate\n") 

    url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'
    load_dotenv(find_dotenv())
    api_key = os.environ.get("APIKEY")

    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "source_language": source_language,
        "target_language": target_language,
        "text": text
    }

    response = pip._vendor.requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

    if response.status_code == 200:
        translated_text = response.json()["text"]
        print("Translate text:", translated_text)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__": 
    respond = "yes"
    while respond == "yes":
        main()
        response = input("Do you wish to continue translating\n")
