from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Adınız: <input type="text" name="name" /><br><br>
        Yaşınız: <input type="number" name="age" /><br><br>
        <input type="submit" value="Göndər" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def check_user():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', type=int)

        if not name:
            message = 'Zəhmət olmasa adınızı daxil edin!'
        elif age is None:
            message = 'Zəhmət olmasa yaşınızı daxil edin!'
        elif age < 18:
            message = f'Salam, {name}! Siz gəncsiniz.'
        else:
            message = f'Salam, {name}! Siz artıq böyüksünüz.'

    return render_template_string(f'''
        <h2>İstifadəçi Məlumatı</h2>
        {html_form}
        <p>{message}</p>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
