from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Aylıq gəlirinizi daxil edin (AZN): <input type="number" step="any" name="income" value="{{ income }}" /><br><br>
        <input type="submit" value="Hesabla" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def tax_calculator():
    result = ''
    income = ''

    if request.method == 'POST':
        income = request.form.get('income', '')
        if not income:
            result = 'Zəhmət olmasa aylıq gəlirinizi daxil edin.'
        else:
            try:
                inc = float(income)
                if inc <= 0:
                    result = 'Düzgün gəlir daxil edin.'
                elif inc <= 1000:
                    tax_rate = 0.10
                elif inc <= 3000:
                    tax_rate = 0.15
                elif inc <= 6000:
                    tax_rate = 0.20
                else:
                    tax_rate = 0.25

                if inc > 0:
                    tax = inc * tax_rate
                    net_income = inc - tax
                    result = (
                        f'Gəlir: {inc:.2f} AZN<br>'
                        f'Vergi dərəcəsi: {tax_rate*100:.0f}%<br>'
                        f'Ödəniləcək vergi: {tax:.2f} AZN<br>'
                        f'Əldə qalacaq məbləğ: {net_income:.2f} AZN'
                    )
            except ValueError:
                result = 'Zəhmət olmasa düzgün ədəd daxil edin.'

    return render_template_string('''
        <h2>Şəxsi Gəlir Vergisi Kalkulyatoru</h2>
        ''' + html_form + '''
        <p><b>{{ result|safe }}</b></p>
    ''', income=income, result=result)

if __name__ == '__main__':
    app.run(debug=True)
