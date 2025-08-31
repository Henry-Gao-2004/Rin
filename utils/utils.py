import requests
import ndjson

base_url = "http://localhost:11434"

def prompt_gpt(prompt: str, options = {}) -> requests.Response:
    url = base_url+"/api/chat"
    payload = {
        "model": "gpt-oss:20b",
        "messages": [
            {
                "role": "user",
                "content": prompt, 
                "options": options
            }
        ]
    }
    response = requests.post(url, json=payload)
    return response