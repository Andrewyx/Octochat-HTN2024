from flask import Flask
import requests
import os
import asyncio
import aiohttp
import dotenv
from flask import Flask, request
from VoiceflowHandler import delete_cache
from RepoHandler import rename_to_txt, get_repo
from Constants import DATA_FOLDER_PATH

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
        get_repo(cachedURL)
        upload_files_to_voiceflow(DATA_FOLDER_PATH)
    # ELSE: DO NOT DO ANYTHING AND DO NOT DISPLAY INJECTED BUTTON

def url_is_cached(url: str) -> bool:
    return cachedURL.strip() == url.strip()

def delete_files_from_voiceflow(document_ids: list[str]) -> None:
    # get the API key from the .env file
    dotenv.load_dotenv()
    VOICEFLOW_API_KEY = os.getenv('VOICEFLOW_API_KEY')

    for document_id in document_ids:

        url = f"https://api.voiceflow.com/v1/knowledge-base/docs/{document_id}"
        headers = {
            "accept": "application/json",
            "Authorization": VOICEFLOW_API_KEY
        }

        response = requests.delete(url, headers=headers)

    print("All files deleted")

def upload_files_to_voiceflow(directory: str) -> list[str]:
    # get the API key from the .env file
    dotenv.load_dotenv()
    VOICEFLOW_API_KEY = os.getenv('VOICEFLOW_API_KEY')

    responses = []
    url = "https://api.voiceflow.com/v1/knowledge-base/docs/upload?maxChunkSize=1000"

    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            print(filename)
            file_path = os.path.join(dirpath, filename)
            filename = rename_to_txt(filename)
            
            with open(file_path, 'rb') as f:
                files = {'file': (filename, f, "text/plain")}
                
                headers = {
                    "accept": "application/json",
                    "Authorization": VOICEFLOW_API_KEY
                }
                
                try:
                    response = requests.post(url, headers=headers, files=files)
                    response_data = response.json()
                    responses.append(response_data)
                except Exception as e:
                    print(e)
                    responses.append({"code": 500, "data": {"documentID": None}})

                
    for response in responses:
        if 'code' not in response:
            response['code'] = 200

    responses = [response for response in responses if response['code'] ==  200]

    responses = [response['data']['documentID'] for response in responses]

    return responses


def get_list_of_documents() -> list[str]:
    # get the API key from the .env file
    dotenv.load_dotenv()
    VOICEFLOW_API_KEY = os.getenv('VOICEFLOW_API_KEY')

    url = "https://api.voiceflow.com/v1/knowledge-base/docs?page=1&limit=100"
    headers = {
        "accept": "application/json",
        "Authorization": VOICEFLOW_API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response_data = response.json()
        document_ids = [doc['documentID'] for doc in response_data['data']]
        return document_ids
    except Exception as e:
        print(e)
        return []


# test endpoint to create
# @app.route("/test1")
# def upload_files() -> str:
#     directory = "./"
#     document_ids = upload_files_to_voiceflow(directory)
#     return str(document_ids)

# @app.route("/test2")
# def delete_files() -> str:
#     document_ids = get_list_of_documents()
#     delete_files_from_voiceflow(document_ids)
#     return str(document_ids)


if __name__ == '__main__':
    app.run(use_reloader=True, port=5525, threaded=True, host="0.0.0.0", debug=True)
    