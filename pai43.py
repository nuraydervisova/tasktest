from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = "" 
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        surname = request.form.get("surname", "").strip()
        if name and surname:
            message = f"salam yeniden xos geldin {name} {surname}!"
        else:
            message = "Zehmet olmasa adinizi daxil edin!"

    return render_template_string("""
        <form method="POST">
            Adiniz: <input type="text" name="name"  /><br><br>
            Soyadiniz: <input type="text" name="surname" /><br><br>
            <input type="submit" value="Gonder" />
        </form>
        <p>{{ message }}</p>
""", message=message)


if __name__ == "__main__":
    app.run(debug=True)
