window.onload = function() {;
    var np1 = getParam('np1');
    var np2 = getParam('np2');
    var cp1 = getParam('cp1');
    var cp2 = getParam('cp2');

    $(".player1").html(np1)
    $(".player2").html(np2)
    $(".player1").addClass(cp1+"-text")
    $(".player2").addClass(cp2+"-text")

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

    function updateGame() {
        $.get( "http://flyyrin.pythonanywhere.com/game", function( data ) {
            data = JSON.parse(data);
            if (data["gameData"]["current-player"] == 1) {
                $(".player1").addClass("playing")
                $(".player2").removeClass("playing")
            }
            if (data["gameData"]["current-player"] == 2) {
                $(".player2").addClass("playing")
                $(".player1").removeClass("playing")
            }
            $(".player1-pieces").html($(".player1-pieces").html().split(":")[0] + ": " + data["gameData"]["pieces"]["player1"]["pieces"])
            $(".player1-kings").html($(".player1-kings").html().split(":")[0] + ": " +  data["gameData"]["pieces"]["player1"]["kings"])
            $(".player1-captured").html($(".player1-captured").html().split(":")[0] + ": " + data["gameData"]["pieces"]["player1"]["captured"])
            $(".player2-pieces").html($(".player2-pieces").html().split(":")[0] + ": " + data["gameData"]["pieces"]["player2"]["pieces"])
            $(".player2-kings").html($(".player2-kings").html().split(":")[0] + ": " +  data["gameData"]["pieces"]["player2"]["kings"])
            $(".player2-captured").html($(".player2-captured").html().split(":")[0] + ": " + data["gameData"]["pieces"]["player2"]["captured"])
            console.log(data["game"])
            if (data["game"] == false && data["winner"] != 0) {
                window.location = window.location.href.replace('game.html?', `win.html?winner=${String(data["winner"])}&time=${gameTime}&`);
            }
        });
    }

    updateGame()
    setInterval(function() {
        updateGame();
    }, 1000);

    $(".exit").on("click", function(){
        pywebview.api.exit("") 
    });
}