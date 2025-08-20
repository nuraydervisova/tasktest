from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Yaşınızı daxil edin: <input type="number" name="age" value="{{ age }}" /><br><br>
        <input type="submit" value="Yoxla" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def age_category():
    result = ''
    age = ''

    if request.method == 'POST':
        age = request.form.get('age', '')
        if not age:
            result = "Zəhmət olmasa yaşınızı daxil edin."
        else:
            try:
                a = int(age)
                if a < 0:
                    result = "Düzgün yaş daxil edin!"
                elif a <= 12:
                    result = "Kateqoriya: Uşaq"
                elif a <= 17:
                    result = "Kateqoriya: Yeniyetmə"
                elif a <= 64:
                    result = "Kateqoriya: Yetkin"
                else:
                    result = "Kateqoriya: Yaşlı"
            except ValueError:
                result = "Zəhmət olmasa düzgün tam ədəd daxil edin."

    return render_template_string('''
        <h2>Yaş Kateqoriyası Müəyyən Edici</h2>
        ''' + html_form + '''
        <p><b>{{ result }}</b></p>
    ''', age=age, result=result)

if __name__ == '__main__':
    app.run(debug=True)
