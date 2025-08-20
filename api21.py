from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Günün əhvalını seçin:<br>
        <select name="mood">
            <option value="">Seçin</option>
            <option value="Xoşbəxt">Xoşbəxt</option>
            <option value="Kədərli">Kədərli</option>
            <option value="Həyəcanlı">Həyəcanlı</option>
            <option value="Sakit">Sakit</option>
        </select><br><br>

        Əlavə şərh:<br>
        <textarea name="comment" rows="4" cols="40" placeholder="İstəsəniz əlavə yazın..."></textarea><br><br>

        <input type="submit" value="Göndər" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def mood_tracker():
    message = ''
    if request.method == 'POST':
        mood = request.form.get('mood')
        comment = request.form.get('comment', '').strip()

        if not mood:
            message = "Zəhmət olmasa əhvalınızı seçin."
        else:
            message = f"Günün əhvalı: <strong>{mood}</strong><br>"
            if comment:
                message += f"Şərhiniz: {comment}"

    return render_template_string(f'''
        <h2>Gündəlik Mood Tracker</h2>
        {html_form}
        <p>{message}</p>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
