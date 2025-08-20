from flask import Flask

app = Flask(__name__)

# Ana səhifə
@app.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset+"UTF-8" />
    <title>Tag-larin numunesi</title>
</head>
<body>

    <h1>Bu en boyuk baasliqdir (h1)</h1>
    <h2>Bu kicik baasliqdir (h2)</h2>
    <h3>Bu az daha kicik basliqdir (h3)</h3>
    <p>Bu bir paraqrafdi burda mutelif tag-lardan istifade edeciyik.BU paraqrafi(p) emri ile yaiziriq.</p>
    <p>
    <p>
        Burada <mark>sari fonlu isiqlandirilmis yazi </mark>soz var,
        <small>kicik olcude yazi</small> ve
        <del>ustunden xett cekilmis kicik melumat</del> ,
        <ins>alti xettli yeni elave edilmis yazi</ins>
    </p>

    <p>
       Yeni serte kecmek ucun <br> bu tag istifade olunur. <br>
       Meselen:
       Salam<br>
       Necesen?
   </p>


   <hr>
  

   <p>
      Kimya numunasi: H<sub>2</sub>0 (su moleykulu)<br>
      Riyaziyyat numunesi: X<sup>2</sup> (X-in kvardrati)
   </p>


</body>
</html>
"""
if __name__ == "__main__":
    app.run(debug=True)
