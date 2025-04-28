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