from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = '''
    <form method="POST">
        Sevdiyiniz rəng: <input type="text" name="color" /><br><br>
        Sevdiyiniz heyvan: <input type="text" name="animal" /><br><br>
        <input type="submit" value="Göndər" />
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def favorite_things():
    message = ''
    if request.method == 'POST':
        color = request.form.get('color', '').strip().lower()
        animal = request.form.get('animal', '').strip().lower()

        if not color or not animal:
            message = 'Zəhmət olmasa hər iki sahəni doldurun!'
        else:
            message = f"Sevdiyiniz rəng {color.title()}, sevdiyiniz heyvan isə {animal.title()}dir. Möhtəşəmdir!"

    return render_template_string(f'''
        <h2>Sevdiklərinizi bizə deyin</h2>
        {html_form}
        <p>{message}</p>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
