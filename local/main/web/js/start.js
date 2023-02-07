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
        console.log("won")
    }
    if (winner == 2) {
        $(".crown1").addClass("invisible")
    }

    $(".restart").on("click", function(){
        window.location = window.location.href.replace('win', 'start');
    });
}