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
            if (data["gameongoing"] == false && data["winner"] != 0) {
                window.location = window.location.href.replace('game.html?', `win.html?winner=${String(data["winner"])}&`);
            }
        });
    }, 1000);
}