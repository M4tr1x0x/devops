from flask import Flask, jsonify
app = Flask(__name__)

# Simulamos una base de datos de cuentas
accounts = {"user1": {"balance": 1000}}

@app.route('/account/<username>', methods=['GET'])
def get_account(username):
    if username in accounts:
        return jsonify(accounts[username]), 200
    else:
        return jsonify({"message": "Account not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
