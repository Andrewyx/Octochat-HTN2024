import pickle
import os, shutil
from Constants import DATA_FOLDER_PATH
import stat
import requests
import dotenv

debug = {"ids":["123901", "fehwio", "new stuff as well"]}

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

def storeData(ids: dict) -> None:    
    # Its important to use binary mode
    dbfile = open('cachedIDs.txt', 'wb+')
    # source, destination
    pickle.dump(ids, dbfile)                    
    dbfile.close()

def loadData():
    # for reading also binary mode is important
    dbfile = open('cachedIDs.txt', 'rb')    
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()

def delete_cache() -> None:
    # Clears the local and remote files
    clear_voiceflow()
    clear_local_files()

def clear_voiceflow() -> None:
    delete_files_from_voiceflow(get_list_of_documents())

def clear_local_files() -> None:
    if not os.path.exists(DATA_FOLDER_PATH):
        os.makedirs(DATA_FOLDER_PATH)

    for root, dirs, files in os.walk(DATA_FOLDER_PATH):  
        for dir in dirs:
            os.chmod(os.path.join(root, dir), stat.S_IRWXU)
        for file in files:
            os.chmod(os.path.join(root, file), stat.S_IRWXU)

    for filename in os.listdir(DATA_FOLDER_PATH):
        file_path = os.path.join(DATA_FOLDER_PATH, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    

# Debug 
if __name__ == '__main__':
    storeData(debug)
    loadData()
    clear_local_files()