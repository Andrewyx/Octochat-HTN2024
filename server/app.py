from flask import Flask
import requests
import os
import asyncio
import aiohttp
import dotenv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


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
