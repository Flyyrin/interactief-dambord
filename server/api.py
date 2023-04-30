"""
Dit is de flask server die ervoor zorgt dat het dambord, de webInterface en de website met elkaar kunnen comuniceren.
"""

# importeer nodioge modules en defineer alle basis variabelen
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
    "np2": "Michael",
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
    "board": {}
}

# maak een flas app aan, en verander de instellingen
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# maak de route "/" aan
# als mensen deze route bezoeken krijgen ze een korte tekst te zien
@app.route('/')
def main():
    return "Server voor <a href='https://dambord.netlify.app/'>GIP</a>"

# maak de route "/games" aan
# als hiernaar gepost wordt dan wordt de json data append naar de games.json file
# als deze route bezoek wordt dan geeft hij de inhoud van games.json terug
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

# maak de route "/game" aan
# als hiernaar gepost wordt kijkt hij naar het argument "type" en aan de hand daarvan kan hij de status van de game of de gameData veranderen
# als deze route bezoek wordt dan geeft hij voegt hij de start tijd en de huidige tijd toe aan de gameData 
# en geeft hij deze data samen met de winner en game status terug
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

# als de file direct wordt uitgevoerd dan start de flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)