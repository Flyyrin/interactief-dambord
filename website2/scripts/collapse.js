$(document).ready(function() {
    $('.panel-collapse').on('DOMSubtreeModified', function(){
        console.log(this);
    });
});