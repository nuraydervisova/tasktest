from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Mətninizi daxil edin:<br>
        <textarea name="text" rows="5" cols="40">{{ text }}</textarea><br><br>
        <input type="submit" value="Hesabla" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def text_stats():
    result = ''
    text = ''

    if request.method == 'POST':
        text = request.form.get('text', '').strip()

        if not text:
            result = "Zəhmət olmasa mətn daxil edin."
        else:
            char_count = len(text)
            word_count = len(text.split())
            result = f"Mətnin uzunluğu: {char_count} simvol<br>Söz sayı: {word_count}"

    return render_template_string('''
        <h2>Mətn Statistikası</h2>
        ''' + html_form + '''
        <p><b>{{ result|safe }}</b></p>
    ''', text=text, result=result)

if __name__ == '__main__':
    app.run(debug=True)
