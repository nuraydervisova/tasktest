from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Adınız: <input type="text" name="name" /><br><br>

        Cinsiniz:<br>
        <input type="radio" name="gender" value="Kişi" /> Kişi<br>
        <input type="radio" name="gender" value="Qadın" /> Qadın<br><br>

        Hobbiləriniz:<br>
        <input type="checkbox" name="hobby" value="Kitab oxumaq" /> Kitab oxumaq<br>
        <input type="checkbox" name="hobby" value="Musiqi dinləmək" /> Musiqi dinləmək<br>
        <input type="checkbox" name="hobby" value="İdman" /> İdman<br><br>

        Sevdiyiniz texnologiya:
        <select name="tech">
            <option value="Python">Python</option>
            <option value="JavaScript">JavaScript</option>
            <option value="HTML/CSS">HTML/CSS</option>
        </select><br><br>

        <input type="submit" value="Profil Yarat" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def user_profile():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        gender = request.form.get('gender')
        hobby = request.form.getlist('hobby')  # Çox seçim üçün getlist istifadə olunur
        tech = request.form.get('tech')

        if not name or not gender or not tech:
            message = 'Zəhmət olmasa bütün sahələri doldurun!'
        else:
            hobbies = ', '.join(hobby) if hobby else "hobbi seçilməyib"
            message = f'''
                <strong>Profiliniz:</strong><br>
                Ad: {name}<br>
                Cins: {gender}<br>
                Hobbilər: {hobbies}<br>
                Sevdiyiniz texnologiya: {tech}<br>
                <br><em>Çox sağ olun, {name}!</em>
            '''

    return render_template_string(f'''
        <h2>Sənin Profilin</h2>
        {html_form}
        <p>{message}</p>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
