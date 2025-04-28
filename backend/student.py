class Student:
    """student"""
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')

all_students = [
    Student({'id': 1, 'name': 'Harry'}),
    Student({'id': 2, 'name': 'Hermione'}),
    Student({'id': 2, 'name': 'Ron'}),
    Student({'id': 3, 'name': 'Bob'}),
    Student({'id': 3, 'name': 'Bob'}),
]