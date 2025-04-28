from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
# import for tiny thing 1
# tiny thing 2 related to tiny thing 1

load_dotenv() # Loads vars in .env file so we can now use `os.environ['MY_VAR]`
print(os.environ['FLASK_ENV'])
print(os.environ['MY_SECRET_API_KEY'])

# tiny thing 3 for tiny thing 1

app = Flask(__name__)
CORS(app)

class Student:
    """student"""
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')

all_students = []
# Add some students
all_students.append(Student({'id': 1, 'name': 'Harry'}))
all_students.append(Student({'id': 2, 'name': 'Hermione'}))
all_students.append(Student({'id': 2, 'name': 'Ron'}))
all_students.append(Student({'id': 3, 'name': 'Bob'}))
all_students.append(Student({'id': 3, 'name': 'Bob'}))

@app.route('/', methods=['GET'])
def base_route():
    return "ping"

@app.route('/students', methods=['GET'])
def get_students():
    # tiny thing 1
    """get all students"""
    student_list = [
        {'id': student.id, 'name': student.name}
        for student in all_students
    ]
    return jsonify(student_list)

IS_DEBUG_ENABLED = False
if os.environ['FLASK_ENV'] == "dev":
    IS_DEBUG_ENABLED = True

app.run(debug=IS_DEBUG_ENABLED)