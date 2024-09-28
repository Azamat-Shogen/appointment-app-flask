from appointmentapp import app
from flask import render_template, request, jsonify
import os
import json


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/viewAvailabilities')
def viewAvailabilities():
    directory = os.path.join(os.path.dirname(__file__), '../data')
    use_names = []

    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                use_names.append(filename.rstrip('.json'))
    else:
        raise Exception(f"The directory {directory} does not exist.")


    return render_template('list_available_users.html', names=use_names)

@app.route('/addAvailability')
def addAvailability():
    return render_template('add_availability.html')


@app.route('/getAvailabilityForUser/<username>')
def getAvailabilityForUser(username):
    f_name = os.path.join(os.path.dirname(__file__), '../data', f"{username}.json")
    if os.path.exists(f_name):
        with open(f_name, 'r') as f:
            data = json.load(f)
        return render_template('availability_per_person.html', user_name=username, availabilities=data)
    else:
        return jsonify({"status": "failed", "reason": "User not found."}), 404
    

@app.route('/saveAvailability', methods=['POST'])
def save_availability():
    name = request.form.get('name')
    availabilities = request.form.getlist('availability')  # Assuming availability is an array

    if not name or not availabilities:
        bad_response = {
            'status': 'failed',
            'reason': "'name' and 'availabilites' are required fields for the 'saveAvailability' api."
        }
        return jsonify(bad_response), 400
    
    # Ensure 'data' directory exists
    data_directory = os.path.join(os.path.dirname(__file__), '../data')
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    file_name = os.path.join(data_directory, f"{name}.json")
    is_file = os.path.isfile(file_name)
    if is_file:
        with open(file_name, 'r') as f:
            data = json.load(f)

        with open(file_name, 'w') as f:
            # we already have a list in the file, so take the 'availabilities' list and add it
            data.extend(availabilities)
            json.dump(data, f)
    else:
        with open(file_name, 'w') as f:
            # availabilities comes as a list so just save it as a json
            json.dump(availabilities, f)

    return render_template("home.html")