from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

DB_FILE_PATH = "db.json"
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET','POST'])
@cross_origin()
def main():
    if request.method == 'POST':
        json_data = request.get_json()
        with open(DB_FILE_PATH,'r') as file:
            file_data = json.load(file)
            file_data.append(json_data)
        with open(DB_FILE_PATH,'w') as file:
            json.dump(file_data, file, indent = 4)
        return ""

    if request.method == 'GET':
        return open(DB_FILE_PATH).read()

import os
print(os.getcwd())
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)