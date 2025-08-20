from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
<html lang="az">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Maraqlı Faktlar</http://127.0.0.1:5000title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .card {
      background: rgba(0,0,0,0.6);
      padding: 30px 40px;
      border-radius: 15px;
      width: 320px;
      text-align: center;
      box-shadow: 0 8px 15px rgba(0,0,0,0.3);
    }
    h2 {
      margin-bottom: 15px;
      font-size: 1.8em;
      text-transform: uppercase;
      letter-spacing: 2px;
    }
    p {
      font-size: 1.2em;
      line-height: 1.4;
      margin-bottom: 25px;
      min-height: 80px;
    }
    button {
      background: #ff6f61;
      border: none;
      padding: 12px 25px;
      font-size: 1em;
      border-radius: 25px;
      cursor: pointer;
      transition: background 0.3s ease;
      color: white;
    }
    button:hover {
      background: #ff3b2f;
    }
  </style>
</head>
<body>

  <div class="card">
    <h2 id="topic">Loading...</h2>
    <p id="fact">Zəhmət olmasa bir az gözləyin.</p>
    <button id="nextBtn">Növbəti Fakt</button>
  </div>

  <script>
    const facts = [
      {
        topic: "İnsan Bədəni",
        fact: "İnsan bədəni saniyədə 2 milyon hüceyrə istehsal edir."
      },
      {
        topic: "Heyvanlar Aləmi",
        fact: "Ahtapotların üç ürəyi var."
      },
      {
        topic: "Kosmos",
        fact: "Günəş sistemində ən isti planet Merkuridir, Venera deyil."
      },
      {
        topic: "Tarix və Mədəniyyət",
        fact: "Misirlilər təxminən 5000 il əvvəl piramidalar tikiblər."
      }
    ];

    let currentIndex = 0;

    const topicEl = document.getElementById("topic");
    const factEl = document.getElementById("fact");
    const nextBtn = document.getElementById("nextBtn");

    function showFact(index) {
      topicEl.textContent = facts[index].topic;
      factEl.textContent = facts[index].fact;
    }

    nextBtn.addEventListener("click", () => {
      currentIndex = (currentIndex + 1) % facts.length;
      showFact(currentIndex);
    });

    // Başlanğıcda ilk faktı göstər
    showFact(currentIndex);
  </script>

</body>
</html>

'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
