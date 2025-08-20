from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Adınız: <input type="text" name="name" /><br><br>
        Yaşınız: <input type="number" name="age" /><br><br>
        Bildiyiniz proqramlaşdırma dili:
        <select name="language">
            <option value="">Seçin</option>
            <option value="Python">Python</option>
            <option value="JavaScript">JavaScript</option>
            <option value="C++">C++</option>
            <option value="Java">Java</option>
        </select><br><br>
        <input type="submit" value="Göndər" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def profile():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', type=int)
        language = request.form.get('language')

        if not name or not age or not language:
            message = "Zəhmət olmasa bütün sahələri doldurun!"
        else:
            if age < 18:
                age_msg = "Siz gənc proqramçısınız!"
            elif 18 <= age < 50:
                age_msg = "Siz təcrübəli proqramçısınız!"
            else:
                age_msg = "Siz veteran proqramçısınız!"

            message = f"Salam, {name}! {age_msg} Bildiyiniz dil: {language}."

    return render_template_string(f'''
        <h2>Profil Formu</h2>
        {html_form}
        <p>{message}</p>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
