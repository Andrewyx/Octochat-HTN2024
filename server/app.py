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
    




