from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return """
    <html lang="az">
<head>
  <meta charset="UTF-8" />
  <title>Mənim Portfolio</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      max-width: 600px;
      margin: 40px auto;
      padding: 0 20px;
    }
    h1 {
      color: #333;
    }
    ul {
      list-style-type: square;
      padding-left: 20px;
    }
    li {
      margin-bottom: 8px;
    }
  </style>
</head>
<body>
  <h1>Salam, Mənim Adım Nuray</h1>
  <p>Mən web inkişaf etdiriciyəm və proqramlaşdırma ilə məşğulam.</p>
  <h2>Bacarıqlarım:</h2>
  <ul>
    <li>HTML & CSS</li>
    <li>JavaScript</li>
    <li>Python & Flask</li>
    <li>Git və GitHub</li>
  </ul>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
