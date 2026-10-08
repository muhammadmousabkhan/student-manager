students = []


def add_student(name, age):
    student = {
        "name": name,
        "age": age
    }

    students.append(student)


def get_students():
    return students


def search_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student

    return None