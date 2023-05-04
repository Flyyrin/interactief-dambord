$(document).ready(function() {
    const server = "https://flyyrin.pythonanywhere.com/games"
    const colors = {
        "e": "#00000000",
        "red": "#fc4c4f",
        "blue": "#4fa3fc",
        "yellow": "#ECD13F",
        "green": "#4bec3f",
        "purple": "#cf3fec",
        "king-red": "#ff0004",
        "king-blue": "#007bff",
        "king-yellow": "#d6b500",
        "king-green": "#0cad00",
        "king-purple": "#a200c3",
    }

    function getParam(name){
        var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
        if (results==null) {
            return null;
        }
        return decodeURI(results[1]) || 0;
    }

    function update() {
        data = gameData[move]
        $(".currentMove").html(move+1)
        $.each(data, function(position, piece) {
            if (piece == 1) {
                $(`.board > svg > #${position}`).attr("fill", colors[cp1]);
            }
            if (piece == 3) {
                $(`.board > svg > #${position}`).attr("fill", colors[`king-${cp1}`]);
            }
            if (piece == 2) {
                $(`.board > svg > #${position}`).attr("fill", colors[cp2]);
            }
            if (piece == 4) {
                $(`.board > svg > #${position}`).attr("fill", colors[`king-${cp2}`]);
            }
            if (piece == "e") {
                $(`.board > svg > #${position}`).attr("fill", colors[piece]);
            }
        });
    }

    if ($(window).width() < 960) {
        $(".board").load("images/m-board.svg")
        $(".pieces").removeClass("d-flex")
        $(".pieces").hide();
    } else {
        $(".board").load("images/board.svg")
    }   

    var cp1
    var cp2
    var gameData
    var move = 0
    var game = getParam("game")

    $.get(server, function(data) {
        data = JSON.parse(data);
        data = data[parseInt(game)]
        gameData = data["history"]

        cp1 = data.player1.color
        cp2 = data.player2.color
        $(".player1").html(data.player1.name)
        $(".player2").html(data.player2.name)
        $(".player1").addClass(data.player1.color+"-text")
        $(".player2").addClass(data.player2.color+"-text") 
        $(".totalMoves").html(gameData.length)
        $(".time").html(`${timeSince(data.date)} geleden`)
        setTimeout(function() {
            update()
        }, 100);
    });

    $(".controlButtonLeft").on("click", function(){
        if (move > 0) {
            move -= 1
            update()
        }
    });

    $(".controlButtonRight").on("click", function(){
        if (move < gameData.length-1) {
            move += 1
            update()
        }
    });

    $(".back").on("click", function(){
        history.back()
    });
})