from flask import Flask, jsonify

app = Flask(__name__)

YOUTUBE_URL = "https://youtu.be/7nSr2P6blYM?si=Lxte8Q4MKw0Zea5-"

@app.route('/')
def index():
    return jsonify(redirect_url=YOUTUBE_URL)

@app.route('/redirect-to-song', methods=['POST'])
def redirect_to_song():
    return jsonify(redirect_url=YOUTUBE_URL)

@app.route('/go')
def go():
    return jsonify(redirect_url=YOUTUBE_URL)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
