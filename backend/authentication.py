from flask import Flask, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sys

app = Flask(__name__)
SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
app.secret_key = SECRET_KEY

# Exemple de stockage des experts
experts = [
    {'email': 'expert1@example.com', 'password': generate_password_hash('password1')},
    {'email': 'expert2@example.com', 'password': generate_password_hash('password2')}
]

# Route pour la connexion de l'expert
@app.route('/api/expert/login', methods=['POST'])
def expert_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    print('Hello world!', file=sys.stderr)
    expert = next((expert for expert in experts if expert['email'] == email), None)
    print("password")
    if expert and check_password_hash(expert['password'], password):
        # Stocker les informations de l'expert dans la session
        session['expert'] = email
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

# Route pour la déconnexion de l'expert
@app.route('/api/expert/logout', methods=['GET'])
def expert_logout():
    # Effacer les informations de l'expert de la session
    session.pop('expert', None)
    return jsonify({'message': 'Logged out successfully'}), 200

# Route pour vérifier l'état de connexion de l'expert
@app.route('/api/expert/status', methods=['GET'])
def expert_status():
    if 'expert' in session:
        return jsonify({'logged_in': True, 'expert_email': session['expert']}), 200
    else:
        return jsonify({'logged_in': False}), 200

if __name__ == '__main__':
    app.run(debug=True)
