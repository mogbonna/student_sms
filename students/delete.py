from data.database import students_db, save_data

def delete_student(name):
    if not name.strip():
        print("Error: Name cannot be empty.")
        return

    original_count = len(students_db)
    updated_db = [s for s in students_db if s["name"].lower() != name.lower()]

    if len(updated_db) == original_count:
        print(f"No student found with name '{name}'.")
    else:
        save_data(updated_db)
        # Reflect changes in in-memory database
        students_db.clear()
        students_db.extend(updated_db)
        print(f"Student '{name}' deleted successfully.")
