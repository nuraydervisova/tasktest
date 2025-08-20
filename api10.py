from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
    <head><title>Task8</title></head>
    <body>
        <h1><strong>Xos gelmisiz! Bu menim yeni lahiyemdir task8.</strong></h1>
         <h2>Ahtapotlar☺️</h2>
        <p>
        <i> Ahtapotlar dəniz canlılarıdır və çox ağıllı heyvanlar sayılırlar. Onların 8 qolu var və hər qolunda öz sinir sistemi mövcuddur.</i><br>
        <i>Ahtapotlar rəng dəyişdirə, gizlənə və çox dar yerlərdən keçə bilirlər. Onların beyinləri çox inkişaf etmişdir.</i><br>
        </p>
        <hr>
                    <ul>
                        <li>Ahtapotların 3 ürəyi var</li>
                        <li>Onlar mürəkkəb ifraz edərək düşməndən qaça bilərlər</li>
                        <li>Çox elastik bədən quruluşuna malikdirlər</li>
                    </ul>

                
              <h3>🐙 Ahtapotlar haqqında maraqlı faktlar</h3>
        <p>
        <b>🔹 3 ürəkləri var</b><br>
            İki ürək qanı solungaçlara göndərir.<br>Üçüncü ürək isə qanı bədənin digər hissələrinə ötürür.<br>Maraqlısı odur ki, ahtapot üzərkən bu üçüncü ürək dayanır – ona görə də çox üzməyi sevmirlər, enerjiyə qənaət edirlər!<br>
        <b>🔹 Mavi qanları var</b><br>
            İnsanlarda hemoqlobin dəmir əsaslıdır və qanımız qırmızıdır.<br>Ahtapotlarda isə hemosiyanin var – bu mis əsaslıdır və qanları mavidir.Bu, onların soyuq və oksigeni az olan sularda yaşamasına imkan verir.<br>
        <b>🔹 İnanılmaz sinir sistemi var</b><br>
            Onların beyni yalnız başlarında deyil – 8 qolunun hər birində də minlərlə sinir hüceyrəsi var.<br>Bu o deməkdir ki, qollar müstəqil şəkildə hərəkət edə və hətta "düşünə" bilir!<br>
        <b>🔹 Ağıllı və problem həll edən canlılardır</<b><br>
            Labirintləri keçə bilir, qapaqlı qabları aça bilir, hətta alətlərdən istifadə etdikləri müşahidə olunub!

        </p>

        
               <h4> ✅ Ahtapotlar haqqında Cədvəl üçün Məlumatlar</h4>
            <table border="1" cellpadding="10" cellspacing="0">
                <thead>
                    <tr>
                        <th>Xüsusiyyət</th>
                        <th>Məlumat</th>
                    </tr>
                </thead>
            <tbody>
                <tr>
                    <td>Elmi adi</td>
                    <td><i>Octopus vulgaris</i></td>
                </tr>
                <tr>
                    <td>Ətraflarının sayı</td>
                    <td>8 qol</td>
                </tr>
                <tr>
                    <td>Ürək sayı</td>
                    <td>3 ədəd (2-si qanı qəlsəməyə, 1-i bədənə vurur)</td>
                </tr>
                <tr>
                    <td>Qan rəngi</td>
                    <td>Göy (hemosiyanin tərkibli)</td>
                </tr>
                <tr>
                    <td>Zəkası</td>
                    <td>Çox inkişaf etmişdir, problem həll edə və labirintdən keçə bilir</td>
                </tr>
                <tr>
                    <td>Müdafiə mexanizmi</td>
                    <td>Mürəkkəb ifrazı, rəng dəyişdirmə, kamuflyaj</td>
                </tr>
                <tr>
                    <td>Ömür müddəti</td>
                </tr>
                <tr>
                    <td>Yaşayış mühiti</td>
                    <td>Dəniz və okeanların dibi, mağara və qayalıqlar</td>
                </tr>
                <tr>
                    <td>Qidalanma</td>
                    <td>Balıqlar, xərçəngkimilər, molyusklar</td>
                </tr>
                <tr>
                    <td>Bədən quruluşu</td>
                    <td>Yumşaq, sümüksüz, elastik bədən</td>
                </tr>
                <tr>
                    <td>Təhlükə anında davranış</td>
                    <td>Qollarını qoparıb qaça bilər, yenidən böyüyür</td>
                <tr>
            </tbody>
         <table>

    <body>
<html>
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
