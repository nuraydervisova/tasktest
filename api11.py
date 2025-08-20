from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """

<html lang="az">
<head>
  <meta charset="UTF-8" />
  <title>Əlaqə Forması</title>
  <style>
    body {
      font-family: Verdana, sans-serif;
      background: #fffbe6;
      display: flex;
      justify-content: center;
      padding-top: 50px;
    }
    form {
      background: #ffecb3;
      padding: 20px;
      border-radius: 10px;
      width: 300px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    input, textarea {
      width: 100%;
      margin-bottom: 10px;
      padding: 8px;
      border: 1px solid #aaa;
      border-radius: 4px;
      font-size: 1em;
    }
    button {
      background: #ff9800;
      border: none;
      padding: 10px;
      width: 100%;
      border-radius: 5px;
      color: white;
      font-weight: bold;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <form>
    <input type="text" placeholder="Adınız" required />
    <textarea rows="4" placeholder="Mesajınız" required></textarea>
    <button type="submit">Göndər</button>
  </form>
</body>
</html>
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
