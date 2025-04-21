import json
import requests

from google import genai

client = genai.Client(api_key="AIzaSyB2TfE1Q-grcmH3CclAX5Lwf8rHP8fr0pA")

natural_language = "'everthing looks too big. I don't like it'"

commands = "[change_theme, increase_font_size, decrease_font_size, increase_volume, decrease_volume]"

query = commands + """
    each word in the square bracket represents a command that addresses a problem.
    Analyse the statement below and return the most appropriate command that addresses 
    the problem. Note, return only the command and nothing else
    """ + natural_language 



def make_request():
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=query
    )
    print("==========> " + response.text)
    return response.text

make_request()




# url = "http://localhost:11434/api/chat"

# natural_language = "'everything here is too small. I don't like it'"

# commands = "[change_theme, increase_font_size, decrease_font_size, increase_volume, decrease_volume]"

# query = commands + """
#     each word in the square bracket represents a command that addresses a problem.
#     Analyse the statement below and return the most appropriate command that addresses 
#     the problem. Note, return only the command and nothing else
#     """ + natural_language 





# payload = {
#     "model": "stable-code",
#     "messages": [{"role": "user", "content": query}]
# }


# def make_request():
    # response = requests.post(url, json=payload, stream=True)
    # full_response = ""

    # for line in response.iter_lines():
    #     if line:
    #         try:
    #             data = json.loads(line.decode("utf-8"))
    #             content = data.get("message", {}).get("content")
    #             if content:
    #                 # print(content, end="", flush=True)
    #                 full_response += content
    #         except json.JSONDecodeError:
    #             continue
    # print("\n\nFull response:\n", full_response)
    # return full_response 