from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_tax(income, tax_rate):
    if income < 0:
        raise ValueError("Income cannot be negative")
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1")
    return round(income * tax_rate, 2)

@app.route('/tax', methods=['GET'])
def tax():
    try:
        income = float(request.args.get('income'))
        tax_rate = float(request.args.get('rate'))
        tax_amount = calculate_tax(income, tax_rate)
        return jsonify({"tax": tax_amount})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
