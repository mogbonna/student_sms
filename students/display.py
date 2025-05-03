from data.database import students_db

def display_students():
    if not students_db:
        print("No student to display.")
        return
    for i, student in enumerate(students_db, 1):
        print(f"{i}. Name:{student['name']}, Age: {student['age']}")