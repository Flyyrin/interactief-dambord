$(document).ready(function() {
    function highlight() {
        hljs.highlightAll()
    }
    $(".code-block").load("../code/checker.py");
    setTimeout(highlight, 1000)
});