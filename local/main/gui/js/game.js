var gameTime = 0
var timerIntervalId
var start
var clicked = 0

window.onload = function() {
    document.body.style.zoom = 1.5

    $.urlParam = function(name){
        var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
        if (results==null) {
           return null;
        }
        return decodeURI(results[1]) || 0;
    }

    var np1 = $.urlParam('np1');
    var np2 = $.urlParam('np2');
    var cp1 = $.urlParam('cp1');
    var cp2 = $.urlParam('cp2');
    console.log(np1, np2, cp1, cp2)

    $(".player1tag").html(np1)
    $(".player2tag").html(np2)
    $(".player1tag").addClass(cp1+"t")
    $(".player2tag").addClass(cp2+"t")

    var start = Date.now()
    var delta = Date.now() - start; 
    var seconds = Math.floor(delta / 1000)
    gameTime = new Date(seconds * 1000).toISOString().substring(14, 19)
    $(".timertag").text(gameTime)
    timerIntervalId = setInterval(timerFunction, 1000);

    function timerFunction() {
        var delta = Date.now() - start; 
        var seconds = Math.floor(delta / 1000)
        gameTime = new Date(seconds * 1000).toISOString().substring(14, 19)
        $(".timertag").text(gameTime)
    }

    $(".restart").on("click", function(){
        clicked += 1
        $(".restart").html("Zeker?")
        setTimeout(function() { $(".restart").html("Stop"); clicked = 0 }, 3000);
        if (clicked == 2) {
            pywebview.api.stop("")
            window.location = window.location.href.replace('game', 'start');
        }
    });

   
    setInterval(function() {
        $.get( "http://flyyrin.pythonanywhere.com/gameongoing", function( data ) {
            data = JSON.parse(data);
            if (data["player"] == 1) {
                $(".player1tag").addClass("playing")
                $(".player2tag").removeClass("playing")
            }
            if (data["player"] == 2) {
                $(".player2tag").addClass("playing")
                $(".player1tag").removeClass("playing")
            }
            $(".p1p").html(": "+data["game"]["p1"]["pieces"])
            $(".p1k").html(": "+data["game"]["p1"]["kings"])
            $(".p1c").html(": "+data["game"]["p1"]["captured"])
            $(".p2p").html(": "+data["game"]["p2"]["pieces"])
            $(".p2k").html(": "+data["game"]["p2"]["kings"])
            $(".p2c").html(": "+data["game"]["p2"]["captured"])
            if (data["gameongoing"] == false && data["winner"] != 0) {
                window.location = window.location.href.replace('game.html?', `win.html?winner=${String(data["winner"])}&time=${gameTime}&`);
            }
        });
    }, 1000);
}