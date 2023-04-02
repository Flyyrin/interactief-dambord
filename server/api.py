from flask import Flask, request, redirect
from flask_cors import CORS, cross_origin
import json
import os
import time

BASE = os.path.dirname(os.path.abspath(__file__))
GAMES_FILE_PATH = os.path.join(BASE, "games.json")

game = False
winner = 0
startTime = 0
gameData = {
    "np1": "Rafael",
    "np2": "Romeo",
    "cp1": "red",
    "cp2": "purple",
    "currentTime": 0,
    "playing": 1,
    "pieces": {
        "player1": {
            "pieces": 1,
            "kings": 2,
            "captured": 3
        },
        "player2": {
            "pieces": 4,
            "kings": 5,
            "captured": 6
        }
    },
    "board": {
        "1": 1, 
        "2": 1, 
        "3": 1, 
        "4": 1, 
        "5": 1, 
        "6": 1, 
        "7": 1, 
        "8": 1, 
        "9": 1, 
        "10": 1, 
        "11": 1, 
        "12": 1, 
        "13": "e", 
        "14": "e", 
        "15": "e", 
        "16": "e", 
        "17": "e", 
        "18": "e", 
        "19": "e", 
        "20": "e", 
        "21": 2, 
        "22": 2, 
        "23": 2, 
        "24": 2, 
        "25": 2, 
        "26": 2, 
        "27": 2, 
        "28": 2, 
        "29": 2, 
        "30": 2, 
        "31": 2, 
        "32": 2
    }
}

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def main():
    return "Server voor <a href='https://dambord.netlify.app/'>GIP</a>"

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

@app.route('/game', methods=['GET','POST'])
@cross_origin()
def gameongoing():
    global game
    global winner
    global gameData
    global startTime
    if request.method == 'POST':
        type = request.args.get("type")
        if type == "winner":
            game = False
            winner = request.get_json()["winner"]
        if type == "start":
            winner = 0
            game = True
            startTime = int(time.time() * 1000)
        if type == "stop":
            winner = 0
            game = False
        if type == "gameData":
            gameData = request.get_json()["gameData"]
        return ""
    if request.method == 'GET':
        gameData["currentTime"] = int(time.time() * 1000)
        gameData["startTime"] = startTime
        return json.dumps({"game":game, "winner":winner, "gameData":gameData})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)