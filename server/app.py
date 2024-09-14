from flask import Flask
import requests
import os
import asyncio
import aiohttp
import dotenv
from flask import Flask, request
from VoiceflowHandler import delete_cache

app = Flask(__name__)
cachedURL  = ""

@app.route("/parseurl", methods=['POST'])
def recieve_url() -> None:
    url = request.args.get("url")
    if url == "":
        raise ValueError("Empty URL")
    elif not url_is_cached(url):
        delete_cache()
        cachedURL = url
    # ELSE: DO NOT DO ANYTHING AND DO NOT DISPLAY INJECTED BUTTON

def url_is_cached(url: str) -> bool:
    return cachedURL.strip() == url.strip()

if __name__ == '__main__':
    app.run(use_reloader=True, port=5525, threaded=True, host="0.0.0.0", debug=True)
    

def upload_files_to_voiceflow(directory: str) -> [str]:
    # get the API key from the .env file
    dotenv.load_dotenv()
    VOICEFLOW_API_KEY = os.getenv('VOICEFLOW_API_KEY')

    responses = []
    url = "https://api.voiceflow.com/v1/knowledge-base/docs/upload?maxChunkSize=1000"

    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            filename = filename.split('.')[-1] + '.txt'
            
            with open(file_path, 'rb') as f:
                files = {'file': (filename, f, "text/plain")}
                
                headers = {
                    "accept": "application/json",
                    "Authorization": VOICEFLOW_API_KEY
                }
                
                response = requests.post(url, headers=headers, files=files)
                response_data = response.json()
                responses.append(response_data)
                
    for response in responses:
        if 'code' not in response:
            response['code'] = 200

    responses = [response for response in responses if response['code'] ==  200]

    responses = [response['data']['documentID'] for response in responses]

    return responses
