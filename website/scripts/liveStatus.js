$(window).ready(function() {
    const server = "https://flyyrin.pythonanywhere.com/game"
   
    function update() {
        $.get(server, function(data) {
            data = JSON.parse(data);
            if (data.game) {
                var startTime = new Date(data.gameData.startTime)
                var currentTime = new Date(data.gameData.currentTime);
                var alphaSeconds = (currentTime.getTime() - startTime.getTime())/1000
                var mmss = new Date(alphaSeconds * 1000).toISOString().substring(14, 19)
                $(".liveStatus").text("Live Game (active)")
                $(".liveStatusData").show()
                $(".liveStatusDivider").show()
                $(".liveStatusData1").text(data.gameData.np1)
                $(".liveStatusData2").text(data.gameData.np2)
                $(".liveStatusData1").addClass(data.gameData.cp1+"-text")
                $(".liveStatusData2").addClass(data.gameData.cp2+"-text")
                $(".liveStatusDatat").text(mmss)
            } else {
                $(".liveStatus").text("Live Game (not active)")
                $(".liveStatusData").hide()
                $(".liveStatusDivider").hide()
            }
        });
    }

    update()
    setInterval(function() {
        update();
    }, 1000);
})