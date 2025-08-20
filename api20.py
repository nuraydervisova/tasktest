from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Sual: Python-un yaradıcılarından biri kimdir?<br><br>
        <input type="text" name="answer" /><br><br>
        <input type="submit" value="Cavabı göndər" />
    </form>
'''

correct_answer = "guido van rossum"

@app.route('/', methods=['GET', 'POST'])
def quiz():
    message = ''
    if request.method == 'POST':
        answer = request.form.get('answer', '').strip().lower()

        if not answer:
            message = "Zəhmət olmasa cavabı daxil edin."
        elif answer == correct_answer:
            message = "Təbriklər! Cavabınız doğrudur."
        else:
            message = "Təəssüf, cavab səhvdir. Yenidən cəhd edin."

    return render_template_string(f'''
        <h2>Sadə Quiz</h2>
        {html_form}
        <p>{message}</p>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
