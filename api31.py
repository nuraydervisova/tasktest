from flask import Flask, request, redirect, url_for

app = Flask(__name__)

neticeler = []

siyahilar = {
    "Meyveler": {"Alma": 3, "Banan": 4, "Ciyelek": 5, "Nar": 2, "Qarpiz": 1},
    "Heyvanlar": {"Pişik": 5, "İt": 4, "At": 3, "Dovşan": 2, "Quş": 1},
    "Rengler": {"Qirmizi": 5, "Yasil": 4, "Goy": 3, "Sari": 2, "Qara": 1},
    "Avtomobiller": {"BMW": 4, "Mercedes": 5, "Toyota": 3, "Audi": 2, "Ford": 1},
    "Desertler": {"Sokolad": 5, "Pecenye": 4, "Dondurma": 3, "Paxlava": 2, "Keks": 1}
}

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Ana səhifə</title></head>
    <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 100px;">
        <h1><strong><i>Xoş gəlmisiniz❗</i></strong></h1>
        <p>
            Bu sayt qısa anket forması təqdim edir.🌟 <br>
            Burada anket suallarına qısa cavablar verməklə puanlar qazanırsınız.😊<br>
            <mark>Bol şanslar🍀</mark>
        </p>
        <a href="/anket" style="font-size: 20px; color: white; background-color: green; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Anketi Başla➡️</a>
    </body>
    </html>
    '''

@app.route('/anket', methods=['GET', 'POST'])
def anket():
    if request.method == 'POST':
        ad = request.form.get('ad', '').strip()
        soyad = request.form.get('soyad', '').strip()

        secimler = {}
        for siyahi in siyahilar:
            sec = request.form.get(siyahi)
            if not sec or sec not in siyahilar[siyahi]:
                return f'<h3>Zəhmət olmasa {siyahi} üçün düzgün seçim edin.😊</h3><a href="/anket">⬅️Geri</a>'
            secimler[siyahi] = sec

        if not ad or not soyad:
            return '<h3>Ad və soyad daxil edilməlidir!</h3><a href="/anket">⬅️Geri</a>'

        neticeler.append({
            "ad": ad,
            "soyad": soyad,
            "secimler": secimler
        })

        return redirect(url_for('netice'))

    # Form HTML hissəsi
    form_html = '''
    <html>
    <head><title>Anket Formu</title></head>
    <body style="background-color: #2e8b57; color: white; font-family: Arial, sans-serif;">
    <div style="max-width: 500px; margin: 50px auto; background-color: #3cb371; padding: 20px; border-radius: 10px;">
        <h2 style="text-align:center;">Anket Formu</h2>
        <form method="post" action="/anket">
            <label for="ad">Ad:</label><br>
            <input type="text" id="ad" name="ad" required style="width: 100%; padding: 5px; margin-bottom: 15px;"><br>
            
            <label for="soyad">Soyad:</label><br>
            <input type="text" id="soyad" name="soyad" required style="width: 100%; padding: 5px; margin-bottom: 15px;"><br>
    '''

    for siyahi, elementler in siyahilar.items():
        form_html += f'<label for="{siyahi}">{siyahi}:</label><br>'
        form_html += f'<select name="{siyahi}" id="{siyahi}" required style="width: 100%; padding: 5px; margin-bottom: 20px;">'
        form_html += '<option value="">Seçin</option>'
        for elem in elementler:
            form_html += f'<option value="{elem}">{elem}</option>'
        form_html += '</select><br>'

    form_html += '''
            <button type="submit" style="background-color: #145214; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">Göndər</button>
        </form>
        <br><a href="/" style="color: white;">Ana səhifəyə qayıt</a>
    </div>
    </body>
    </html>
    '''
    return form_html

@app.route('/netice')
def netice():
    if not neticeler:
        return '''
        <h2>Heç bir cavab yoxdur.</h2>
        <a href="/anket">Ankete başla</a><br>
        <a href="/">Ana səhifə</a>
        '''

    netice_html = '''
    <html>
    <head><title>Anket Nəticələri</title></head>
    <body style="font-family: Arial, sans-serif; max-width: 700px; margin: 50px auto;">
        <h2 style="text-align:center;">Anket Nəticələri✨</h2>
        <table border="1" cellpadding="10" cellspacing="0" style="width: 100%; border-collapse: collapse;">
        <tr>
            <th>Ad Soyad</th>
    '''

    for siyahi in siyahilar:
        netice_html += f"<th>{siyahi}</th><th>{siyahi} Puan🌟</th>"

    netice_html += "<th>Ümumi Puan</th></tr>"

    for cavab in neticeler:
        adsoyad = f"{cavab['ad']} {cavab['soyad']}"
        secimler = cavab['secimler']
        puanlar = [siyahilar[s][secimler[s]] for s in siyahilar]
        cem = sum(puanlar)

        netice_html += f"<tr><td>{adsoyad}</td>"
        for s in siyahilar:
            netice_html += f"<td>{secimler[s]}</td><td>{siyahilar[s][secimler[s]]}</td>"
        netice_html += f"<td><b>{cem}</b></td></tr>"

    netice_html += '''
        </table>
        <br>
        <a href="/anket">Anketə yenidən başla</a> | <a href="/">Ana səhifəyə qayıt</a>
    </body>
    </html>
    '''

    return netice_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
