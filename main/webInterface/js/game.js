// als de pagina is geladen, haal np1, np2, cp1 en cp2 uit de url
// zet de namen in de juiste elementen en voeg de juiste class toe aan de hand van de kleur
window.onload = function() {;
    var np1 = getParam('np1');
    var np2 = getParam('np2');
    var cp1 = getParam('cp1');
    var cp2 = getParam('cp2');

    $(".player1").html(np1)
    $(".player2").html(np2.replace("🤖", "<span>🤖</span>"))
    $(".player1").addClass(cp1+"-text")
    $(".player2").addClass(cp2+"-text")

    // haal de huidige tijd op en start een timer interval die elke seconde de timer waarde update
    var gameTime
    var startTime = Date.now()
    var delta = Date.now() - startTime; 
    var seconds = Math.floor(delta / 1000)
    gameTime = new Date(seconds * 1000).toISOString().substring(14, 19)
    setInterval(function timerFunction() {
        var delta = Date.now() - startTime; 
        var seconds = Math.floor(delta / 1000)
        gameTime = new Date(seconds * 1000).toISOString().substring(14, 19)
        $(".timer").text(gameTime)
    }, 1000);
 
    // als er 1x op stop wordt geklikt, vraag voor en confirmatie
    // als er nog eens wordt gedrukt, voer de stop functie van de api uit een ga terug naar het begin scherm
    // anders zet de stop knop weer terug op normaal
    var clicked = 0
    $(".stop").on("click", function(){
        clicked += 1
        $(".stop").html("Zeker?")
        setTimeout(function() { $(".stop").html("Stop"); clicked = 0 }, 3000);
        if (clicked == 2) {
            pywebview.api.stop("")
            window.location = window.location.href.replace('game', 'start');
        }
    });

    // functie die telkens opnieuw wordt uigevoerd
    // haal data van de server af (/game) en update aantal speelstukken en wie aan de beurt is
    // als de game niet actief is en er is een winner,
    // dan verwijs door naar de win pagina en voeg winner en speeltijd toe aan de parameters
    function updateGame() {
        $.get( "http://flyyrin.pythonanywhere.com/game", function( data ) {
            data = JSON.parse(data);
            if (data["gameData"]["playing"] == 1) {
                $(".player1").addClass("playing")
                $(".player2").removeClass("playing")
            }
            if (data["gameData"]["playing"] == 2) {
                $(".player2").addClass("playing")
                $(".player1").removeClass("playing")
            }
            $(".player1-pieces").html($(".player1-pieces").html().split(":")[0] + ": " + data["gameData"]["pieces"]["player1"]["pieces"])
            $(".player1-kings").html($(".player1-kings").html().split(":")[0] + ": " +  data["gameData"]["pieces"]["player1"]["kings"])
            $(".player1-captured").html($(".player1-captured").html().split(":")[0] + ": " + data["gameData"]["pieces"]["player1"]["captured"])
            $(".player2-pieces").html($(".player2-pieces").html().split(":")[0] + ": " + data["gameData"]["pieces"]["player2"]["pieces"])
            $(".player2-kings").html($(".player2-kings").html().split(":")[0] + ": " +  data["gameData"]["pieces"]["player2"]["kings"])
            $(".player2-captured").html($(".player2-captured").html().split(":")[0] + ": " + data["gameData"]["pieces"]["player2"]["captured"])
            if (data["game"] == false && data["winner"] != 0) {
                window.location = window.location.href.replace('game.html?', `win.html?winner=${String(data["winner"])}&time=${gameTime}&`);
            }
        });
    }

    // voer de update functie uit, en herhaal dit elker 100 milliseconde
    updateGame()
    setInterval(function() {
        updateGame();
    }, 100);

    // als de exit knop wordt ingedrukt, voer de exit functie van de api uit
    $(".exit").on("click", function(){
        pywebview.api.exit("") 
    });
} 