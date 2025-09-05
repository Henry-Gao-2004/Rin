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

def response_to_text(response: requests.Response) -> str:
    if response.status_code != 200:
        return False, f"Error: {response.status_code}, {response.text}"
    try:
        data = response.json()
        if "choices" in data and len(data["choices"]) > 0:
            return True, data["choices"][0]["message"]["content"]
        else:
            return False, "Error: No choices in response"
    except Exception as e:
        return False, f"Error parsing response: {str(e)}"