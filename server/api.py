from flask import Flask, request, redirect, send_file
from flask_cors import CORS, cross_origin
from datetime import datetime
import uuid
import json
import os

PASSWORD = "gipstrijders123"

BASE = os.path.dirname(os.path.abspath(__file__))
GAMES_FILE_PATH = os.path.join(BASE, "games.json")
BLOGS_FILE_PATH = os.path.join(BASE, "blogs.json")
UPLOAD_FOLDER_PATH = os.path.join(BASE, "uploads")
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
        password = request.form.get("password")

        if password == PASSWORD:
            data = {
                "title":  request.form.get("title"),
                "name":  request.form.get("name"),
                "date":  datetime.today().strftime('%d-%m-%Y'),
                "content":  request.form.get("content")
            }

            img = request.files['imgfile']
            newname = f"{str(uuid.uuid4())}{os.path.splitext(img.filename)[1]}"
            img.save(os.path.join(UPLOAD_FOLDER_PATH, newname))

            data["imgurl"] = f"http://flyyrin.pythonanywhere.com/media/{newname}"

            with open(BLOGS_FILE_PATH,'r') as file:
                file_data = json.load(file)
                file_data.append(data)
            with open(BLOGS_FILE_PATH,'w') as file:
                json.dump(file_data, file, indent = 4)

            return redirect("https://dambord.netlify.app/blog")
        else:
            return redirect("https://dambord.netlify.app/fout")

    if request.method == 'GET':
        print(BASE)
        print(UPLOAD_FOLDER_PATH)
        return open(BLOGS_FILE_PATH).read()
    
@app.route('/media/<id>')
@cross_origin()
def media(id):
    filepath = os.path.join(UPLOAD_FOLDER_PATH, id)
    if os.path.exists(filepath):
        return send_file(filepath, mimetype='image/gif')
    else:
        return send_file(os.path.join(BASE, "notfound.png"), mimetype='image/gif')

data = {
    "gameongoing": False, 
    "winner": 0, 
    "player": 0,
    "game": {
        "p1": {
            "pieces": 0,
            "kings": 0,
            "captured": 0
        },
        "p2": {
            "pieces": 0,
            "kings": 0,
            "captured": 0
        }
    }
}
@app.route('/gameongoing/', methods=['GET','POST'])
@cross_origin()
def gameongoing():
    global data
    if request.method == 'POST': 
        data = request.get_json()
        return ""
    if request.method == 'GET':
        return json.dumps(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)