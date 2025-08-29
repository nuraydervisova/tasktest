from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Maraqli Fakt</title>
        </head>
        <body>
            <h1>🌐 Maraqlı Fakt: İnternetdə İlk Veb Sayt Nə İdi?</h1>
            <img src="https://ctcgulf.com/wp-content/uploads/2016/05/it4.jpg" alt="İlk veb sayt"><br><br>
            <p>Dünyanın ilk veb saytı 1991-ci ildə <em>Tim Berners-Lee</em> tərəfindən yaradılıb və yalnızca mətn-dən ibarət idi.<br><b>Saytın ünvanı:</b></p>
            <p><b><i>🔗 http://info.cern.ch</b></i></p>
            <p>Bu sayt World Wide Web-in necə işlədiyini izah edirdi – yəni indi sənin bu mesajı oxuduğun texnologiyanın başlanğıcı!</p>
            <a href='/result' style="background-color: blue; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Novbeti</a>
        </body>
    </html>
"""

sozler = [
    "Elm insanı ucaldar.",
    "Harda çox danışıq var, orda iş az olar.",
    "Dost dar gündə tanınar.",
    "Səbir hər şeyin açarıdır.",
    "Kitab insanın ən yaxşı dostudur."
]

html_sablon = """
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8"
    <title>Günün Sözü</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;       /* Üst-üstə yığır */
            justify-content: center;      /* Şaquli mərkəzləşdirmə */
            align-items: center;          /* Üfüqi mərkəzləşdirmə */
            height: 100vh;
            margin: 0;
            text-align: center;
            background-color: #f0f0f0;
            gap: 30px;                    /* Elementlər arasına məsafə verir */
            padding-top: 100px;  
        }
        .soz {
            font-size: 24px;
            padding: 30px;
            border-radius: 10px;
            width: 60%;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .button {
            margin-top: 30px;
            display: inline-block;
            background-color: green;
            color: white;
            padding: 10px 20px;
            text-decoration: none
            border-radius: 5px;
        }
        img {
            width: 300px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <img src="https://lh3.googleusercontent.com/gps-cs-s/AC9h4np8kLu-7LY2-Gmf7-UNIFgIo_snKbwDebGLoVoSgypqUkKq0Id3J6m37Z-c59ZW32h6XVV0AtmsaIMU8P7iPYYvSIcTRRfVTBCoMw8hfbhY3GlxprqQ-6Kvqs_md-PGUPaIa-TcTw=s294-w294-h220-k-no" alt="Kitab şəkli">
    <div class="soz">
        <p>{{ soz }}</p>
    </div>
    <a href="/" class="button">Əvvəlki səhifəyə keç</a>
</body>
</html>
"""
@app.route("/result")
def index():
    soz = random.choice(sozler)
    return render_template_string(html_sablon, soz=soz)

if __name__ == "__main__":
    app.run(debug=True)
