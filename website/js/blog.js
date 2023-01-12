const api_url = "https://flyyrin.pythonanywhere.com/blogs";
const minimim_spinner_time = 3000

async function getapi(url) {
    const response = await fetch(url);
    var apidata = await response.json();
    if (response) {
        return apidata
    }
}

async function loadData(data) {
    var blog = 1
    for (var i = 0; i < data.length; i++) {
        await $.get('html/blog-item.html', function (template) {
            template = template.replace("titel", data[i]["title"])
            template = template.replace("titel", data[i]["title"])
            template = template.replace("titel", data[i]["title"])
            template = template.replace("imgurl", data[i]["imgurl"])
            template = template.replace("imgurl", data[i]["imgurl"])
            template = template.replace("name", data[i]["name"])
            template = template.replace("name", data[i]["name"])
            template = template.replace("date", (data[i]["date"]))
            template = template.replace("date", (data[i]["date"]))
            template = template.replace("--id--", i)
            template = template.replace("--id--", i)
            template = template.replace("--c--", data[i]["content"])
            template = template.replace("--s--", data[i]["content"])
            $(".row").last().append(template);
            blog += 1;
            if (blog > 3) {
                $(".blogs").append('<div class="row"></div>');
                blog = 1;
            }
        })
    }
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

function hideSpinner() {
    document.getElementById('placeholderBlogs').style.display = 'none';
}

async function loadBlogs() {
    var blog = 1
    for (var i = 0; i < 9; i++) {
        await $.get('html/placeholder-blog-item.html', function (template) {
            $(".prow").last().append(template);
            blog += 1;
            if (blog > 3) {
                $(".placeholderBlogs").append('<div class="row prow"></div>');
                blog = 1;
            }
        })
    }
    data = await getapi(api_url)
    await minDelay()
    await loadData(data)
    hideSpinner();
    $(".footer").load("html/footer.html");
    checkFooter()
    $('body').removeClass('stop-scrolling')
}

window.onload = function(){
    $('body').addClass('stop-scrolling')
    $(".header").load("html/header.html");
    $(".footer").load("html/footer.html");
    checkFooter()
    loadBlogs()
}