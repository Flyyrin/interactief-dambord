$(window).ready(function() {
    // var server = "http://flyyrin.pythonanywhere.com/game"
    var server = "data.json"
    const colors = {
        "e": "#00000000",
        "red": "#fc4c4f",
        "blue": "#4fa3fc",
        "yellow": "#ECD13F",
        "green": "#4bec3f",
        "purple": "#cf3fec",
        "ai": "#ffffff",
        "king-red": "#ff0004",
        "king-blue": "#007bff",
        "king-yellow": "#ffd900",
        "king-green": "#11ff00",
        "king-purple": "#a200c3",
        "king-ai": "#ffffff88"
    }

    function setup() {
        $.get(server, function(data) {
            console.log(data)
            // data = JSON.parse(data);

            console.log(data.game)
            if (!data.game && !data.winner) {
                $("#noGameModal").modal('show');
            } else if (!data.game && data.winner) {
                $(".winner").attr('class', 'winner black-text-shadow');
                if (data.winner == 1) {
                    $(".winner").text(data.gameData.np1);
                    $(".winner").addClass(data.gameData.cp1+"-text");
                }
                if (data.winner == 2) {
                    $(".winner").text(data.gameData.np2);
                    $(".winner").addClass(data.gameData.cp2+"-text");
                }
                $("#winnerModal").modal('show');
            } else{
                $(".player1").html(data.gameData.np1)
                $(".player2").html(data.gameData.np2)
                $(".player1").addClass(data.gameData.cp1+"-text")
                $(".player2").addClass(data.gameData.cp2+"-text")

                update()
                setInterval(function() {
                    update();
                }, 1000);
            }
        });
    }

    function update() {
        $.get(server, function(data) {
            // data = JSON.parse(data);
            var startTime = new Date(data.gameData.time)
            var currentTime = new Date();
            var alphaSeconds = (currentTime.getTime() - startTime.getTime())/1000
            var mmss = new Date(alphaSeconds * 1000).toISOString().substring(14, 19)
            $(".timer").html(mmss)

            if (data.gameData.playing == 1) {
                $(".player1").addClass("playing")
                $(".player2").removeClass("playing")
            }
            if (data.gameData.playing == 2) {
                $(".player2").addClass("playing")
                $(".player1").removeClass("playing")
            }

            $(".player1-pieces").html($(".player1-pieces").html().split(":")[0] + ": " + data.gameData.pieces.player1.pieces)
            $(".player1-kings").html($(".player1-kings").html().split(":")[0] + ": " +  data.gameData.pieces.player1.kings)
            $(".player1-captured").html($(".player1-captured").html().split(":")[0] + ": " + data.gameData.pieces.player1.captured)
            $(".player2-pieces").html($(".player2-pieces").html().split(":")[0] + ": " + data.gameData.pieces.player2.pieces)
            $(".player2-kings").html($(".player2-kings").html().split(":")[0] + ": " +  data.gameData.pieces.player2.kings)
            $(".player2-captured").html($(".player2-captured").html().split(":")[0] + ": " + data.gameData.pieces.player2.captured)

            $.each(data.gameData.board, function(position, piece) {
                if (piece == 1) {
                    $(`.board > svg > #${position}`).attr("fill", colors[data.gameData.cp1]);
                }
                if (piece == 3) {
                    $(`.board > svg > #${position}`).attr("fill", colors[`king-${data.gameData.cp1}`]);
                }
                if (piece == 2) {
                    $(`.board > svg > #${position}`).attr("fill", colors[data.gameData.cp2]);
                }
                if (piece == 4) {
                    $(`.board > svg > #${position}`).attr("fill", colors[`king-${data.gameData.cp2}`]);
                }
                if (piece == "e") {
                    $(`.board > svg > #${position}`).attr("fill", colors[piece]);
                }
            });
        });
    }

    if ($(window).width() < 960) {
        console.log($(".pieces"))
        $(".pieces").removeClass("d-flex")
        $(".pieces").hide();
    }
    $(".board").load("images/board.svg")
    setup()
})