from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Birinci ədəd: <input type="number" name="num1" /><br><br>
        İkinci ədəd: <input type="number" name="num2" /><br><br>
        <input type="submit" value="Topla" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def add():
    result = ''
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')

        if not num1 or not num2:
            result = 'Zəhmət olmasa iki ədəd daxil edin.'
        else:
            try:
                toplam = float(num1) + float(num2)
                result = f'Nəticə: {toplam}'
            except ValueError:
                result = 'Zəhmət olmasa düzgün ədəd daxil edin.'

    return render_template_string(f'''
        <h2>Sadə Toplama Kalkulyatoru</h2>
        {html_form}
        <p>{result}</p>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
