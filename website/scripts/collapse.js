$(document).ready(function() {
    $('.collapse').on('shown.bs.collapse', function(){
        $(this).parent().find(".bi-caret-down").removeClass("bi-caret-down").addClass("bi-caret-up");
    }).on('hidden.bs.collapse', function(){
        $(this).parent().find(".bi-caret-up").removeClass("bi-caret-up").addClass("bi-caret-down");
        });
});