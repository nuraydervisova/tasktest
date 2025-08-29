from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            message = f"Salam xos geldin! {name}!"
        else:
            message = "Zehmet olmasa adinzi daxil et!"

    return render_template_string("""
        <form method="POST">
            Adinizi: <input type="text", name="name" /><br><br>
            <input type="submit" value="Gonder" />
        </form>
        <p>{{ message }}</p>
    """, message=message )

if __name__ == "__main__":
    app.run(debug=True)
