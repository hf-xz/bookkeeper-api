from bson.objectid import ObjectId

from database import get_collection

student_collection = get_collection('students_collection')


# helpers
def student_helper(student) -> dict:
    return {
        'id': str(student['_id']),
        'fullname': student['fullname'],
        'course_of_study': student['course_of_study'],
        'year': student['year'],
        'GPA': student['gpa'],
    }


# Retrieve all students present in the database
def retrieve_students():
    students = []
    for student in student_collection.find():
        students.append(student_helper(student))
    return students


# Add a new student into to the database
def add_student(student_data: dict) -> dict:
    student = student_collection.insert_one(student_data)
    new_student = student_collection.find_one(
        {'_id': student.inserted_id})
    return student_helper(new_student)


# Retrieve a student with a matching ID
def retrieve_student(id: str) -> dict:
    student = student_collection.find_one({'_id': ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = student_collection.find_one({'_id': ObjectId(id)})
    if student:
        updated_student = student_collection.update_one(
            {'_id': ObjectId(id)}, {'$set': data})
        if updated_student:
            return True
        return False


# Delete a student from the database
def delete_student(id: str):
    student = student_collection.find_one({'_id': ObjectId(id)})
    if student:
        student_collection.delete_one({'_id': ObjectId(id)})
        return True
