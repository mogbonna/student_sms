from data.database import students_db

def search_student(name):
    if not name.strip():
        print('Error: Name can not be empty.')
        return
    
    results = [s for s in students_db if s["name"].lower() == name.lower()]
    if results:
        for s in results:
            print(f"Found: {s['name']}, Age: {s['age']}")
    else:
        print(f"Student '{name}' not found")