$(document).ready(function () {
  const server = "https://flyyrin.pythonanywhere.com/game";

  function update() {
    $(".liveStatus").text("Live Game (active)");
    $(".liveStatusData").show();
    $(".liveStatusDivider").show();
    $(".liveStatusData1").text("Rafael");
    $(".liveStatusData2").text("Michael");
    $(".liveStatusData1").addClass("red-text");
    $(".liveStatusData2").addClass("purple-text");
    $(".liveStatusDatat").text(mmss);
  }

  update();
});
