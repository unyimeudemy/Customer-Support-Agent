import json
import requests


url = "http://localhost:11434/api/chat"

natural_language = "'everything here is too small. I don't like it'"

commands = "[change_theme, increase_font_size, decrease_font_size, increase_volume, decrease_volume]"

query = commands + """
    each word in the square bracket represents a command that addresses a problem.
    Analyse the statement below and return the most appropriate command that addresses 
    the problem. 
    """ + natural_language 

payload = {
    "model": "stable-code",
    "messages": [{"role": "user", "content": query}]
}

def make_request():
    response = requests.post(url, json=payload, stream=True)
    full_response = ""

    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                content = data.get("message", {}).get("content")
                if content:
                    # print(content, end="", flush=True)
                    full_response += content
            except json.JSONDecodeError:
                continue
    print("\n\nFull response:\n", full_response)
    return full_response 