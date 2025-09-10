import requests
import ndjson

base_url = "http://localhost:11434"

def prompt_gpt(prompt: str, options = {}) -> requests.Response:
    """
    use ollama to access the gpt-oss:20b model deployed locally
    prompt: str, the prompt to send to the model
    options: dict, additional options to pass to the model
    return: requests.Response, the response from the model
    """
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
    """
    Convert the response from the model output to text.
    response: requests.Response, the response from the model
    return: str, the text output from the model
    """
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