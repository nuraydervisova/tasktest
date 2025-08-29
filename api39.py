from flask import Flask,  request, redirect, url_for, session, render_template_string

app = Flask(__name__)
app.secret_key = 'gizli_acar'


melumatlar = {
    "Kitablar": "Kitablar həyatımızın ən böyük sərmayəsidir. Hər oxunan səhifə yeni bilik və motivasiya qaynağıdır. Kitablar insanı zənginləşdirir və yeni dünyalar açır.",
    "Seyahət": "Seyahət insanın ruhunu zənginləşdirir, yeni mədəniyyətlər tanımağa imkan verir. Hər səyahət bir macəradır və həyatımıza rəng qatır.",
    "Texnologiya": "Texnologiya sürətlə inkişaf edir və həyatımızı asanlaşdırır. Yeniliklərə açıq olmaq uğurun açarıdır və daim öyrənmək vacibdir.",
    "Təbiət": "Təbiət insanın ən yaxşı müəllimidir. Sakitlik və təbiətlə iç-içə olmaq motivasiyanı artırır, enerji verir və ruhu dincəldir."
}

sekiller = {
    "Kitablar": "https://images.unsplash.com/photo-1512820790803-83ca734da794",
    "Seyahet":"https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "Texnologiya": "https://images.unsplash.com/photo-1518770660439-4636190af475",
    "Tebiet" : "https://images.unsplash.com/photo-1502082553048-f009c37129b9"
}

index_templete = """
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>task33</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: url('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Svln_svln4821_ordubad_me_best_top_photography_resimleri_sekilleri_photos_creative_profil_maraqli_sekil_resim_fotograflari_fotograf_ornek_resimler_%28344%29.JPG/2560px-Svln_svln4821_ordubad_me_best_top_photography_resimleri_sekilleri_photos_creative_profil_maraqli_sekil_resim_fotograflari_fotograf_ornek_resimler_%28344%29.JPG') no-repeat center center fixed;
            background-size: cover;
            color: white;
            text-align: center;
            padding-top: 150px;
            height: 100vh;
            margin: 0;
        }
        form {
            margin-top: 30px;
        }
        input,  button {
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            border: none;
        }
        button {
            background-color: #28a745;
            color: white;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Xos gelmisiniz:</h1>
    <form method="POST">
        <label>Adinizi daxil edin!</label><br><br>
        <input type="text" name="ad" required>
        <button type="submit">Davam et </button>
    </form>
</body>
</html>
"""
secim_templete = """
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <title>Secim et</title>
    <style>
        body {
            background: url("https://images.unsplash.com/photo-1503264116251-35a269479413") no-repeat center center fixed;
            font-family: Arial, sans-serif;
            background-size: cover;
            color: #fff;
            text-align: center;
            padding-top: 120px;
            height: 100vh;
            margin: 0;
        }
        select, button {
            padding: 12px;
            font-size: 16px;
            margin-top: 20px;
            border-radius: 8px;
            border: none; 
        }
        button {
            background-color: #007bff;
            color: white;
            cursor: pointer;
        }
        .nav {
            position: absolute;
            top: 20px;
            left: 20px;
        }
        .nav a {
            background: rgba(225,225,225,0.3);
            padding: 10px 15px;
            border-radius: 8px;
            color: white;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="nav">
        <a href="{{url_for('index') }}">← Əsas səhifə</a>
    </div>
    <h1>Bir seçim edin, {{ ad }}</h1>
    <form method="POST">
        <select name="secim" required>
            <option value="">--Secin--</option>
            <option value="Kitablar">Kitablar</option>
            <option value="Seyahet">Seyahet</option>
            <option value="Texnologiya">Texnologiya</option>
            <option value="Tebiet">Tebiet</option>
        </select><br>
        <button type="submit">Neticeye kec</button>
    </form>
</body>
</html>
"""
netice_templete = """
<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <title>Netice</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color:   #e8f5e9;
            padding-top: 120px;
            text-align: center;
            margin: 0;
            height: 100vh;
            }
        .card {
            background: white;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            display: inline-block;
            max-width: 600px;
            padding: 40px 60px;
        }
        .nav {
            position; absolute;
            top: 20px;
            left: 20px; 
        }
        .nav a {
            padding: 10px 15px
            color: #333;
            text-decoration: none;
            border-radius: 8px
            background: #d4edda;
        }
    </style>
</head>
<body>
    <div class="nav">
        <a href="{{url_for('index')}}">← Əsas səhifə</a>
    </div>
    <div class="card">
        <h>1Tebrikler, {{ ad }}! 🎉</h1>
        <p>Siz <strong>{{ secim }}</strong> secdiniz</p>
        <p style="margin-top: 20px; font-style: italic; color: #555;">{{melumat}}</p>
    </div>
    <img src="{{sekil_url}}" alt ="Movzu sekil" style="max-width: 100%; margin-top: 30px; border-radius: 12px;">
</body>
</html>
"""
@app.route("/", methods=["GET", "POST"])
def index ():
    if request.method == "POST":
        ad = request.form.get("ad")
        if ad:
            session["ad"] = ad
            return redirect(url_for("secim"))
    return render_template_string(index_templete)
    
@app.route("/secim", methods=["GET", "POST"])
def secim():
    ad = session.get("ad", 'Istifadeci')
    if request.method == "POST":
        secim = request.form.get("secim")
        if secim:
            session["secim"] = secim
            return redirect(url_for('netice'))
    return render_template_string(secim_templete, ad=ad)

@app.route("/netice")
def netice():
    ad = session.get("ad", "Istifadeci")
    secim = session.get("secim", "namelum")
    melumat = melumatlar.get(secim, "")
    sekil_url = sekiller.get(secim, "")
    return render_template_string(netice_templete, ad=ad, secim=secim, melumat=melumat, sekil_url=sekil_url)      

if __name__ == '__main__':
    app.run(debug=True)
