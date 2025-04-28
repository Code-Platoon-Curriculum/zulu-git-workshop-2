from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
# from .student import Student, all_students
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

every_student = []
# Add some students
every_student.append(Student({'id': 1, 'name': 'Jon Snow'}))
every_student.append(Student({'id': 2, 'name': 'Daenerys'}))
every_student.append(Student({'id': 2, 'name': 'Mr. White Walker'}))
every_student.append(Student({'id': 3, 'name': 'The Hound'}))
every_student.append(Student({'id': 3, 'name': 'Sage'}))

@app.route('/', methods=['GET'])
def base_route():
    return "pong"

@app.route('/students', methods=['GET'])
def get_students():
    # tiny thing 1
    """get all students"""
    student_list = [
        {'id': student.id, 'name': student.name}
        for student in every_student
    ]
    return jsonify(student_list)

@app.route('/goodbye', methods=['GET'])
def say_goodbye(id):
    student = next((s for s in every_student if s['id'] == id), None)
    return f"Goodbye, {student.name}!"


IS_DEBUG_ENABLED = False
if os.environ['FLASK_ENV'] == "dev":
    IS_DEBUG_ENABLED = True

app.run(debug=IS_DEBUG_ENABLED)