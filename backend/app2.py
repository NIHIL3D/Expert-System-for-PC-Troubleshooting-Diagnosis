# from flask import Flask, jsonify, request
# import pickle
# import sys

# app = Flask(__name__)

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.yes = None
#         self.no = None

# # def build_tree():
# #     root = TreeNode("Is your computer turning on?")
# #     root.yes = TreeNode("Is the screen displaying anything?")
# #     root.no = TreeNode("Is the power cable plugged in?")
# #     root.yes.yes = TreeNode("Your computer might have a display issue. Contact support.")
# #     root.yes.no = TreeNode("Is the computer making any unusual noises?")
# #     root.yes.no.yes = TreeNode("Your computer's hardware might be faulty. Contact support.")
# #     root.yes.no.no = TreeNode("Is the monitor cable connected properly?")
# #     root.yes.no.no.yes = TreeNode("Your computer's display cable might be faulty. Try replacing it.")
# #     root.yes.no.no.no = TreeNode("Your monitor might be faulty. Try connecting it to another computer.")
# #     root.no.yes = TreeNode("Is the power outlet working?")
# #     root.no.no = TreeNode("Plug in the power cable and try turning on the computer again.")
# #     root.no.yes.yes = TreeNode("Check the circuit breaker and try a different outlet.")
# #     root.no.yes.no = TreeNode("Contact an electrician to fix the wiring issue.")
# #     return root

# # @app.route("/start", methods=["GET"])
# # def start_diagnosis():
# #     root = build_tree()
# #     print(root.data, file=sys.stderr)
# #     with open("temp", "wb") as f:
# #         pickle.dump(root, f)
# #     # return "Diagnosis started."
# #     return jsonify({"question": root.data})

# # @app.route("/answer/<ans>", methods=["GET"])
# # def answer_question(ans):
# #     with open("temp", "rb") as f:
# #         root = pickle.load(f)
# #     if ans.lower() == "yes":
# #         root = root.yes
# #     elif ans.lower() == "no":
# #         root = root.no
# #     else:
# #         return jsonify({"error": "Invalid answer."})
    
# #     if root.yes is None and root.no is None:
# #         return jsonify({"diagnosis": root.data})
# #     else:
# #         with open("temp", "wb") as f:
# #             pickle.dump(root, f)
# #         return jsonify({"question": root.data})
    
#     # with open("temp", "wb") as f:
#     #     pickle.dump(root, f)
#     #     return jsonify({"question": root.data})
    

# def build_tree():
#     root = TreeNode("Is your computer turning on?")
#     root.yes = TreeNode("Blank screen?")
#     root.no = TreeNode("Is your computer not booting to OS?")
    
#     # Blank screen branch
#     root.yes.yes = TreeNode("Is the power indicator light on?")
#     root.yes.no = TreeNode("Is the monitor power indicator light on?")
    
#     # Sub-branches for blank screen with power indicator on
#     root.yes.yes.yes = TreeNode("Faulty graphics card")
#     root.yes.yes.no = TreeNode("Faulty power supply")
    
#     # Sub-branches for blank screen with monitor power indicator on
#     root.yes.no.yes = TreeNode("Faulty monitor")
#     root.yes.no.no = TreeNode("Loose display cable")
    
#     # Not booting to OS branch
#     root.no.yes = TreeNode("Does the computer display any error messages during startup?")
#     root.no.no = TreeNode("Printer not printing?")
    
#     # Sub-branches for error messages during startup
#     root.no.yes.yes = TreeNode("Corrupted boot loader")
#     root.no.yes.no = TreeNode("Missing boot files")
    
#     # Sub-branches for printer not printing
#     root.no.no.yes = TreeNode("Printer paper jam")
#     root.no.no.no = TreeNode("Printer offline")
    
#     # Additional branches
#     root.yes.yes.yes = TreeNode("Artifacting on screen?")
#     root.yes.yes.yes.yes = TreeNode("Faulty graphics card")
#     root.yes.yes.yes.no = TreeNode("Overheating")
    
#     root.yes.yes.no = TreeNode("Flickering display?")
#     root.yes.yes.no.yes = TreeNode("Faulty graphics card")
#     root.yes.yes.no.no = TreeNode("Loose display cable")
    
#     root.yes.no.yes = TreeNode("No sound?")
#     root.yes.no.yes.yes = TreeNode("Faulty audio card")
#     root.yes.no.yes.no = TreeNode("Faulty speakers")
#     root.yes.no.no = TreeNode("Is the sound muted on the computer?")
#     root.yes.no.no.yes = TreeNode("Mute setting enabled")
#     root.yes.no.no.no = TreeNode("Faulty audio card")
    
#     root.no.yes.yes = TreeNode("Computer freezing?")
#     root.no.yes.yes.yes = TreeNode("Does the freezing occur during specific tasks or randomly?")
#     root.no.yes.yes.yes.yes = TreeNode("Specific tasks: Insufficient memory")
#     root.no.yes.yes.yes.no = TreeNode("Randomly: Faulty hard drive")
#     root.no.yes.yes.yes.yes.yes = TreeNode("Overheating")
#     root.no.yes.yes.yes.yes.no = TreeNode("Insufficient memory")
    
#     root.no.yes.yes.no = TreeNode("Random shutdowns?")
#     root.no.yes.yes.no.yes = TreeNode("Does the shutdown happen immediately after turning on the computer?")
#     root.no.yes.yes.no.yes.yes = TreeNode("Faulty power supply")
#     root.no.yes.yes.no.yes.no = TreeNode("Faulty hard drive")
#     root.no.yes.yes.no.yes.yes.yes = TreeNode("Overheating")
#     root.no.yes.yes.no.yes.yes.no = TreeNode("Faulty power supply")
    
#     root.no.yes.yes.no.no = TreeNode("Is the computer overheating before shutting down?")
#     root.no.yes.yes.no.no.yes = TreeNode("Overheating")
#     root.no.yes.yes.no.no.no = TreeNode("Faulty power supply")
    
#     root.no.yes.no = TreeNode("Loud fan noise?")
#     root.no.yes.no.yes = TreeNode("Is the fan noise constant or intermittent?")
#     root.no.yes.no.yes.yes = TreeNode("Constant: Dusty components")
#     root.no.yes.no.yes.no = TreeNode("Intermittent: Faulty fan")
#     root.no.yes.no.yes.yes.yes = TreeNode("Dusty components")
#     root.no.yes.no.yes.yes.no = TreeNode("Faulty fan")
    
#     root.no.yes.no.no = TreeNode("Is the computer overheating?")
#     root.no.yes.no.no.yes = TreeNode("Yes: Dusty components")
#     root.no.yes.no.no.no = TreeNode("No: Faulty fan")
    
#     root.no.yes.no = TreeNode("Slow performance?")
#     root.no.yes.no.yes = TreeNode("Has the computer's performance gradually worsened over time?")
#     root.no.yes.no.yes.yes = TreeNode("Yes: Insufficient memory")
#     root.no.yes.no.yes.no = TreeNode("No: Too many background processes")
#     root.no.yes.no.no = TreeNode("Is the CPU usage abnormally high?")
#     root.no.yes.no.no.yes = TreeNode("Yes: High CPU usage")
#     root.no.yes.no.no.no = TreeNode("No: Disk fragmentation")
    
#     root.no.yes.no.no.yes.yes = TreeNode("High CPU usage?")
#     root.no.yes.no.no.yes.yes.yes = TreeNode("Are there any unusual processes consuming CPU resources?")
#     root.no.yes.no.no.yes.yes.yes.yes = TreeNode("Yes: Malware infection")
#     root.no.yes.no.no.yes.yes.yes.no = TreeNode("No: Too many background processes")
    
#     root.no.yes.no.no.yes.no = TreeNode("Blue screen of death?")
#     root.no.yes.no.no.yes.no.yes = TreeNode("Does the blue screen display any error messages?")
#     root.no.yes.no.no.yes.no.yes.yes = TreeNode("Yes: Corrupted system files")
#     root.no.yes.no.no.yes.no.yes.no = TreeNode("No: Driver conflict")
#     root.no.yes.no.no.yes.no.no = TreeNode("Has the computer recently experienced power outages or system crashes?")
#     root.no.yes.no.no.yes.no.no.yes = TreeNode("Yes: Corrupted system files")
#     root.no.yes.no.no.yes.no.no.no = TreeNode("No: Faulty memory")
    
#     root.no.yes.no.no.no = TreeNode("Network connection issues?")
#     root.no.yes.no.no.no.yes = TreeNode("Are other devices on the same network experiencing similar issues?")
#     root.no.yes.no.no.no.yes.yes = TreeNode("Yes: Misconfigured network settings")
#     root.no.yes.no.no.no.yes.no = TreeNode("No: Faulty network adapter")
#     root.no.yes.no.no.no.no = TreeNode("Is there any nearby electronic interference?")
#     root.no.yes.no.no.no.no.yes = TreeNode("Yes: Interference")
#     root.no.yes.no.no.no.no.no = TreeNode("No: Faulty network adapter")
    
#     root.no.yes.no.no.no = TreeNode("Unresponsive keyboard?")
#     root.no.yes.no.no.no.yes = TreeNode("Are any keys physically stuck or unresponsive?")
#     root.no.yes.no.no.no.yes.yes = TreeNode("Yes: Faulty keyboard")
#     root.no.yes.no.no.no.yes.no = TreeNode("No: Loose keyboard cable")
#     root.no.yes.no.no.no.no = TreeNode("Does the keyboard work in BIOS or during system startup?")
#     root.no.yes.no.no.no.no.yes = TreeNode("Yes: Driver issues")
#     root.no.yes.no.no.no.no.no = TreeNode("No: Faulty keyboard")
    
#     root.no.yes.no.no.no = TreeNode("USB device not recognized?")
#     root.no.yes.no.no.no.yes = TreeNode("Have you tried connecting the USB device to different ports?")
#     root.no.yes.no.no.no.yes.yes = TreeNode("Yes: Faulty USB port")
#     root.no.yes.no.no.no.yes.no = TreeNode("No: Driver issues")
    
#     root.no.no = TreeNode("Computer won't power on?")
#     root.no.no.yes = TreeNode("Are there any unusual smells coming from the computer?")
#     root.no.no.yes.yes = TreeNode("Yes: Faulty power supply")
#     root.no.no.yes.no = TreeNode("No: Faulty motherboard")
#     root.no.no.no = TreeNode("Is there any visible damage to the power supply unit?")
#     root.no.no.no.yes = TreeNode("Yes: Faulty power supply")
#     root.no.no.no.no = TreeNode("No: Faulty motherboard")
    
#     return root


# @app.route("/start", methods=["GET"])
# def start_diagnosis():
#     root = build_tree()
#     print(root.data, file=sys.stderr)
#     with open("temp", "wb") as f:
#         pickle.dump(root, f)
#     # return "Diagnosis started."
#     return jsonify({"question": root.data})

# @app.route("/answer/<ans>", methods=["GET"])
# def answer_question(ans):
#     with open("temp", "rb") as f:
#         root = pickle.load(f)
#     if ans.lower() == "yes":
#         root = root.yes
#     elif ans.lower() == "no":
#         root = root.no
#     else:
#         return jsonify({"error": "Invalid answer."})
    
#     if root.yes is None and root.no is None:
#         return jsonify({"diagnosis": root.data})
#     else:
#         with open("temp", "wb") as f:
#             pickle.dump(root, f)
#         return jsonify({"question": root.data})
    
#     with open("temp", "wb") as f:
#         pickle.dump(root, f)
#         return jsonify({"question": root.data})


# # @app.route("/diagnose", methods=["POST"])
# # def diagnose():
# #     symptoms = request.form.getlist("symptoms")
# #     # diagnosis = "Placeholder diagnosis"
# #     # Implement your diagnosis logic here based on the selected symptoms
# #     # with open("temp", "rb") as f:
# #     #     root = pickle.load(f)
# #     root = build_tree()
# #     while root.yes is not None and root.no is not None:
# #         if root.data in symptoms:
# #             root = root.yes
# #         else:
# #             root = root.no
# #     return jsonify({"diagnosis": root.data})

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from pyswip import Prolog

# app = Flask(__name__)

# # Initialize Prolog
# prolog = Prolog()
# prolog.consult("diagnosis.pl")  # Assuming Prolog file is named diagnosis.pl

# @app.route('/diagnose', methods=['POST'])
# def diagnose():
#     symptoms = request.json.get('symptoms')
#     diagnosis = perform_diagnosis(symptoms)
#     return jsonify({'diagnosis': diagnosis})

# def perform_diagnosis(symptoms):
#     all_diagnosis = []
#     for symptom in symptoms:
#         diagnosis = None
#         for result in prolog.query(f"diagnose_symptom({symptom}, Issue)"):
#             diagnosis = result['Issue']
#             break  # We only need the first diagnosis for each symptom
#         if diagnosis:
#             all_diagnosis.append(diagnosis)
#     return all_diagnosis

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from pyswip import Prolog

app = Flask(__name__)

# Initialize Prolog
prolog = Prolog()
prolog.consult("diagnosis.pl")  # Assuming Prolog file is named diagnosis.pl

@app.route('/diagnose', methods=['POST'])
def diagnose():
    symptoms = request.json.get('symptoms')
    diagnosis = perform_diagnosis(symptoms)
    return jsonify({'diagnosis': diagnosis})

def perform_diagnosis(symptoms):
    all_diagnosis = []
    for symptom in symptoms:
        diagnosis = None
        for result in prolog.query(f"diagnose_symptom({symptom}, Issue)"):
            diagnosis = result['Issue']
            break  # We only need the first diagnosis for each symptom
        if diagnosis:
            all_diagnosis.append(diagnosis)
    return all_diagnosis

if __name__ == '__main__':
    app.run(debug=True)