from flask import Flask, request, render_template_string

app = Flask(__name__)


html_form = '''
<form method='POST'>
    Birinci ədəd: <input type="number" step="any" name="num1" /><br><br>
    İkinci ədəd: <input type="number" step="any" name="num2" /><br><br>
    Əməliyyat:<br>
    <input type="radio" name="operation" value="add" />Toplama<br>
    <input type="radio" name="operation" value="subtract" />Çıxma<br>
    <input type="radio" name="operation" value="multiply" />Vurma<br>
    <input type="radio" name="operation" value="divide" />Bölmə<br><br>
    <input type="submit" value="Hesabla" />
</form>
'''
@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        try:
            num1 = float(request.form.get ("num1", " "))
            num2 = float(request.form.get("num2", " "))
        except ValueError:
            result = "Zəhmət olmasa düzgün ədədlər daxil edin!"
            return render_template_string(html_form + f'<p>{result}</p>')
    
        operation = request.form.get("operation")
        if not operation:
            result = "Zəhmət olmasa əməliyyat seçin!"
        else:
            if operation == "add":
                res = num1 + num2
                result = f"Nəticə: {res}"
            elif operation == "subtract":
                res = num1 - num2
                result = f"Nəticə: {res}"
            elif operation == "multiply":
                res = num1 * num2
                result = f"Nəticə: {res}"
            elif operation == "divide":
                if num2 == 0:
                    result = "Sıfıra bölmək olmaz!"
                else:
                    res = num1 / num2
                    result = f"Nəticə: {res}"
    return render_template_string(html_form + f"<p>{result}</p>")

if __name__=='__main__':
    app.run(debug=True)
