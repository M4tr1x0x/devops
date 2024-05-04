from flask import Flask, request, jsonify
app = Flask(__name__)

# Simulamos una base de datos de usuarios
users = {"user1": "password1"}

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    if username in users and users[username] == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
