const api_url = "https://flyyrin.pythonanywhere.com/games";
const minimim_spinner_time = 3000
var current_apidata
var refreshInterval

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
        return apidata.reverse()
        // return apidata.slice(-3).reverse()
    }
}

function showGames() {
    $(".games").show();
} 

function hideGames() {
    $(".games").hide();
} 
  
function hideSpinner() {
    $(".placeholder").hide();
} 

function showSpinner() {
    $(".placeholder").show();
} 

async function loadData(data) {
    $(".games").empty();
    console.log(data)
    for (var i = 0; i < 3; i++) {
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
            template = template.replace("tm", data[i]["time"])
            template = template.replace("pt", `${timeSince(data[i]["date"])} geleden`)
            // `window.open('/history?game=${data.length-data.indexOf(data[i])-1}', '_blank', 'top=150,left=${(window.innerWidth/2)-150},width=300,height=500');`
            template = template.replace("oc", `window.open('/history?game=${data.length-data.indexOf(data[i])-1}', '_self');`)
            $(".games").append(template);
        })
    }
}

async function refreshFunction() {
    data = await getapi(api_url)
    if (JSON.stringify(data)!=JSON.stringify(current_apidata)) {
        hideGames()
        showSpinner();
        await loadData(data)
        hideSpinner();
        showGames();
    } 
    current_apidata = data
}

async function firstLoad() {
    data = await getapi(api_url)
    current_apidata = data
    await minDelay()
    await loadData(data)
    hideSpinner();
    showGames()
}

function minDelay() {
    return new Promise(resolve => setTimeout(resolve, minimim_spinner_time));
}  

$(document).ready(function() {
    hideGames()
    firstLoad()
    refreshInterval = setInterval(refreshFunction, 3000);
});