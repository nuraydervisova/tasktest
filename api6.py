from flask import Flask

app = Flask(__name__)

@app.route('/')
def sayt_x():
    return '''
<html>
<head><title>Yeni sayt</title></head>
<body>
       <h1>🌐  HTML Sayt Yaratmaq üçün</h1>
    <p>
    <b>1. Fayl yarat:</b><br>
    <i>Kompüterində "Notepad" (və ya digər mətn redaktoru) aç.<br>Faylı <mark>index.html</mark> adı ilə yadda saxla.</i><br>
    <b>2. Faylin kodunu  yaz:</b><br>
    <strong>🧠 KODLARIN MƏNASI:</strong><br>
    <em>"!DOCTYPE html"</em>--------------Səhifənin HTML5 olduğunu göstərir.<br>
    <em>"html lang="az"</em>"---------------Səhifənin əsas dilinin azərbaycan dili olduğunu bildirir.<br>
    <em>"head"</em>---------------------Brauzerə görünməyən məlumatlar (title, charset və s.) yerləşir.<br>
    <em>"meta charset="UTF-8""</em>--------------Yazı simvollarının düzgün görünməsi üçün kodlaşdırma.<br>
    <em>"title"</em>------------------Brauzerin başlığında görünən səhifə adı.<br>
    <em>"body"</em>--------------------İstifadəçiyə görünən əsas məzmun bu hissədə olur.<br>
    <em>"h1"</em>-------------------Ən böyük başlıq.<br>
    <em>"p"</em>---------------------Paraqraf (mətn hissəsi).<br>
    <b.3. Nəticə</b>
    <i>Bu faylı <mark>.html</mark> kimi saxladıqdan sonra brauzerdə açsan, sayt işləyəcək.</i>
    </p>
    <h2>📋 Siyahılar</h2>
    <p>
    <ul>
        <li>1-Nizamsuz siyahi    <b>ul</b></li>
        <li>2-Nizamlı siyahı (sıralı — 1,2,3...)     <b>ol</b></li>
        <li>3-Siyahı elementi (həm <b>ul</b>, həm də <b>ol</b> içində)  li</li>
    </ul>
    
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
