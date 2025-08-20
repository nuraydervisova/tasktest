from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Adınız: <input type="text" name="name" /><br><br>

        Cinsiniz:<br>
        <input type="radio" name="gender" value="Kişi" /> Kişi<br>
        <input type="radio" name="gender" value="Qadın" /> Qadın<br><br>

        Getmək istədiyiniz yerlər:<br>
        <input type="checkbox" name="olke" value="Amerika" /> Amerika<br>
        <input type="checkbox" name="olke" value="İtaliya" /> İtaliya<br>
        <input type="checkbox" name="olke" value="Yaponiya" /> Yaponiya<br>
        <input type="checkbox" name="olke" value="Afrika" /> Afrika<br>
        <input type="checkbox" name="olke" value="Almaniya" /> Almaniya<br>
        <input type="checkbox" name="olke" value="İndoneziya" /> İndoneziya<br>
        <input type="checkbox" name="olke" value="Norveç" /> Norveç<br><br>

        Nəqliyyat vasitəsi:<br>
        <select name="car">
            <option value="Təyyarə">Təyyarə</option>
            <option value="Gəmi">Gəmi</option>
            <option value="Qatar">Qatar</option>
            <option value="Avtobus">Avtobus</option>
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
        olke = request.form.getlist('olke')  # Çox seçim üçün getlist istifadə olunur
        car = request.form.get('car')

        if not name or not gender or not car:
            message = 'Zəhmət olmasa bütün sahələri doldurun!'
        else:
            olkeler = ', '.join(olke) if olke else "yer seçilməyib"
            message = f'''
                <strong>Profiliniz:</strong><br>
                Ad: {name}<br>
                Cins: {gender}<br>
                Getmək istədiyiniz yerlər: {olkeler}<br>
                Nəqliyyat vasitəsi: {car}<br>
                <br><em>Çox sağ olun, {name}!</em>
            '''

    return render_template_string(f'''
        <h2>Sənin Profilin</h2>
        {html_form}
        <p>{message}</p>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
