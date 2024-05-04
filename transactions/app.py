from flask import Flask, request, jsonify
app = Flask(__name__)

# Simulamos una base de datos de transacciones
transactions = []

@app.route('/transaction', methods=['POST'])
def add_transaction():
    transaction = request.json
    transactions.append(transaction)
    return jsonify({"message": "Transaction added"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
