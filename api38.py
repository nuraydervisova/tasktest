from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)  # Flask tətbiqi yaradılır

motivasiyaedici_sozler = [
    "Hər şey mümkündür!",
    "Güclü qal, davam et!",
    "Sən bacararsan!",
    "Uğur səbrin məhsuludur.",
    "Bugün yeni fürsətlər günü!"
]

maraqli_faktlar = [
    "Dünyanın ən böyük canlısı mavi balinadır.",
    "İnsan beyni saniyədə təxminən 50,000 düşüncə yaradır.",
    "Arılar rəngləri insanlardan fərqli görürlər.",
    "Kosmosda səslər ötürülmür.",
    "Dünyada 1.4 milyarddan çox ağac kəsilir hər il."
]

template = """
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8" />
    <title>Maraqli Sayt</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
            color: #333;
        }

        .card {
            background: white;
            padding: 30px 40px;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            max-width: 500px;
            text-align: center;
        }

        h1 {
            margin-bottom: 20px;
            color: #06189e;
        }

        #output {
            margin: 20px 0;
            font-size: 22px;
            font-weight: 600;
            min-height: 50px;
        }

        button {
            cursor: pointer;
            background-color: #007bff;
            border: none;
            padding: 12px 25px;
            margin: 5px;
            border-radius: 8px;
            color: white;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #0056b3;
        }

        @media (max-width: 600px) {
            body {
                height: auto;
                padding: 40px 10px;
            }

            .card {
                width: 100%;
                padding: 20px;
            }

            button {
                width: 100%;
                margin: 8px 0;
            }
        }
    </style>
</head>
<body>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBjUtbP6a4JhSBUYO7W48kONHTd3LhUPbh5cqpiMxe2o6RtChBaUoCAebyldPpxEpX4dM&usqp=CAU" 
            alt="Motivasiya şəkli" 
            style="max-width: 1000px; border-radius: 10px; margin-bottom: 100px; position: absolute; top: 50px;">
            
    <div class="card">
        <h1>Motivasiya və Maraqlı Faktlar</h1>
        <div id="output">Bir düyməyə basın və yeni söz və ya fakt alın!</div>
        <button id="motivasiya">Motivasiya Sözləri</button>
        <button id="maraqli">Maraqlı Faktlar</button>
    </div>
    <script>
        const output = document.getElementById('output');
        const motivasiyaBtn = document.getElementById('motivasiya');
        const maraqliBtn = document.getElementById('maraqli');

        motivasiyaBtn.addEventListener('click', () => {
            fetch('/api/motivasiya')
                .then(response => response.json())
                .then(data => {
                    output.textContent = data.soz;
                });
        });

        maraqliBtn.addEventListener('click', () => {
            fetch('/api/maraqli')
                .then(response => response.json())
                .then(data => {
                    output.textContent = data.fakt;
                });
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(template)

@app.route('/api/motivasiya')
def get_motivasiya():
    soz = random.choice(motivasiyaedici_sozler)
    return jsonify({'soz': soz})

@app.route('/api/maraqli')
def get_maraqli():
    fakt = random.choice(maraqli_faktlar)
    return jsonify({'fakt': fakt})

if __name__ == "__main__":
    app.run(debug=True)
