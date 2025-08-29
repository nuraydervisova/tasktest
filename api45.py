from flask import Flask, request, render_template_string

app = Flask(__name__)

html_form = """
    <form method="POST">
        Yasinizi daxil edin: <input type="number" name="age" /><br><br>
        <input type="submit" value="Gonder">
    </form> 
"""

@app.route("/", methods=["GET", "POST"])
def check_age():
    message = ""
    if request.method == "POST":
        age = request.form.get("age", type=int)
        if age is None:
            message = "Zehmet olmasa yas daxil edin!"
        elif age < 0:
            message = "Yas menfi ola bilmez."
        elif age <= 5:
            message = "Bilet: odenissizdir."
        elif age <= 17:
            message = "Bilet qiymeti: 5-manat."
        elif age <= 64:
            message = "Bilet qiymeti: 10 manat."
        else:
            message = "Bilet qiymeti: 7 manat."

    return render_template_string(f"""
    <h2> Yas uzre bilet qiymeti</h2>
    {html_form}
    <p>{message}</p>
""", message=message)

if __name__ == "__main__":
    app.run(debug=True)
