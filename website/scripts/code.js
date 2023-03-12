$(document).ready(function() {
    function highlight() {
        hljs.highlightAll()
    }
    $(".code-block-1").load("../code/checker.py");
    $(".code-block-2").load("../code/webInterface.py");
    $(".code-block-3").load("../code/controller.py");
    $(".code-block-4").load("../code/start.py");
    setTimeout(highlight, 1000)
});