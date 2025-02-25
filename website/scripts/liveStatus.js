$(document).ready(function () {
  const server = "https://flyyrin.pythonanywhere.com/game";

  function update() {
    $(".liveStatus").text("Live Game (not active)");
    $(".liveStatusData").hide();
    $(".liveStatusDivider").hide();
  }

  update();
});
