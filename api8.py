from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def hello():
  return """
<html lang="az">
<head>
    <meta charset="UTF-8" />
    <title>Sadə Səhifə</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f0f8ff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            text-align: center;
        }
        h1 {
            margin-bottom: 15px;
            color: #2c3e50;
        }
        p {
            color: #34495e;
            margin-bottom: 25px;
            line-height: 1.5;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 25px;
        }
        table, th, td {
            border: 1px solid #3498db;
        }
        th, td {
            padding: 8px;
            color: #2c3e50;
        }
        th {
            background-color: #2980b9;
            color: white;
        }
        ul {
            list-style-type: disc;
            text-align: left;
            padding-left: 20px;
            color: #34495e;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Saytımızın Məqsədi</h1>
        <p>
            Bu sayt istifadəçilərə veb inkişafı sahəsində əsas anlayışları sadə dildə təqdim etmək üçün hazırlanmışdır.
            Burada HTML, CSS və JavaScript kimi texnologiyalar haqqında qısa məlumatlar, nümunələr və tövsiyələr təqdim olunur.
            Məqsədimiz, yeni başlayanların asanlıqla öyrənməsi və layihələr yaratmasıdır.
        </p>

        <table>
            <tr>
                <th>Texnologiya</th>
                <th>Əhəmiyyəti</th>
            </tr>
            <tr>
                <td>HTML</td>
                <td>Veb səhifələrin strukturunu yaradır.</td>
            </tr>
            <tr>
                <td>CSS</td>
                <td>Səhifələrin görünüşünü tənzimləyir.</td>
            </tr>
            <tr>
                <td>JavaScript</td>
                <td>Veb səhifələrə interaktivlik əlavə edir.</td>
            </tr>
            <tr>
                <td>Python</td>
                <td>Backend proqramlaşdırma üçün istifadə olunur.</td>
            </tr>
            <tr>
                <td>SQL</td>
                <td>Məlumat bazası ilə işləməyə imkan verir.</td>
            </tr>
        </table>

        <ul>
            <li>Veb inkişafının əsasları</li>
            <li>Frontend və Backend</li>
            <li>Responsive dizayn</li>
            <li>Versiya nəzarət sistemləri</li>
            <li>Proqramlaşdırma dilləri</li>
        </ul>
    </div>
</body>
</html>
  
"""  




if __name__ == '__main__':
    app.run(debug=True)
