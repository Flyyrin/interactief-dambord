window.onload = function() {
    if (window.location.href.split('?')[1]) {
        window.location = window.location.href.split('?')[0]
    }

    var cp1 = $(".color-player1 > .selected").attr('class').split(' ')[2];
    var cp2 = $(".color-player2 > .selected").attr('class').split(' ')[2];

    function updateButton() {
        pywebview.api.color(cp1+"&"+cp2)
        $(".start").css({background: `linear-gradient(120deg, ${$(".color-player1 > .selected").css("background-color")} 50%, ${$(".color-player2 > .selected").css("background-color")} 50%)`});
    }

    $(".color-player1").on("click", "div", function(){
        var color = $(this).attr('class').split(' ')[2];
        if (cp2 != color) {
            cp1 = color;
            $(this).siblings().removeClass("selected");
            $(this).addClass("selected");
            $(`.color-player2 > .${cp1}`).siblings().removeClass("disabled");
            $(`.color-player2 > .${cp1}`).addClass("disabled")
            updateButton()
        }
    });

    $(".color-player2").on("click", "div", function(){
        var color = $(this).attr('class').split(' ')[2];
        if (cp1 != color) {
            cp2 = color;
            $(this).siblings().removeClass("selected");
            $(this).addClass("selected");
            $(`.color-player1 > .${cp2}`).siblings().removeClass("disabled");
            $(`.color-player1 > .${cp2}`).addClass("disabled")
            updateButton()
        }
    });

    $(".name-player1").on("input", function(){
        if ($(this).val() == "" || $(this).val().length > 10) {
            $(".start").addClass("disabled")
            $(this).addClass("invalid");
        } else {
            $(this).removeClass("invalid");
            if ($(".name-player2").val() != "" && ($(".name-player2").val().length > 10) != true) {
                $(".start").removeClass("disabled")
            }
        }
    });

    $(".name-player2").on("input", function(){
        if ($(this).val() == "" || $(this).val().length  > 10) {
            $(".start").addClass("disabled")
            $(this).addClass("invalid");
        } else {
            $(this).removeClass("invalid");
            if ($(".name-player1").val() != "" && ($(".name-player1").val().length > 10) != true) {
                $(".start").removeClass("disabled")
            }
        }
    });

    $(".start").on("click", function(){
        if (!$(".start").hasClass("disabled")) {
            var np1 = $(".name-player1").val()
            var np2 = $(".name-player2").val()
            var assist = $(".assist").val()
            pywebview.api.start(np1+"&"+np2+"&"+cp1+"&"+cp2+"&"+assist)
            window.location = window.location.href.replace('start.html', `game.html?np1=${np1}&np2=${np2}&cp1=${cp1}&cp2=${cp2}`);
        }
    });

    $(".exit").on("click", function(){
        pywebview.api.exit("")
    });
}