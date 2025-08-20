from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Birinci ədəd: <input type="number" step="any" name="num1" value="{{num1}}" /><br><br>
        İkinci ədəd: <input type="number" step="any" name="num2" value="{{num2}}" /><br><br>
        Əməliyyat:
        <select name="operation">
            <option value="add" {% if operation == 'add' %}selected{% endif %}>Toplama</option>
            <option value="subtract" {% if operation == 'subtract' %}selected{% endif %}>Çıxma</option>
        </select><br><br>
        <input type="submit" value="Hesabla" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def my_calculate():
    result = ''
    num1 = ''
    num2 = ''
    operation = 'add'

    if request.method == "POST":
        num1 = request.form.get('num1', '')
        num2 = request.form.get('num2', '')
        operation = request.form.get('operation', "add")

        if not num1 or not num2:
            result = 'Zəhmət olmasa iki ədəd daxil edin.'
        else:
            try:
                n1 = float(num1)
                n2 = float(num2)
                if operation == "add":
                    toplam = n1 + n2
                    result = f"Nəticə: {toplam}"
                elif operation == 'subtract':
                    ferq = n1 - n2
                    result = f'Nəticə: {ferq}'
                else:
                    result = 'Qeyri-müəyyən əməliyyat seçildi.'
            except ValueError:
                result = 'Zəhmət olmasa düzgün ədəd daxil edin.'

    return render_template_string('''
        <h2>Sadə Kalkulyator</h2>
        ''' + html_form + '''
        <p><b>{{ result }}</b></p>
    ''', num1=num1, num2=num2, operation=operation, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
