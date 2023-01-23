window.onload = function(){
    $(".header").load("html/header.html");
    $(".footer").load("html/footer.html");
    if ($("html").height() > $(window).height()) {
        $(".footer").removeClass("fixed-bottom")
    } else {
        $(".footer").addClass("fixed-bottom")
    }
}