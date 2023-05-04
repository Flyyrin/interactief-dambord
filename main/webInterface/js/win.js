// als de pagina is geladen, haal de winner, time, np1, np2, cp1 en cp2 uit de url
// zet de namen in de juiste elementen en voeg de juiste class toe aan de hand van de kleur
// laat aan de hand van de winner de juiste kroon zien.
// als er op restart wordt gedrukt, voer de stop functie uit op de api, en ga terug naar het start schrerm
// als er op exit wordt gedrukt, voer de exit functie uit op de api
window.onload = function() {
    var winner = getParam('winner');
    var time = getParam('time');
    var np1 = getParam('np1');
    var np2 = getParam('np2');
    var cp1 = getParam('cp1');
    var cp2 = getParam('cp2');

    $(".player1").html(np1)
    $(".player2").html(np2)
    $(".time").html(time)
    $(".timertag").html(time)
    $(".player1").addClass(cp1+"-text")
    $(".player2").addClass(cp2+"-text")
    if (winner == 1) {
        $(".crown2").addClass("invisible")
    }
    if (winner == 2) {
        $(".crown1").addClass("invisible")
    }

    $(".restart").on("click", function(){
        pywebview.api.stop("") 
        window.location = window.location.href.replace('win', 'start');
    });

    $(".exit").on("click", function(){
        pywebview.api.exit("") 
    });
}