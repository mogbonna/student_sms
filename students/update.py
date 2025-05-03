from data.database import students_db, save_data

def update_student(old_name, new_name=None, new_age=None):
    if not old_name.strip():
        print("Error: Existing student name is required.")
        return

    for student in students_db:
        if student["name"].lower() == old_name.lower():
            if new_name and new_name.strip():
                student["name"] = new_name.strip()
            if new_age and new_age.strip().isdigit() and int(new_age) > 0:
                student["age"] = int(new_age)
            save_data(students_db)
            print(f"Student '{old_name}' updated successfully.")
            return

    print(f"Student '{old_name}' not found.")
