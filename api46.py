from flask import Flask, request, render_template_string

app = Flask(__name__)


question = [
    {
        "question": "1.Python nedir?",
        "name": "q1",
        "answer": "Proqramlasdirma dili."
    },
    {
        "question": "2.  Süni zəkanın ən erkən formalarından biri hansıdır?",
        "name": "q2",
        "answer": "eliza"
    },
    {
        "question" : "3.OpenAI tərəfindən yaradılmış məşhur dil modeli hansıdır?",
        "name" : "q3",
        "answer" : "chatgpt"
    },
    {
        "question": "4. HTML nə üçün istifadə olunur?",
        "name": "q4",
        "answer": "veb səhifə qurmaq"
    },
    {
        "question": "5. Proqramlaşdırmada “loop” nədir?",
        "name": "q5",
        "answer": "döngü"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    result = ""
    correct_count = 0


    if request.method == "POST":
        for q in question:
            user_answer = request.form.get(q["name"], "").strip().lower()
            if user_answer ==q["answer"]:
                correct_count += 1

        result = f"<strong>Netice: </strong> {correct_count} / {len(question)} duzhun cavab verdiniz."

    form_html = '<form method="POST" >'
    for q in question:
        form_html += f"<p>{q['question']}<br><input type='text' name='{q['name']}' /></p>"
    form_html += '<input type="submit" value="Gonder" /></form>'

    return render_template_string(f"""
        <h2> Sualdan Ibaret  quiz</h2>
        {form_html}
        <p>{result}</p>
""")

if __name__ == '__main__':
    app.run(debug=True)
