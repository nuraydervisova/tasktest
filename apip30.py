from flask import Flask, render_template_string

app = Flask(__name__)

html_page = '''
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8" />
    <title>Azərbaycanın Məşhur Şəhərləri</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px auto;
            max-width: 700px;
            line-height: 1.6;
            color: #333;
            background: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: #006633;
        }
        .city {
            margin-bottom: 30px;
        }
        .city img {
            max-width: 100%;
            border-radius: 6px;
            margin-top: 10px;
            margin-bottom: 10px;
        }
        a {
            color: #006633;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        footer {
            margin-top: 40px;
            text-align: center;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>
<body>
    <h1>Azərbaycanın Məşhur Şəhərləri</h1>

    <div class="city">
        <h2>Bakı</h2>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Baku_Cityscape_July_2019_panorama.jpg/640px-Baku_Cityscape_July_2019_panorama.jpg" alt="Bakı şəhəri" />
        <p>Bakı — Azərbaycanın paytaxtı və ən böyük şəhəridir. Xəzər dənizinin sahilində yerləşir və zəngin tarixi, mədəniyyəti ilə məşhurdur.</p>
        <p><a href="https://az.wikipedia.org/wiki/Bakı" target="_blank">Daha ətraflı</a></p>
    </div>

    <div class="city">
        <h2>Gəncə</h2>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Ganja_Azerbaijan_2019.jpg/640px-Ganja_Azerbaijan_2019.jpg" alt="Gəncə şəhəri" />
        <p>Gəncə Azərbaycanın ikinci ən böyük şəhəridir. Tarixi və memarlıq abidələri ilə zəngindir.</p>
        <p><a href="https://az.wikipedia.org/wiki/Gəncə" target="_blank">Daha ətraflı</a></p>
    </div>

    <div class="city">
        <h2>Şəki</h2>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/%C5%9E%C9%99ki_-_UNESCO_World_Heritage_Site_in_Azerbaijan_01.jpg/640px-%C5%9E%C9%99ki_-_UNESCO_World_Heritage_Site_in_Azerbaijan_01.jpg" alt="Şəki şəhəri" />
        <p>Şəki Azərbaycanın qədim şəhərlərindən biridir və UNESCO-nun Dünya İrsi Siyahısına daxildir.</p>
        <p><a href="https://az.wikipedia.org/wiki/Şəki" target="_blank">Daha ətraflı</a></p>
    </div>

    <footer>
        © 2025 Sadə Məlumat Saytı
    </footer>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_page)

if __name__ == '__main__':
    app.run(debug=True)
