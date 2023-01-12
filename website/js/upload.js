window.onload = function(){
    $(".header").load("html/header.html");
    $(".footer").load("html/footer.html");
    if ($("html").height() > $(window).height()) {
        $(".footer").removeClass("fixed-bottom")
    } else {
        $(".footer").addClass("fixed-bottom")
    }

    var fileURL = "https://placehold.co/600x400?text=Geen Foto Geupload"
    var file;
    const input = $(".preview")
    const output = $(".preview-img")
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

    // function uploadIMG(img) {
    //     var fd = new FormData();
    //     fd.append('file1', img /*, optional filename */)

    //     var req = jQuery.ajax({
    //         url: 'http://172.16.1.106:5000/upload', 
    //         method: 'POST',
    //         data: fd, // sends fields with filename mimetype etc
    //         // data: aFiles[0], // optional just sends the binary
    //         processData: false, // don't let jquery process the data
    //         contentType: false // let xhr set the content type
    //     });

    //     // jQuery is promise A++ compatible and is the todays norms of doing things 
    //     req.then(function(response) {
    //        return response
    //     }, function(xhr) {
    //         return xhr
    //     })
    //     return req
    // }

    // async function uploadBlog() {
    //     var data = {
    //         "title":  $(".ptitv").val(),
    //         "name":  $(".pnamv").val(),
    //         "imgurl": await uploadIMG(file),
    //         "date":  new Date().toISOString().slice(0, 10),
    //         "content":  $(".pconv").val()
    //     }
    //     console.log(data)
    // }
    // $(".plaatsbut").on("click",function(){
    //     uploadBlog()
    // })
    
}