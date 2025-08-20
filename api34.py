from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return """
    <html lang="az">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>İnsan Beyni Haqqında Maraqlı Məlumatlar</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #283e51, #485563);
      color: #e0e0e0;
      margin: 0;
      padding: 20px;
      line-height: 1.6;
    }
    .container {
      max-width: 900px;
      margin: 0 auto;
      background: rgba(0, 0, 0, 0.7);
      padding: 30px 40px;
      border-radius: 12px;
      box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    }
    h1 {
      font-size: 2.5em;
      text-align: center;
      margin-bottom: 15px;
      color: #00bfff;
    }
    h2 {
      color: #00aaff;
      margin-top: 30px;
      margin-bottom: 15px;
      border-bottom: 2px solid #00aaff;
      padding-bottom: 5px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 25px;
    }
    th, td {
      border: 1px solid #444;
      padding: 12px 15px;
      text-align: left;
    }
    th {
      background-color: #005f99;
      color: #fff;
    }
    tr:nth-child(even) {
      background-color: #1e2f43;
    }
    ul {
      list-style: none;
      padding-left: 0;
    }
    ul li {
      margin-bottom: 10px;
      padding-left: 25px;
      position: relative;
    }
    ul li::before {
      content: "🧠";
      position: absolute;
      left: 0;
      top: 0;
    }
    .fact-list li::before {
      content: "🔹";
    }
    .fact-list {
      padding-left: 20px;
      list-style-type: none;
      color: #cceeff;
    }
    p {
      margin-bottom: 15px;
      font-size: 1.1em;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>🧠 İnsan Beyni Haqqında Maraqlı Məlumatlar</h1>

    <p>İnsan beyni bədənimizin ən kompleks və sirli orqanlarından biridir. Təxminən 1.3–1.4 kq ağırlığında olsa da, bədənimizin funksiyalarını idarə edir, düşünür, hiss edir və yadda saxlayır. Alimlər hələ də onun bütün sirrlərini tam aça bilməyiblər. Aşağıda bu möcüzəvi orqan haqqında maraqlı faktları təqdim edirik:</p>

    <h2>🔍 Ümumi Məlumatlar</h2>
    <table>
      <tr>
        <th>Xüsusiyyət</th>
        <th>Təfərrüat</th>
      </tr>
      <tr>
        <td>Orta çəkisi</td>
        <td>1.3–1.4 kq</td>
      </tr>
      <tr>
        <td>Enerji istehlakı</td>
        <td>Bədənin ümumi enerjisinin 20%-i</td>
      </tr>
      <tr>
        <td>Neyron sayı</td>
        <td>Təxminən 86 milyard</td>
      </tr>
      <tr>
        <td>Məlumat ötürmə sürəti</td>
        <td>250 mil/saniyəyə qədər</td>
      </tr>
      <tr>
        <td>Su tərkibi</td>
        <td>73%</td>
      </tr>
    </table>

    <h2>🧩 Maraqlı Faktlar</h2>
    <ul class="fact-list">
      <li><strong>Yaddaş məkan problemi:</strong> İnsan beynindəki yaddaş məkanının həcmi tam olaraq bilinməsə də, bəzi araşdırmalara görə bu, təxminən 2.5 petabayt-a qədər çata bilər. Bu, 3 milyon saatlıq video yaddaşa bərabərdir!</li>
      <li><strong>Beyin ağrını hiss etmir:</strong> Maraqlıdır ki, beyin özü ağrı reseptorlarına malik deyil, yəni o birbaşa ağrı hiss etmir. Buna görə beyin əməliyyatları bəzən xəstə ayıq halda aparılır.</li>
      <li><strong>Yuxu zamanı aktivlik:</strong> İnsan yuxuda olarkən beyin bəzən oyaq haldakından daha aktiv olur. Bu, yuxuların və yaddaşın emal prosesi ilə bağlıdır.</li>
      <li><strong>Sol və sağ yarımkürələr:</strong> Beynin sol tərəfi daha çox məntiq, analiz və dil bacarıqlarını, sağ tərəfi isə incəsənət, musiqi və vizual düşünməni idarə edir.</li>
    </ul>

    <h2>🧪 Beyni Gücləndirən Fəaliyyətlər</h2>
    <table>
      <tr>
        <th>Fəaliyyət</th>
        <th>Təsiri</th>
      </tr>
      <tr>
        <td>Kitab oxumaq</td>
        <td>Yaddaşı və diqqəti gücləndirir</td>
      </tr>
      <tr>
        <td>Fiziki idman</td>
        <td>Qan dövranını artıraraq beyin funksiyalarını yaxşılaşdırır</td>
      </tr>
      <tr>
        <td>Yeni bacarıqlar öyrənmək</td>
        <td>Neyronlar arasında yeni əlaqələr yaradır</td>
      </tr>
      <tr>
        <td>Sağlam qidalanma</td>
        <td>Beynin enerji və vitamin balansını qoruyur</td>
      </tr>
      <tr>
        <td>Musiqi dinləmək və ifa etmək</td>
        <td>Koordinasiya və emosional sabitliyi artırır</td>
      </tr>
    </table>

    <h2>📌 Qısa Faktlar</h2>
    <ul class="fact-list">
      <li>Beyin 1 dəqiqədə 1,000 söz təhlil edə bilər.</li>
      <li>Bir insan gündə təxminən 60,000 fikir düşünür.</li>
      <li>Alkoqol beynin qərarvermə və yaddaş mərkəzinə mənfi təsir edir.</li>
    </ul>

  </div>

</body>
</html>
   
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
