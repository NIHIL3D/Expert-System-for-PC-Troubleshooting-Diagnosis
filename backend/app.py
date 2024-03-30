from flask import Flask, request, jsonify, session, redirect, url_for
from itertools import combinations, permutations
from pyswip import Prolog
from werkzeug.security import generate_password_hash, check_password_hash


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

# Route pour récupérer l'email de l'expert connecté
@app.route('/api/expert/email', methods=['GET'])
def get_expert_email():
    if 'expert' in session:
        expert_email = session['expert']
        return jsonify({'expert_email': expert_email}), 200
    else:
        return jsonify({'error': 'Expert not logged in'}), 401

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



# Define the list of symptoms

f = open("symptoms.txt", "r")

symptoms = list(f.read().split("\n"))

# Initialize Prolog
prolog = Prolog()
prolog.consult("diagnosis.pl")

# Define the find_faulty_issues function
def find_faulty_issues(symptoms):
    # Initialize an empty list to store the faulty issues
    faulty_issues = []

    # Initialize the longest combination of symptoms
    longest_combination = [0]

    while symptoms and longest_combination:
        longest_combination = []
        # Iterate over each symptom subset
        for i in range(1, len(symptoms) + 1):
            for symptom_subset in combinations(symptoms, i):
                for symptom_permutation in permutations(symptom_subset):
                    # Try to diagnose the current symptom subset
                    diagnosis_query = "diagnose_issues([{}], Issues)".format(','.join(["'{}'".format(symptom) for symptom in symptom_permutation]))
                    issues = list(prolog.query(diagnosis_query))

                    # If there are diagnosed issues, update the longest combination and the faulty issues
                    if issues[0]['Issues']:
                        if len(symptom_permutation) >= len(longest_combination):
                            longest_combination = list(symptom_permutation)

        # Construct the query string for Prolog
        prolog_list = "[" + ", ".join(["'{}'".format(symptom) for symptom in longest_combination]) + "]"
        issues = list(prolog.query("diagnose_issues({}, Issues)".format(prolog_list)))
        faulty_issues += issues[0]['Issues']
        
        # Remove the symptoms in the longest combination from the symptom list
        for item in longest_combination:
            if item in symptoms:
                symptoms.remove(item)
        
    return faulty_issues

# Endpoint to get the list of symptoms
@app.route('/api/symptoms', methods=['GET'])
def get_symptoms():
    return jsonify({'symptoms': symptoms})

@app.route('/api/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    symptoms = data.get('symptoms', [])
    print(symptoms)
    faulty_issues = find_faulty_issues(symptoms)
    return jsonify({'faulty_issues': faulty_issues})

@app.route('/api/add-symptom', methods=['POST'])
def add_symptom():
    data = request.json
    issue = data.get('issue', '')
    issue += "_symptoms"
    symptom = data.get('symptom', '')
    if issue and symptom:
        # Add symptom to the corresponding issue
        print("issue: ", issue)
        print("symptom: ", symptom)
        add_or_create_fault(symptom, issue)
        return jsonify({'message': 'Symptom added successfully'})
    else:
        return jsonify({'error': 'Invalid data'})

def add_or_create_fault(symptoms, fault_predicate):
    done = False
    filename = "diagnosis.pl"
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            if fault_predicate in line and not done:
                line = line.rstrip()[:-3] + ", " + symptoms + "]).\n"
                done = True
            file.write(line)
    if not done:
        with open(filename, "w") as file:
            for line in lines:
                if "Define symptoms associated with each issue" in line:
                    line = line + f"\n{fault_predicate}([" + symptoms +"]).\n"
                if "Define dynamic predicates for symptoms" in line:
                    line = line + "\n:- dynamic {}/1.\n".format(fault_predicate)
                fault_predicateW = fault_predicate[:-9]
                if "Rules for diagnosing issues based on symptoms" in line:
                    line = line + f"""\ndiagnose_issue(Symptoms, {fault_predicateW}) :-
    {fault_predicate}(Symptoms).\n""".format(fault_predicate)
                    done = True
                file.write(line)
    with open("symptoms.txt", "a") as file:
        for i in symptoms.split(", "):
            file.write(f"\n{i}")



if __name__ == '__main__':
    app.run(debug=True)
