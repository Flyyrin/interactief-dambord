var gameTime = 0
var timerIntervalId
var start

window.onload = function() {
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
        $(".timevalue").attr("value",gameTime);
        $(".stop").attr("value","True");
    });
}