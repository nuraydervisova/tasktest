from flask import Flask

app = Flask(__name__)

#Ana seyfe
@app.route('/')
def home():
    return """
<html>
<head><title>API</title></head>
    <h1><em>🧠 API nədir?</em></h1>
    <h2>API HAQQINDA</h2>
    <p>API — Application Programming Interface sözlərinin qısaltmasıdır. Yəni Tətbiq Proqramlaşdırma İnterfeysi deməkdir.
     Bu, iki proqram arasında əlaqə yaratmaq üçün istifadə olunan "qayda və metodlar toplusudur".
     </p>
    <p><strong>🎯 Niyə API istifadə olunur?</strong><br><b>Bir proqram başqa proqramdan məlumat almaq, məlumat göndərmək və ya əmr vermək istəyəndə API vasitəsi ilə bunu edir.<b>Məsələn, hava məlumatı göstərən bir proqram, Meteoroloji xidmətin API-sindən bu məlumatı çəkə bilər.
    </p>

    <p><strong>🔧 API necə işləyir?</strong><br>API əsasən sorğu-cavab (request-response) sistemi ilə işləyir:<br>Sən sorğu göndərirsən: <i>GET /productsaq</i><br>Server cavab verir:<i>[{id: 1, name: "Laptop"}]</i></br></p>
    <strong>🧱 API növləri.<br></strong>
    <ins>1. REST API (ən məşhuru).<br></ins>
    <ins>2.SOAP API. <br></ins>
    <ins>3. GraphQL API. <br></ins>
    <p><strong>📦 API nə üçün istifadə olunur?</strong></p>
    <del>Mobil tətbiqlərin serverlə əlaqə qurması üçün<br>İki fərqli proqramın məlumat mübadiləsi üçün

<br>Ödəniş sistemlərinin (məsələn, PayPal, Stripe) inteqrasiyası üçün<br>Sosial şəbəkə API-ləri ilə (Facebook, Instagram) məlumat əldə etmək üçün</del>

    </p>pip install Flask
    
    <hr>
"""


if __name__ == '__main__':
    app.run(debug=True)
