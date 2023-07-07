import requests
import json

source_language = input("Please choose the source language:(English, Luganda, Runyankole, Ateso, Lugbara or Acholi)\n")
if source_language == "English":
    target_language = input ("Please choose the target language:(Luganda, Runyankole, Ateso, Lugbara or Acholi)\n")
    text = input("Enter the text to translate")
elif source_language == "Luganda":
    target_language = "English"
    text = input("Enter the text to translate")
elif source_language == "Runyakole":
    target_language = "English"
    text = input("Enter the text to translate")
elif source_language == "Ateso":
    target_language = "English"
    text = input("Enter the text to translate")
elif source_language == "Lugbara":
    target_language = "English"  
    text = input("Enter the text to translate")
elif source_language == "Acholi":
    target_language = "English"
    text = input("Enter the text to translate")
else:
    print("Do not recognise language")

url = 'https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app'

headers = {
    "Authorization": "Bearer {eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJJbnRlcm5zaGlwcyIsImV4cCI6NDg0MTQ4NzEyMn0.-j3rdudJ9pXEm3-456LLiDPun5SwIm5sw-RoNvgDwfk}",
    "Content-Type": "application/json"
}

payload = {
  "source_language": source_language,
  "target_language": target_language,
  "text": text
}

response = requests.post(f"{url}/tasks/translate", headers=headers, json=payload)

if response.status_code == 200:
    translated_text = response.json()["text"]
    print("Translate text:", translated_text)
else:
    print("Error:", response.status_code, response.text)