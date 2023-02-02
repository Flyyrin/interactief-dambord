window.onload = function() {
    var cp1 = $(".cp1 > .selected").attr('class').split(' ')[0];
    var cp2 = $(".cp2 > .selected").attr('class').split(' ')[0];

    function updateButton() {
        $(".submit").css({background: `linear-gradient(120deg, ${$(".cp1 > .selected").css("background-color")} 50%, ${$(".cp2 > .selected").css("background-color")} 50%)`});
    }

    $(".cp1").on("click", "li", function(){
        var color = $(this).attr('class').split(' ')[0];
        if (cp2 != color) {
            cp1 = color;
            $(this).siblings().removeClass("selected");
            $(this).addClass("selected");
            $(`.cp2 > .${cp1}`).siblings().removeClass("disabled");
            $(`.cp2 > .${cp1}`).addClass("disabled")
            updateButton()
        }
    });

    $(".cp2").on("click", "li", function(){
        var color = $(this).attr('class').split(' ')[0];
        if (cp1 != color) {
            cp2 = color;
            $(this).siblings().removeClass("selected");
            $(this).addClass("selected");
            $(`.cp1 > .${cp2}`).siblings().removeClass("disabled");
            $(`.cp1 > .${cp2}`).addClass("disabled")
            updateButton()
        }
    });

    $(".player1name").on("input", function(){
        if ($(this).val() == "") {
            $(".submit").addClass("disabled")
        } else {
            if ($(".player2name").val() != "") {
                $(".submit").removeClass("disabled")
            }
        }
    });

    $(".player2name").on("input", function(){
        if ($(this).val() == "") {
            $(".submit").addClass("disabled")
        } else {
            if ($(".player1name").val() != "") {
                $(".submit").removeClass("disabled")
            }
        }
    });

    $(".submit").on("click", function(){
        if (!$(".submit").hasClass("disabled")) {
            $(".color1").attr("value",cp1);
            $(".color2").attr("value",cp2);
            $(".start").attr("value","True");
        }
    });
}