import requests
from bs4 import BeautifulSoup
import ollama

OLLAMA_API = "http://localhost:11434/api/chat"
HEADER = {"Content-Type": "application/json"}
MODEL = "llama3.2"

if __name__ == "__main__":
  messages = [
    {"role": "user", "content": "Describe some of business applications of Generative AI."}
  ]

  # Web request to Ollama API
  # payload = {
  #   "model": MODEL,
  #   "messages": messages,
  #   "stream": False
  # }

  # response = requests.post(OLLAMA_API, json=payload, headers=HEADER)
  # print(response.json()['message']['content'])

  # Using Ollama Python SDK
  response = ollama.chat(model=MODEL, messages=messages)
  print(response['message']['content'])
