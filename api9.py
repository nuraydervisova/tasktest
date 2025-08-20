from flask import Flask

app = Flask(__name__)

# Ana səhifə
@app.route('/')
def index():
    return '''
        <h1>Salam! Bu mənim sadə Flask saytımdır.</h1>
        <p>Bu ana səhifədir.</p>
        <a href="/haqqinda">➡️ Haqqında səhifəsinə keç</a>
    '''

# Haqqında səhifəsi
@app.route('/haqqinda')
def about():
    return '''
        <h1>Haqqımızda</h1>
        <p>Bu sayt Flask öyrənmək üçündür.</p>
        <a href="/">⬅️ Ana səhifəyə qayıt</a>
    '''
# Serveri işə salırıq
if __name__ == '__main__':
    app.run(debug=True)
