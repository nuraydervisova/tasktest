from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
    <head><title>newtask</title></head>
    <body>
    <h1>Yeni layihəmə xoş gəlmisiniz.🙂</h1>
    <h2>Bu layihe kosmos və ulduzlar mövzusundadir.🌌✨</h2>
        <p><strong><i>Kosmos və Ulduzlar Haqqında Əsas Məlumatlar✨</strong></i><br>
        <em>Ulduzlar nədir?</em><br>
            Ulduzlar, nəhəng qaz topalarıdır, əsasən hidrogen və helium qazlarından ibarətdir. Onların nüvəsində gedən nüvə reaksiyaları sayəsində böyük enerji və işıq yayırlar.<br>
        <em>Günəşimiz🌞</em>
            Bizim Günəşimiz Yerə ən yaxın ulduzdur və planet sistemimizin mərkəzində yerləşir. Günəşin enerjisi həyatı mümkün edir.<br>
        <em>Ulduzların növləri🌟</em><br>

            <ul>
                <li><b>Qırmızı cırtdanlar:</b>Kiçik və nisbətən soyuq ulduzlar, uzunömürlüdürlər.</li>
                <li><b>Sarı ulduzlar:</b>Məsələn, bizim Günəş.</li>
                <li><b>Mavi nəhənglər:</b>Böyük və çox isti ulduzlar, ömürləri qısadır.</li>
                <li><b>Nəhayət, qara dəliklər</b>Ulduzlar həyatlarının sonunda partlayıb sıxlaşaraq yaranan, cazibə qüvvəsi o qədər güclüdür ki, işıq belə ondan qaça bilmir.</li>
            </ul>
        <em>Supernova nədir?🚀✨</em>
            Böyük kütləli ulduzların həyatının son mərhələsində baş verən partlayışdır. Bu, çox güclü enerji və işıq yayır, bəzən yeni ulduzların yaranmasına səbəb olur.
        </p>
        <hr>
        <p>
        <strong>Maraqlı Faktlar</strong>
            <ul>
                <li>Ulduzların çoxu bizim Günəşdən qat-qat böyükdür.</li>
                <li>Ulduzlar arasında məsafələr milyonlarla kilometrdən başlayır.</li>
                <li>İşıq sürəti ilə kosmosda səyahət etsək, Günəşdən Yerə işıq 8 dəqiqəyə gəlir.</li>
                <li>Kosmosdakı ulduzların sayı təxminən 100 milyard milyarddır (10^22).</li>
            </ul>

            <a href="/haqqinda">➡️ Haqqında səhifəsinə keç</a>
    </body>
    </html>
"""
@app.route("/haqqinda")
def haqqinda():
    return """
    <h1>Ulduzların Həyat Dövrü🌠</h1>
    <p>
    <em>Ulduzun yaranması</em><br>
      Ulduzlar böyük qaz və toz buludlarından (nebula) yaranır. Qravitasiya qüvvəsi bu buludu sıxışdıraraq nüvəni qızdırır və nüvə reaksiyaları başlayır.<br>
    <em>Əsas ardıcıllıq fazası</em><br>
       Ulduz bu fazada hidrogen nüvələrinin helium nüvələrinə çevrilməsi prosesini davam etdirir. Bu mərhələ ulduzun həyatının ən uzun mərhələsidir.<br>
    <em>Qırmızı nəhəng və ya supernəhəng faza</em><br>
        Hidrogen tükəndikdə, ulduz genişlənir və soyuyur, qırmızı rəng alır. Böyük ulduzlarda supernəhəng mərhələsi yaranır.<br>
    <em>Həyatının sonu</em>
        <ul>
            <li>Kütləli ulduzlar supernova partlayışı ilə həyatlarını bitirirlər və qara dəlik və ya neytron ulduzuna çevrilirlər.</li>
            <li>Daha kiçik ulduzlar isə ağ cırtdan adlanan kiçik, sıx ulduz halına gəlirlər.</li>
        </ul>
    </p>

    <table>
        <thead>
            <tr style="background-color: #4CAF50; color: white;">
                <th>Xüsusiyyət</th>
                <th>Məlumat və İzah</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Ulduzun Yaranması</td>
                <td>Qaz və toz buludlarının sıxılması ilə yaranır</td>
            </tr>
            <tr>
                <td>Əsas Ardıcıllıq</td>
                <td>Hidrogen nüvələrinin helium nüvələrinə çevrildiyi faza</td>
            </tr>
            <tr>
                <td>Qırmızı Nəhəng</td>
                <td>Ulduzun yaşlanmış və genişlənmiş, soyumuş vəziyyəti</td>
            </tr>
                <td>Supernova</td>
                <td>Kütləli ulduzların partlayış mərhələsi</td>
            </tr>
            <tr>  
                <td>Qara Dəlik</td>
                <td>Supernova sonrası çox sıxlaşmış cazibə obyektidir</td>
            </tr>
                <td>İşıq Sürəti</td>
                <td>Saniyədə 299,792 km</td>
            </tr>
            <tr>
                <td>Günəş</td>
                <td>Sarı ulduz, orta ölçüdə, Günəş sistemi mərkəzi</td>
            </tr>
            <tr>
                <td>Betelgeuse</td>
                <td>Qırmızı supernəhəng, Günəşdən 1000 dəfə böyük</td>
            </tr>
            <tr>
                <td>Rigel</td>
                <td>Mavi nəhəng, Günəşdən 70,000 dəfə parlaq</td>
            </tr>
            <tr>
                <td>Proksima Kentavri</td>
                <td>Ən yaxın ulduz sistemi, Yerə 4.24 işıq ili məsafədə</td>
            </tr>
                <td>Günəş Sisteminin Planetləri</td>
                <td>8 planet (Merkuri, Venera, Yer, Mars, Yupiter, Saturn, Uran, Neptun)</td>
            </tr>
        </tbody>
    </table>
    <a href="/">Ana seyfeye kecid</a>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
