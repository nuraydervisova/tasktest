from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Yaşınızı daxil edin: <input type="number" name="age" />
        <input type="submit" value="Yoxla" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def check_age():
    message = ''
    if request.method == 'POST':
        age = request.form.get('age', type=int)
        if age is None:
            message = 'Zəhmət olmasa yaşınızı daxil edin!'
        elif age < 18:
            message = 'Siz gəncsiniz.'
        else:
            message = 'Siz artıq böyüksünüz.'

    return render_template_string(f'''
        <h2>Yaş Yoxlayıcı</h2>
        {html_form}
        <p>{message}</p>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
