window.onload = function(){
    $(".header").load("html/header.html");
    $(".footer").load("html/footer.html");
    if ($("html").height() > $(window).height()) {
        $(".footer").removeClass("fixed-bottom")
    } else {
        $(".footer").addClass("fixed-bottom")
    }

    const input = $(".preview")
    const output = $(".preview-img")

    var file = input.prop('files')[0];
    var fileURL = "https://placehold.co/600x400?text=Geen Foto Geupload"

    if (file) {
        fileURL = URL.createObjectURL(file)
        output.attr("src",fileURL);
    }

    input.on('change', function() {
        file = input.prop('files')[0];
        fileURL = URL.createObjectURL(file)
        output.attr("src",fileURL);
    });

    $(".pbut").on("click",function(){
        $(".pimg").attr("src",fileURL);
        if ($(".ptitv").val()) {
            $(".ptit").text($(".ptitv").val());
        } else {
            $(".ptit").text("Nog Geen Titel");
        }
        if ($(".pconv").val()) {
            $(".pcont").text($(".pconv").val());
        } else {
            $(".pcont").text("Nog Geen Inhoud");
        }
        $(".pnam").text($(".pnamv").val());
        $(".pdat").text(new Date().toISOString().slice(0, 10));
        $("#modalpreview").modal()
    })

}