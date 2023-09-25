from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/deduct', methods=['POST'])
def deduct_amount():
    # Get the amount from the request
    try:
        data = request.get_json()
        amount = float(data['amount'])
    except:
        return jsonify({"error": "Invalid or missing 'amount' in the request data."}), 400
    
    deductions = []
    
    # Deduct $10 increments and add them to the deductions list
    while amount >= 10:
        deductions.append("$10")
        amount -= 10
    
    # Return the deductions and the remaining amount
    return jsonify({
        "deductions": deductions,
        "remaining_amount": f"${amount:.2f}"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
