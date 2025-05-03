from data.database import students_db,save_data

def add_student(name, age):
    if not name.strip():
        print('Error: Name can not be empty.')
        return
    if not age.strip():
        print('Error: Age can not be empty.')
        return
    
    if not age.isdigit() or int(age)<= 0:
        print('Error: Age must be a positive number.')
        return
    
    student = {'name': name.strip(), 'age': int(age)}
    students_db.append(student)
    save_data(students_db)
    print(f"Student {name} added successfully!")