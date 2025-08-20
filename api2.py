from flask import Flask

app = Flask(__name__)

# Ana səhifə
@app.route("/")
def home():
    return """
    <html>
    <head><title>Ana Səhifə</title></head>
    <body style="text-align: center; font-family: Arial;">
        <h1 style="color: purple;">🌐 Mənim Saytım</h1>
        <p style="color: gray;">Bu, sadə 3 səhifəli bir Flask tətbiqidir.</p>
        <a href="/result" style="background-color: green; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Result API səhifəsinə keç</a><br><br>
        <a href="/restful" style= color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">RESTful API səhifəsinə keç</a>
    </body>
    </html>
    """

# Result API səhifəsi
@app.route("/result")
def result():
    return """
    <html>
    <head><title>Result API</title></head>
    <body style="text-align: center; font-family: Arial;">
        <h2 style="color: blue;">🔍 Result API Nədir?</h2>
        <p>Bu səhifədə Result API haqqında kiçik məlumat verilir. Sadə və öyrədici!</p>
        <a href="/" style="margin-right: 20px;">⬅ Ana Səhifəyə Qayıt</a>
        <a href="/restful">➡ Növbəti Səhifə</a>
    </body>
    </html>
    """

# RESTful API səhifəsi
@app.route("/restful")
def restful():
    return """
    <html>
    <head><title>RESTful API</title></head>
    <body style="text-align: center; font-family: Arial;">
        <h2 style="color: darkred;">🧩 RESTful API nədir?</h2>
        <p>RESTful API — müasir veb sistemlərdə istifadə olunan məlumat mübadilə üsuludur.</p>
        <a href="/">⬅ Ana Səhifəyə Qayıt</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
