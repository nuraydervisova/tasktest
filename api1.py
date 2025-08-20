from flask import Flask 

app = Flask(__name__)

@app.route('/')
def my_sayt():
    return '''
<html>
<head>
  <title>Mənim Saytım</title>
</head>
<body>
  <h1>Salam Dünya!</h1>
  <p>Bu, mənim ilk HTML səhifəmdir.</p>
  <a href="https://example.com">Sayta keç</a>
  <ul>
    <li>Element 1</li>
    <li>Element 2</li>
  </ul>
  <form>
    <label for="ad">Adınız:</label>
    <input type="text" id="ad" name="ad" required>
    <button type="submit">Göndər</button>
  </form>
</body>
</html>
'''


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000)
