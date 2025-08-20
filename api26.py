from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Əsas məbləğ: <input type="number" step="any" name="principal" value="{{principal}}" /><br><br>
        Faiz dərəcəsi (%): <input type="number" step="any" name="rate" value="{{rate}}" /><br><br>
        <input type="submit" value="Hesabla" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def interest_calculator():
    result = ''
    principal = ''
    rate = ''

    if request.method == 'POST':
        principal = request.form.get('principal', '')
        rate = request.form.get('rate', '')

        if not principal or not rate:
            result = 'Zəhmət olmasa əsas məbləği və faiz dərəcəsini daxil edin.'
        else:
            try:
                p = float(principal)
                r = float(rate)
                faiz = p * r / 100
                toplam = p + faiz
                result = f'Faiz məbləği: {faiz:.2f} <br> Ümumi məbləğ: {toplam:.2f}'
            except ValueError:
                result = 'Zəhmət olmasa düzgün ədədlər daxil edin.'

    return render_template_string('''
        <h2>Faiz Kalkulyatoru</h2>
        ''' + html_form + '''
        <p><b>{{ result|safe }}</b></p>
    ''', principal=principal, rate=rate, result=result)

if __name__ == '__main__':
    app.run(debug=True)
