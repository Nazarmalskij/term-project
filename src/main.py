from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Tax Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f1f1f1;
            padding: 40px;
        }
        .container {
            max-width: 400px;
            margin: auto;
            background: white;
            padding: 30px 40px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        label {
            font-weight: bold;
        }
        input[type=number], input[type=submit] {
            width: 100%;
            padding: 10px;
            margin: 6px 0 20px 0;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
        }
        input[type=submit] {
            background-color: #4CAF50;
            color: white;
            border: none;
            font-size: 16px;
            cursor: pointer;
        }
        input[type=submit]:hover {
            background-color: #45a049;
        }
        .result {
            text-align: center;
            font-size: 18px;
            color: #333;
        }
        .error {
            color: red;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Tax Calculator</h2>
        <form method="post" action="/calculate">
            <label for="income">Income (USD):</label>
            <input type="number" step="0.01" name="income" required>
            
            <label for="rate">Tax Rate (%):</label>
            <input type="number" step="0.01" name="rate" min="0" max="100" required>
            
            <input type="submit" value="Calculate">
        </form>

        {% if tax is not none %}
            <div class="result">Tax Amount: <strong>{{ tax }} USD</strong></div>
        {% elif error %}
            <div class="error">Error: {{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

def calculate_tax(income, tax_rate_percent):
    if income < 0:
        raise ValueError("Income cannot be negative")
    if not 0 <= tax_rate_percent <= 100:
        raise ValueError("Tax rate must be between 0 and 100 percent  ")
    return round(income * (tax_rate_percent / 100), 2)

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
