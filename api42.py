from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    massage = "" 
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            massage = f"Yeni taskimizdan salamlar {name}!"
        else:
            massage = "Zehmet olmasa adinizi daxil edin!"
    return render_template_string("""
        <form method="POST">
            Adiniz: <input type="text" name="name" /><br><br>
            <input type="submit" value="Gonder" />
        </form>
        <p>{{ message }}</p>
    """, massage=massage)

if __name__ == "__main__":
    app.run(debug=True)
