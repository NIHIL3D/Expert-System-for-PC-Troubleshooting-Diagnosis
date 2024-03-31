# Expert-System-for-PC-Troubleshooting-Diagnosis
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Expert System Logic in diagnosis.pl](#expert-system-logic)
- [PySwip](#pyswip)
- [Images](#images)
## Introduction
The Expert System for PC Troubleshooting Diagnosis aims to provide users with a convenient tool for identifying potential issues with their computer systems based on reported symptoms. By leveraging Prolog's rule-based logic, the system can effectively diagnose various hardware and software problems, offering valuable insights for troubleshooting and resolution.
## Features
- User-friendly web interface for symptom input and issue diagnosis
- Support for both client-side and expert-side interactions
- Dynamic addition of new symptoms and issues for continuous system improvement
- Secure authentication for expert login
- Persistent storage of expert and diagnostic data
## Technologies Used
- Flask for the backend server
- Prolog (Logic programming language)
- React for the frontend interface
- PySwip: Python interface to SWI-Prolog providing a Prolog engine embeddable in Python.
- Werkzeug: A comprehensive WSGI web application library for Python.
## Setup
1. Clone the repository:
  ```
  git clone https://github.com/NIHIL3D/Expert-System-for-PC-Troubleshooting-Diagnosis.git
  ```
2. Navigate to the project directory:
  ```
  cd Expert-System-for-PC-Troubleshooting-Diagnosis
  ```
3. Install dependencies for the frontend and backend:
  ```
  cd frontend
  npm install
  cd ../backend
  pip install -r requirements.txt
  ```
4. Start the Flask server:
  ```
  python app.py
  ```
5. Start the React development server:
  ```
  cd ../frontend
  npm start
  ```
- Open your browser and go to http://localhost:3000 to access the application.
6. Expert creds:
  ```
    {email: 'expert1@example.com', password: 'password1'},
    {email: 'expert2@example.com', password: 'password2'}
  ```
## Usage
- Client Side:
  - Visit the homepage and choose your role as a client.
  - Select symptoms from the checklist and click "Diagnose Issues" to identify potential problems with your PC.
  
- Expert Side:
  - Log in as an expert to access additional functionalities.
  - Add new symptoms and associated issues to improve the diagnosis capabilities.

## Expert System Logic
The diagnosis.pl file plays a crucial role in implementing the expert system logic for diagnosing PC issues based on the symptoms provided. Here's how it works:

### 1. Rule Definition
  The file defines rules that map symptoms to potential faulty issues. For each type of issue, there are associated symptoms that help identify it.
### 2. Dynamic Predicate Initialization
  Dynamic predicates are initialized for each type of issue and its associated symptoms. This allows for the addition of new issues and symptoms dynamically during runtime.
### 3. Diagnosis Rules
  The rules define how to diagnose issues based on the symptoms provided. For example:
  ```prolog
  diagnose_issue(Symptoms, faulty_graphics_card) :-
    faulty_graphics_card_symptoms(Symptoms).
  ```
  This rule states that if the provided symptoms match those associated with a faulty graphics card, then the issue is diagnosed as a faulty graphics card.
### 4. Diagnosing Issues
  - The main predicate diagnose_issues/2 takes a list of symptoms as input and returns a list of diagnosed issues.
  - It iterates through the symptoms and attempts to match them with known issues based on the defined rules.
  - If a match is found, the corresponding issue is added to the list of diagnosed issues.
### 5. Prolog Consultation
  Prolog is consulted to utilize its inference engine, allowing for efficient pattern matching and rule-based reasoning.

## PySwip
PySwip is a Python library that enables bidirectional communication between Python and Prolog, allowing seamless integration of Prolog's logic programming capabilities into Python applications. In the context of the Expert System for PC Troubleshooting Diagnosis, PySwip plays a vital role:
- Logic-Based Reasoning: PySwip facilitates the execution of Prolog queries within Python, enabling the system to leverage Prolog's logic-based reasoning for diagnosing PC hardware and software issues based on observed symptoms.
- Rule-Based Inference: Prolog rules defined in diagnosis.pl encode relationships between symptoms and faulty components, allowing the system to infer potential issues by matching observed symptoms against these rules.
- Interoperability: PySwip enables seamless integration of Prolog's rule-based reasoning into the Python-based web application, providing a flexible and extensible framework for diagnosing a wide range of PC issues.
- Flexible Knowledge Representation: Using PySwip, the system represents the knowledge base of PC issues in Prolog's declarative syntax, enabling developers to define predicates and rules that capture complex relationships between symptoms and faults.


## Images

![Screenshot_782](https://github.com/NIHIL3D/Expert-System-for-PC-Troubleshooting-Diagnosis/assets/117014237/ab4d5603-f417-432a-b75e-01ff61a8675f)


![Screenshot_783](https://github.com/NIHIL3D/Expert-System-for-PC-Troubleshooting-Diagnosis/assets/117014237/8ac7f166-057c-4436-ae4d-67c4bb63e855)


![Screenshot_786](https://github.com/NIHIL3D/Expert-System-for-PC-Troubleshooting-Diagnosis/assets/117014237/b7f6ae31-dab2-48b5-bab5-a6c7c7553a25)


![Screenshot_785](https://github.com/NIHIL3D/Expert-System-for-PC-Troubleshooting-Diagnosis/assets/117014237/bb4ac5d1-b9c0-46b1-b11c-b75f5c47f34a)



