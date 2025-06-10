from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML-шаблон
HTML_PAGE = """
<!doctype html>
<html>
<head>
    <title>Tax Calculator</title>
</head>
<body>
    <h2>Tax Calculator</h2>
    <form method="post" action="/calculate">
        <label for="income">Income:</label><br>
        <input type="number" step="0.01" name="income" required><br><br>
        <label for="rate">Tax Rate (0-1):</label><br>
        <input type="number" step="0.01" name="rate" min="0" max="1" required><br><br>
        <input type="submit" value="Calculate">
    </form>

    {% if tax is not none %}
        <h3>Tax Amount: {{ tax }}</h3>
    {% elif error %}
        <h3 style="color:red;">Error: {{ error }}</h3>
    {% endif %}
</body>
</html>
"""

def calculate_tax(income, tax_rate):
    if income < 0:
        raise ValueError("Income cannot be negative")
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1")
    return round(income * tax_rate, 2)

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_PAGE, tax=None, error=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        income = float(request.form.get('income'))
        rate = float(request.form.get('rate'))
        tax_amount = calculate_tax(income, rate)
        return render_template_string(HTML_PAGE, tax=tax_amount, error=None)
    except Exception as e:
        return render_template_string(HTML_PAGE, tax=None, error=str(e))

@app.route('/tax', methods=['GET'])
def tax_api():
    try:
        income = float(request.args.get('income'))
        tax_rate = float(request.args.get('rate'))
        tax_amount = calculate_tax(income, tax_rate)
        return jsonify({"tax": tax_amount})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
