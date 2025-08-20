from flask import Flask

app = Flask(__name__)

@app.route('/')
def sayt_yeni(): 
  return """
<html lang="az">
<head>
  <meta charset="UTF-8">
  <title>Sadə Cədvəl</title>
</head>
<body>

  <h2>İşçi Siyahısı</h2>

  <table border="1" cellpadding="8" cellspacing="0">
    <tr>
      <th>Ad</th>
      <th>Soyad</th>
      <th>Yaş</th>
      <th>Vəzifə</th>
    </tr>
    <tr>
      <td>Əli</td>
      <td>Məmmədov</td>
      <td>30</td>
      <td>Proqramçı</td>
    </tr>
    <tr>
      <td>Günay</td>
      <td>Qasımova</td>
      <td>25</td>
      <td>Dizayner</td>
    </tr>
    <tr>
      <td>Rəşad</td>
      <td>Hüseynov</td>
      <td>28</td>
      <td>Menecer</td>
    </tr>
  </table>

</body>
</html>
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
