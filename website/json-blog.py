blogs = [
    {
        "title": "Week 1 : 26 - 30 september",
        "name": "Michael Van Walderveen",
        "date": "12-01-2023",
        "content": "<h3> maandag 26 september: </h3>\r\nUitleg project gekregen. Github en Team aangemaakt.\r\n\r\nWerking led strip uitgezocht. Nagedacht over website maken.\r\n\r\n<h3>Donderdag 29 september:</h3>\r\nRepository voor de website aangemaakt\r\n\r\nWebsite opgebouwd en basis gemaakt.",
        "imgurl": "http://flyyrin.pythonanywhere.com/media/14d4d852-fc73-4bec-9179-d637a2a83d55.png"
    },
    {
        "title": "Week 2 : 3 - 7 oktober",
        "name": "Michael Van Walderveen",
        "date": "29-01-2023",
        "content": "<h3> Maandag 3 oktober: </h3>\r\n\r\nBlog post programma gemaakt, led code voorbereid om te testen.\r\nVerder site opbouwen.\r\n\r\n<h3> Donderdag 7 oktober: </h3>\r\n\r\nSite afgemaakt en getest, voorbereidingen voor code.",
        "imgurl": "http://flyyrin.pythonanywhere.com/media/6ce29c70-55c6-49a4-851e-f6f27b7e7ecb.png"
    },
    {
        "title": "Week 3: 10 - 14 oktober",
        "name": "Michael Van Walderveen",
        "date": "29-01-2023",
        "content": "<h3> Maandag 10 oktober: </h3>\r\n\r\nJoystick werking en bekabeling afmaken. \r\nVoorbereiding joystick detectie code.\r\n\r\n<h3> Donderdag 13 oktober: </h3>\r\n\r\nDambord lay-out uitgewerkt en led-aansturing hier op aangepast zodat iedere cel co\u00f6rdinaten heeft en aangestuurd kan worden.",
        "imgurl": "http://flyyrin.pythonanywhere.com/media/7d4f64a6-1f11-493d-872c-9ba6512b6b9d.png"
    },
    {
        "title": "Week 4 : 17 - 21 oktober",
        "name": "Michael Van Walderveen",
        "date": "29-01-2023",
        "content": "<h3> Maandag 17 oktober: </h3>\r\n\r\nBeide joysticks gesoldeerd en werking gecontroleerd.\r\n\r\n<h3> Donderdag 20 oktober: </h3>\r\n\r\nJoystick herkenningscode af en begin damspel.",
        "imgurl": "http://flyyrin.pythonanywhere.com/media/9f06acd8-3e94-474b-9c94-432fed1169ca.png"
    },
    {
        "title": "Week 5 : 21 - 25 november",
        "name": "Michael Van Walderveen",
        "date": "29-01-2023",
        "content": "<h3> Maandag 21 november: </h3>\r\n\r\nWebsite verder opgeknapt. Begonnen met regels toevoegen aan damspel.\r\n\r\n<h3> Donderdag  25 november </h3>\r\n\r\nWebsite home en blogpagina afgemaakt en damspel regels toegevoegd. ",
        "imgurl": "http://flyyrin.pythonanywhere.com/media/2f7398f2-1e69-4c82-ba12-2105c4540171.png"
    },
    {
        "title": "Week 6 : 28 november - 2 december",
        "name": "Michael Van Walderveen",
        "date": "29-01-2023",
        "content": "<h3> Maandag 28 november: </h3>\r\n\r\nDamspel verder afwerken en testen.\r\n\r\n<h3> Donderdag 2 december: </h3>\r\n\r\nDamspel werkend gekregen met 1 joystick en een deel van de regels.",
        "imgurl": "http://flyyrin.pythonanywhere.com/media/315a9130-9147-4c15-8965-82a57dbc3817.png"
    },
    {
        "title": "Week 7 t/m 9 : Kerstvakantie",
        "name": "Rafael Lemmen",
        "date": "29-01-2023",
        "content": "Lay-out van website verbeterd, Ganttproject planning gemaakt.\r\n\r\nVerdere regels afgewerkt van damspel en begonnen met werking van 2 spelers en dus 2 joysticks.",
        "imgurl": "http://flyyrin.pythonanywhere.com/media/6405bf7a-d313-4df9-a557-f2664b74e4ce.jpg"
    },
    {
        "title": "Week 10 t/m 12 : 9 - 27 januari",
        "name": "Rafael Lemmen",
        "date": "29-01-2023",
        "content": "Opruimen van GitHub, site lay-out opnieuw verbeterd, verbeteringen van de regels in het damspel, werking met 2 joysticks afgemaakt en begonnen met toevoegen van extra idee\u00ebn zoals led animaties in het spel. ",
        "imgurl": "http://flyyrin.pythonanywhere.com/media/a9a509d4-b672-4108-b77a-0ad13e1f7027.jpg"
    },
    {
        "title": "<H1> DE WCROL <\\H1>",
        "name": "Michael Van Walderveen",
        "date": "27-02-2023",
        "content": "<H1> DE WCROL VAN MICHAEL <\\H1>",
        "imgurl": "http://flyyrin.pythonanywhere.com/media/c0d88e24-113f-4c6d-bc35-a82a0486e591.jpg"
    },
    {
        "title": "<H1> vader en zoon <\\H1>",
        "name": "Michael Van Walderveen",
        "date": "27-02-2023",
        "content": "vader en zoon",
        "imgurl": "http://flyyrin.pythonanywhere.com/media/048444ba-9f8c-4489-8eb8-f51e511d13a0.png"
    }
]

blog_html = """
    <div class="embla__slide slider-image item" style="margin-left: 1rem; margin-right: 1rem;">
        <div class="slide-content">
            <div class="item-wrapper">
                <div class="item-img">
                    <img src="images/blog/imagearea.jpg" alt="Blog">
                </div>
            </div>
            <div class="item-content">
                <h5 class="item-title bs-fonts-style display-7"><strong> titelarea </strong></h5>
                <p class="bs-text bs-fonts-style mt-3 display-7"> textarea </p>
            </div> 
        </div>
    </div>
"""

for blog in blogs:
    done_blog_html = blog_html.replace("titelarea", blog["title"])
    done_blog_html = done_blog_html.replace("textarea", blog["content"])
    done_blog_html = done_blog_html.replace("imagearea", blog["imgurl"])
    print(done_blog_html)
