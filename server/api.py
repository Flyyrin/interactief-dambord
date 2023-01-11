from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import os

BASE = os.getcwd()
GAMES_FILE_PATH = "games.json"
BLOGS_FILE_PATH = "blogs.json"
UPLOAD_FOLDER_PATH = os.path.join(BASE, "/uploads")
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def main():
    return "API voor GIP"

@app.route('/games', methods=['GET','POST'])
@cross_origin()
def games():
    if request.method == 'POST':
        json_data = request.get_json()
        with open(GAMES_FILE_PATH,'r') as file:
            file_data = json.load(file)
            file_data.append(json_data)
        with open(GAMES_FILE_PATH,'w') as file:
            json.dump(file_data, file, indent = 4)
        return ""

    if request.method == 'GET':
        return open(GAMES_FILE_PATH).read()

@app.route('/blogs', methods=['GET','POST'])
@cross_origin()
def blogs():
    if request.method == 'POST':
        json_data = request.get_json()
        with open(BLOGS_FILE_PATH,'r') as file:
            file_data = json.load(file)
            file_data.append(json_data)
        with open(BLOGS_FILE_PATH,'w') as file:
            json.dump(file_data, file, indent = 4)
        return ""

    if request.method == 'GET':
        return open(BLOGS_FILE_PATH).read()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'error'
        file1 = request.files['file1']
        path = os.path.join(UPLOAD_FOLDER_PATH, file1.filename)
        file1.save(path)
        return path
    if request.method == 'GET':
        return ""

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)