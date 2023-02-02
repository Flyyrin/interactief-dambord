window.onload = function() {
    document.body.style.zoom = 1.5

    $.urlParam = function(name){
        var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
        if (results==null) {
           return null;
        }
        return decodeURI(results[1]) || 0;
    }

    var winner = $.urlParam('winner');
    var np1 = $.urlParam('np1');
    var np2 = $.urlParam('np2');
    var cp1 = $.urlParam('cp1');
    var cp2 = $.urlParam('cp2');
    console.log(winner, np1, np2, cp1, cp2)
    $(".player1tag").html(np1)
    $(".player2tag").html(np2)
    $(".player1tag").addClass(cp1+"t")
    $(".player2tag").addClass(cp2+"t")
    if (winner == 1) {
        $(".p1w").addClass("winner")
    }
    if (winner == 2) {
        $(".p2w").addClass("winner")
    }

    $(".replay").on("click", function(){
        window.location = window.location.href.replace('win', 'start');
    });
}