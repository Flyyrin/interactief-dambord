const api_url = "http://flyyrin.pythonanywhere.com/";
var current_apidata

const colors = {
    "red": "#fc4c4f",
    "blue": "#4fa3fc",
    "yellow": "#ECD13F",
    "green": "#4bec3f",
    "purple": "#cf3fec"
}
  
async function getapi(url) {
    const response = await fetch(url);
    var apidata = await response.json();
    if (response) {
        hideSpinner();
        await loadData(apidata)
        $(".footer").load("html/footer.html");
    }
}
  
function hideSpinner() {
    document.getElementById('spinner').style.display = 'none';
} 

async function loadData(data) {
    for (var i = 0; i < data.length; i++) {
        console.log(data[i])
        await $.get('html/game-item.html', function (template) {
            template = template.replace("player1", data[i]["player1"]["name"])
            template = template.replace("player2", data[i]["player2"]["name"])
            if (data[i]["winner"] == 1) {
                template = template.replace("p1w", "winner")
            }
            if (data[i]["winner"] == 2) {
                template = template.replace("p2w", "winner")
            }
            template = template.replace("cp1", colors[data[i]["player1"]["color"]])
            template = template.replace("cp2", colors[data[i]["player2"]["color"]])
            console.log(data[i]["date"])
            template = template.replace("pt", timeSince(data[i]["date"]))
            
            $(".table").append(template);
        })
    }
}

function timeSince(date) {
    var seconds = Math.floor((new Date() - date) / 1000);
    var interval = seconds / 31536000;
    if (interval > 1) {
      return Math.floor(interval) + " years";
    }
    interval = seconds / 2592000;
    if (interval > 1) {
      return Math.floor(interval) + " months";
    }
    interval = seconds / 86400;
    if (interval > 1) {
      return Math.floor(interval) + " days";
    }
    interval = seconds / 3600;
    if (interval > 1) {
      return Math.floor(interval) + " hours";
    }
    interval = seconds / 60;
    if (interval > 1) {
      return Math.floor(interval) + " minutes";
    }
    return Math.floor(seconds) + " seconds";
}

window.onload = function() {
    $(".header").load("html/header.html");
    getapi(api_url);
}