$(document).ready(function () {
  const newStartTime = Date.now() - 0 * 60 * 1000;
  const server = "https://flyyrin.pythonanywhere.com/game";
  var currentData = [];
  const colors = {
    c: "#4de1ff",
    h: "#ffffff",
    p: "#eba152",
    e: "#00000000",
    red: "#fc4c4f",
    blue: "#4fa3fc",
    yellow: "#ECD13F",
    green: "#4bec3f",
    purple: "#cf3fec",
    "king-red": "#ff0004",
    "king-blue": "#007bff",
    "king-yellow": "#d6b500",
    "king-green": "#0cad00",
    "king-purple": "#a200c3",
  };

  maindata = {
    game: true,
    winner: 1,
    gameData: {
      np1: "Rafael",
      np2: "Michael",
      cp1: "red",
      cp2: "purple",
      currentTime: 0,
      startTime: newStartTime,
      playing: 2,
      pieces: {
        player1: {
          pieces: 0,
          kings: 0,
          captured: 0,
        },
        player2: {
          pieces: 0,
          kings: 0,
          captured: 0,
        },
      },
      board: {
        0: "e",
        1: 1,
        2: "e",
        3: 1,
        4: "e",
        5: 1,
        6: "e",
        7: 1,
        8: "e",
        9: 1,
        10: "e",
        11: 1,
        12: "e",
        13: 1,
        14: "e",
        15: 1,
        16: "e",
        17: 1,
        18: "e",
        19: 1,
        20: "e",
        21: 1,
        22: "e",
        23: 1,
        24: "e",
        25: "e",
        26: "e",
        27: "e",
        28: "e",
        29: "e",
        30: "e",
        31: "e",
        32: "e",
        33: "e",
        34: "e",
        35: "e",
        36: "e",
        37: "e",
        38: "e",
        39: "e",
        40: "e",
        41: 2,
        42: "e",
        43: 2,
        44: "e",
        45: 2,
        46: "e",
        47: 2,
        48: "e",
        49: 2,
        50: "e",
        51: 2,
        52: "e",
        53: 2,
        54: "e",
        55: 2,
        56: "e",
        57: 2,
        58: "e",
        59: 2,
        60: "e",
        61: 2,
        62: "e",
        63: 2,
      },
    },
  };

  function update() {
    var newData = [
      maindata.gameData.np1,
      maindata.gameData.np2,
      maindata.gameData.cp1,
      maindata.gameData.cp2,
    ];
    if (newData != currentData) {
      currentData = newData;
      $(".player1").attr("class", "playertag player1");
      $(".player2").attr("class", "playertag player2");
      $(".player1").html(maindata.gameData.np1);
      $(".player2").html(maindata.gameData.np2);
      $(".player1").addClass(maindata.gameData.cp1 + "-text");
      $(".player2").addClass(maindata.gameData.cp2 + "-text");
    }

    if (!maindata.game && !maindata.winner) {
      $("#noGameModal").modal("show");
    } else if (!maindata.game && maindata.winner) {
      $("#noGameModal").modal("hide");
      $(".winner").attr("class", "winner black-text-shadow");
      if (maindata.winner == 1) {
        $(".winner").text(maindata.gameData.np1);
        $(".winner").addClass(maindata.gameData.cp1 + "-text");
      }
      if (maindata.winner == 2) {
        $(".winner").text(maindata.gameData.np2);
        $(".winner").addClass(maindata.gameData.cp2 + "-text");
      }
      $("#winnerModal").modal("show");
    } else {
      $("#noGameModal").modal("hide");
      $("#winnerModal").modal("hide");
      var startTime = new Date(maindata.gameData.startTime);
      var currentTime = new Date(maindata.gameData.currentTime);
      var alphaSeconds = (Date.now() - startTime.getTime()) / 1000;
      var mmss = new Date(alphaSeconds * 1000).toISOString().substring(14, 19);
      $(".timer").html(mmss);

      if (maindata.gameData.playing == 1) {
        $(".player1").addClass("playing");
        $(".player2").removeClass("playing");
      }
      if (maindata.gameData.playing == 2) {
        $(".player2").addClass("playing");
        $(".player1").removeClass("playing");
      }

      $(".player1-pieces").html(
        $(".player1-pieces").html().split(":")[0] +
          ": " +
          maindata.gameData.pieces.player1.pieces
      );
      $(".player1-kings").html(
        $(".player1-kings").html().split(":")[0] +
          ": " +
          maindata.gameData.pieces.player1.kings
      );
      $(".player1-captured").html(
        $(".player1-captured").html().split(":")[0] +
          ": " +
          maindata.gameData.pieces.player1.captured
      );
      $(".player2-pieces").html(
        $(".player2-pieces").html().split(":")[0] +
          ": " +
          maindata.gameData.pieces.player2.pieces
      );
      $(".player2-kings").html(
        $(".player2-kings").html().split(":")[0] +
          ": " +
          maindata.gameData.pieces.player2.kings
      );
      $(".player2-captured").html(
        $(".player2-captured").html().split(":")[0] +
          ": " +
          maindata.gameData.pieces.player2.captured
      );

      $.each(maindata.gameData.board, function (position, piece) {
        if (piece == 1) {
          $(`.board > svg > #${position}`).attr(
            "fill",
            colors[maindata.gameData.cp1]
          );
        }
        if (piece == 3) {
          $(`.board > svg > #${position}`).attr(
            "fill",
            colors[`king-${maindata.gameData.cp1}`]
          );
        }
        if (piece == 2) {
          $(`.board > svg > #${position}`).attr(
            "fill",
            colors[maindata.gameData.cp2]
          );
        }
        if (piece == 4) {
          $(`.board > svg > #${position}`).attr(
            "fill",
            colors[`king-${maindata.gameData.cp2}`]
          );
        }
        if (piece == "e") {
          $(`.board > svg > #${position}`).attr("fill", colors[piece]);
        }
        if (piece == "c") {
          $(`.board > svg > #${position}`).attr("fill", colors[piece]);
        }
        if (piece == "h") {
          $(`.board > svg > #${position}`).attr("fill", colors[piece]);
        }
        if (piece == "p") {
          $(`.board > svg > #${position}`).attr("fill", colors[piece]);
        }
      });
    }
  }

  if ($(window).width() < 960) {
    $(".board").load("images/m-board.svg");
    $(".pieces").removeClass("d-flex");
    $(".pieces").hide();
  } else {
    $(".board").load("images/board.svg");
  }

  const serverTest = "scripts/testGame.json";
  var gameHistory = [];

  $.get(serverTest, function (data) {
    gameHistory = data;
    steps = gameHistory.length;
    var totalTime = 0;
    var start = true;
    let totalDelay = 0;

    $.each(gameHistory, function (index, board) {
      // Generate a random delay between 3000 and 5000 ms for each iteration
      var delay = Math.floor(Math.random() * (5000 - 3000 + 1)) + 3000;
      if (start) {
        delay = 10;
        start = false;
      }
      totalTime += delay;

      // Increment the totalDelay by the delay of this iteration, so the next iteration will wait after this one
      totalDelay += delay;

      // Use setTimeout with the cumulative totalDelay to ensure the correct sequence
      setTimeout(function () {
        console.log(index); // Print index
        maindata.gameData.board = board; // Update gameData with the current board

        // Toggle player
        if (maindata.gameData.playing == 1) {
          maindata.gameData.playing = 2;
        } else {
          maindata.gameData.playing = 1;
        }

        processPieces(board);
        update(); // Call the update function
      }, totalDelay); // Sequential delay based on the cumulative time
    });

    setTimeout(function () {
      maindata.game = false;
    }, totalTime);
  });

  function startTimer() {
    let timer = 0; // Start with a 60-second timer (you can change this to any value)

    // Update the timer every 500 milliseconds
    const timerInterval = setInterval(function () {
      var startTime = new Date(maindata.gameData.startTime);
      var currentTime = new Date(maindata.gameData.currentTime);
      var alphaSeconds = (Date.now() - startTime.getTime()) / 1000;
      var mmss = new Date(alphaSeconds * 1000).toISOString().substring(14, 19);
      $(".timer").html(mmss);
    }, 500); // Update every 500 milliseconds
  }

  startTimer();
  update();
});

function processPieces(input) {
  // Iterate over the input data
  maindata.gameData.pieces.player1.pieces = 0;
  maindata.gameData.pieces.player1.kings = 0;
  maindata.gameData.pieces.player1.captured = 12;

  maindata.gameData.pieces.player2.pieces = 0;
  maindata.gameData.pieces.player2.kings = 0;
  maindata.gameData.pieces.player2.captured = 12;

  $.each(input, function (index, value) {
    if (value === 1) {
      // Player 1 piece
      maindata.gameData.pieces.player1.pieces++;
    } else if (value === 3) {
      // Player 1 king
      maindata.gameData.pieces.player1.kings++;
    } else if (value === 4) {
      // Player 2 king
      maindata.gameData.pieces.player2.kings++;
    } else if (value === 2) {
      // Player 2 piece
      maindata.gameData.pieces.player2.pieces++;
    }
  });

  maindata.gameData.pieces.player1.captured =
    12 - maindata.gameData.pieces.player2.pieces;
  maindata.gameData.pieces.player2.captured =
    12 - maindata.gameData.pieces.player1.pieces;
}
