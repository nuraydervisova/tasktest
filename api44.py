from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def task():
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        color = request.form.get("color", "").strip()
        country = request.form.get("country", "").strip()
        eat = request.form.get("eat", "").strip()
        if name and color and country and eat:
            message = f"Salam {name}! Sizin sevdiyiniz reng {color}, Getmek istediyiniz olke {country} ve sevimli yemeyiniz {eat} - dir cox gozel secimlerdir!"
        else:
            message = "Zeh,et olmasa bosluqlari doldurun eks halda cavablari gore bilmeyeceksiniz!"
    return render_template_string("""
        <form method="POST">
            Adizin: <input type="text" name="name" /><br><br>
            Sevdiyiniz reng: <input type="text" name="color" /><br><br>
            Getmek istediyiniz olke: <input type="text" name="country" /><br><br>
            Sevimli yemek: <input type="text" name="eat" /><br><br>
            <input type="submit" value="Cavablari gor" />
        </form>
        <p>{{ message }}</p>
""", message=message)

if __name__ == "__main__":
    app.run(debug=True)
