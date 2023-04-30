// als de pagina is geladen
window.onload = function() {

    // als er nog argumenten in de url staan, verwijder deze
    if (window.location.href.split('?')[1]) {
        window.location = window.location.href.split('?')[0]
    }

    // kijk welke kleuren gekozen zijn door te kijken welke kleur de class selected heeft
    var cp1 = $(".color-player1 > .selected").attr('class').split(' ')[2];
    var cp2 = $(".color-player2 > .selected").attr('class').split(' ')[2];
    var difficult = false

    // deze functie kijkt naar de gekoze kleuren, en update de button aan de hand hiervan
    // ook geeft hij de 2 kleuren door aan de api met de color functie
    function updateButton() {
        $(".start").css({background: `linear-gradient(120deg, ${$(".color-player1 > .selected").css("background-color")} 50%, ${$(".color-player2 > .selected").css("background-color")} 50%)`});
        pywebview.api.color(cp1+"&"+cp2)
    }

    // als speler 1 of speler 2 een kleur aanklikken, kijk of deze kleur niet al gekozen is door de anders speler
    // als deze nog niet gekozen is, selecteer deze kleur een disable deze voor de andere speler
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

    // als speler 1 of speler 2 een naam intypen, kijk of deze naam niet langer dan 11 characters is, anders kleur de naam rood
    $(".name-player1").on("input", function(){
        if ($(this).val() == "" || $(this).val().length > 11) {
            $(".start").addClass("disabled")
            $(this).addClass("invalid");
        } else {
            $(this).removeClass("invalid");
            if ($(".name-player2").val() != "" && ($(".name-player2").val().length > 11) != true) {
                $(".start").removeClass("disabled")
            }
        }
    });

    $(".name-player2").on("input", function(){

        // als speler 2 een ai is, voeg de juiste emoji toe aan de hand van de difficulity
        if ($(".ai").is(':checked')) {
            console.log($(".difficulty").hasClass("difficult"))
            if ($(".difficulty").hasClass("difficult")) {
                $('.name-player2').val($('.name-player2').val().slice(0,-2)+"🧠")
            } else {
                $('.name-player2').val($('.name-player2').val().slice(0,-2)+"💩")
            }
        }

        if ($(this).val() == "" || $(this).val().length  > 11) {
            $(".start").addClass("disabled")
            $(this).addClass("invalid");
        } else {
            $(this).removeClass("invalid");
            if ($(".name-player1").val() != "" && ($(".name-player1").val().length > 11) != true) {
                $(".start").removeClass("disabled")
            }
        }
    });

    // als er op start wordt gedrukt en start niet disabled (moet voldoen aan juiste naam creteria)
    // voer de start functie van de api uit met de namen en instellingen als parameters
    // en verwijs naar het game scherm met de juiste parameters
    $(".start").on("click", function(){
        if (!$(".start").hasClass("disabled")) {
            var np1 = $(".name-player1").val()
            var np2 = $(".name-player2").val()
            var assist = $(".assist").is(':checked')
            var opponent_ai = $(".ai").is(':checked')
            var difficult_ai = $(".difficulty").hasClass("difficult")
            pywebview.api.start(np1+"&"+np2+"&"+cp1+"&"+cp2+"&"+assist+"&"+opponent_ai+"&"+difficult_ai)
            window.location = window.location.href.replace('start.html', `game.html?np1=${np1}&np2=${np2}&cp1=${cp1}&cp2=${cp2}`);
        }
    });


    // als de ai checkbox wordt aangevinkt, kies een random kleur die nog niet geselecteerd is en kies een random naam
    // laat alleen de juiste kleur zien voor de ai en voeg een robot emoji to achter de naam van de ai
    // als de ai checkbox wordt uitgevink, maak de naam van ai leeg en zet alles weer terug zoals het stond
    $('.ai').change(function() {
        if(this.checked) {
            var colors = ["red", "blue", "yellow", "green", "purple"]  
            var names = ["bob", "henkie", "willie", "dave", "karel", "mindy", "karen", "ankie", "tessa", "carly", "stinky", "benjy"];        
            colors.splice(colors.indexOf(cp1), 1);
            cp2 = colors[Math.floor(Math.random()*colors.length)];
            ai_name = names[Math.floor(Math.random()*names.length)];
            $('.name-player2').attr('disabled', 'disabled');
            $('.name-player2').val(`${ai_name}🤖💩`).change().trigger("input");
            $(".name-player2").addClass("disabled")
            $(".color-player1 > .color").removeClass("disabled");
            $(`.color-player1 > .${cp2}`).addClass("disabled");
            $(".color-player2 > .color:eq(2)").addClass("selected");
            $(".color-player2 > .color:eq(2)").removeClass("yellow");
            $(".color-player2 > .color:eq(2)").addClass(cp2);
            $(".color-player2 > .color:eq(0)").css("opacity", 0) ;
            $(".color-player2 > .color:eq(1)").css("opacity", 0) ;
            $(".color-player2 > .color:eq(3)").css("opacity", 0) ;
            $(".color-player2 > .color:eq(4)").css("opacity", 0) ;
            updateButton()
        } else {
            cp1 = "red"
            $(".color-player2 > .color:eq(2)").removeClass(cp2);
            $(`.color-player1 > .${cp2}`).removeClass("disabled");
            cp2 = "purple"
            $('.name-player2').removeAttr('disabled');
            $('.name-player2').val("").change();
            $(".name-player2").removeClass("disabled");
            $(".color-player2 > .color").removeClass("selected");
            $(".color-player2 > .color").removeClass("disabled");
            $(".color-player2 > .color:eq(0)").css("opacity", 100) ;
            $(".color-player2 > .color:eq(1)").css("opacity", 100) ;
            $(".color-player2 > .color:eq(3)").css("opacity", 100) ;
            $(".color-player2 > .color:eq(4)").css("opacity", 100) ;
            $(".color-player2 > .color:eq(4)").addClass("selected");
            $(".color-player1> .color:eq(4)").addClass("disabled");
            $(".color-player2> .color:eq(0)").addClass("disabled");
            $(".color-player1 > .color").removeClass("selected");
            $(".color-player1 > .color:eq(0)").addClass("selected");
            $(".color-player2 > .color:eq(2)").addClass("yellow");
            updateButton()
        }
    });

    // als de difficulty knop wordt ingedrukt, zet hem op moeielijk of makkelijk aan de hand van waarop die al staat
    $(".difficulty").on("click", function(){
        if (difficult) {
            difficult = false
            $(this).removeClass("difficult");
            $(this).text("Makkelijk");
        } else {
            difficult = true
            $(this).addClass("difficult");
            $(this).text("Moeielijk");
        }
        $('.name-player2').change().trigger("input");
    });

    // als de exit knop wordt ingedrukt, voer de exit functie van de api uit
    $(".exit").on("click", function(){
        pywebview.api.exit("")
    });
}