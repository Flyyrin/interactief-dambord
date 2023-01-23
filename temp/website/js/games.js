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
        return apidata
    }
}
  
function hideSpinner() {
    document.getElementById('placeholder').style.display = 'none';
} 

function showSpinner() {
    document.getElementById('placeholder').style.display = 'block';
} 

async function loadData(data) {
    for (var i = 0; i < data.length; i++) {
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

async function refreshFunction() {
    data = await getapi(api_url)
    if (JSON.stringify(data)!=JSON.stringify(current_apidata)) {
        $(".table").empty();
        showSpinner();
        await loadData(data)
        checkFooter()
        hideSpinner();
        checkFooter()
    } 
    current_apidata = data
}

async function firstLoad() {
    for (var i = 0; i < 10; i++) {
        await $.get('html/placeholder-game-item.html', function (template) {  
            $(".ptable").append(template);
        })
    }
    data = await getapi(api_url)
    current_apidata = data
    await minDelay()
    await loadData(data)
    hideSpinner();
    $(".footer").load("html/footer.html");
    checkFooter()
    $('body').removeClass('stop-scrolling')
}

function checkFooter() {
    if ($("html").height() > $(window).height()) {
        $(".footer").removeClass("fixed-bottom")
    } else {
        $(".footer").addClass("fixed-bottom")
    }
}

function minDelay() {
    return new Promise(resolve => setTimeout(resolve, minimim_spinner_time));
}  

window.onload = function() {
    $('body').addClass('stop-scrolling')
    $(".header").load("html/header.html");
    $(".footer").load("html/footer.html");
    checkFooter()
    firstLoad()
    refreshInterval = setInterval(refreshFunction, 3000);
}