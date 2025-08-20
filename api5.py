from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def new_file():
    return """ 
<html lang="az">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Menim Yeni Saytim</title>
</head>
<body>
    <h1>Xos gelmisiz!</h1>
    <p>Bu, yeni yaratdigim saytin ilk sehifesidir.</p>

    <a href="https://example.com" target="_blank">Sayta keçid</a>


    <h2>Menim sevimli meyvelerim</h2>
    <ul>
        <li>Alma</li>
        <li>Banan</li>
        <li>Ciyelek</li>
        <li>Nar</li>
        <li>Qarpiz</li>

    </ul>
    <h2>Elave formasi</h2>
    <form action="/gonder" method="post">
        <label for="ad">Adiniz:</label><br />
        <input type="text" id="ad" name="ad" placeholder="Adinizi yazin" /><br /><br />
        <button type="submit">Gonder</button>
    </form>
</body>
</html>
"""
@app.route('/gonder', methods=['POST'])
def gonder():
    ad = request.form.get('ad')
    if not ad:
        return "h1>Ad daxil edilmeyib. Zehmet olmasa ad daxil edin.</h1>"
    return f"<h1>salam, {ad}! Form ugurla daxil edildi.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

app = Flask(__name__)


@app.route('/')
def new_file():
    return """ 
<html lang="az">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Menim Yeni Saytim</title>
</head>
<body>
    <h1>Xos gelmisiz!</h1>
    <p>Bu, yeni yaratdigim saytin ilk sehifesidir.</p>

    <a href="https://example.com" target="_blank">Sayta keçid</a>


    <h2>Menim sevimli meyvelerim</h2>
    <ul>
        <li>Alma</li>
        <li>Banan</li>
        <li>Ciyelek</li>
        <li>Nar</li>
        <li>Qarpiz</li>

    </ul>
    <h2>Elave formasi</h2>
    <form action="/gonder" method="post">
        <label for="ad">Adiniz:</label><br />
        <input type="text" id="ad" name="ad" placeholder="Adinizi yazin" /><br /><br />
        <button type="submit">Gonder</button>
    </form>
</body>
</html>
"""
@app.route('/gonder', methods=['POST'])
def gonder():
    ad = request.form.get('ad')
    if not ad:
        return "h1>Ad daxil edilmeyib. Zehmet olmasa ad daxil edin.</h1>"
    return f"<h1>salam, {ad}! Form ugurla daxil edildi.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
