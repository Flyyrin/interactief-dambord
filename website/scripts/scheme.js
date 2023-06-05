$(document).ready(function() {
    $(".image-hard").hide()

    $(".simple").on("click", function(){
        if (!$(this).hasClass("active")) {
            $(this).siblings().removeClass("active")
            $(this).addClass("active")
            $(".image-hard").hide()
            $(".image-simple").show()
        }
    });

    $(".hard").on("click", function(){
        if (!$(this).hasClass("active")) {
            $(this).siblings().removeClass("active")
            $(this).addClass("active")
            $(".image-simple").hide()
            $(".image-hard").show()
        }
    });
});