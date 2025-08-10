import requests
import ndjson

base_url = "http://localhost:11434"

def prompt_gpt(prompt, options = {}):
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
    if response.status_code == 200:
        result = ndjson.loads(response._content)
        response_text = ""
        for item in result:
            if item['message']['role'] == 'assistant':
                response_text = response_text+ item['message']['content']
        return True, response_text.strip()
    else:
        return False, response.status_code