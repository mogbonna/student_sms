````markdown
# Student Management System (SMS)

A lightweight, command-line and menu-based Python application to manage student records — add, view, search, update, and delete students — with persistent local storage.

---

## Features

- ✅ Add new students with validation
- 📋 Display all student records
- 🔍 Search for students by name
- ♻️ Update student details (name, age)
- ❌ Delete students from the database
- 🧠 Dual interface: CLI + Interactive menu

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/student-sms.git
cd student-sms
```
````

## Usage

### 🖥️ Command-Line Interface (CLI)

```bash
# Add a new student
student-sms --add --name "Asha" --age 18

# Display all students
student-sms --display

# Search for a student
student-sms --search --name "Asha"

# Update a student
student-sms --update --name "Asha" --new-name "Zehra" --new-age 19

# Delete a student
student-sms --delete --name "Zehra"
```

### 📇 Interactive Menu

```bash
student-sms
```

You'll get a friendly menu with options to add, view, search, update, and delete students.

---

## Project Structure

```
sms/
├── main.py
├── students/
│   ├── add.py
│   ├── delete.py
│   ├── display.py
│   ├── search.py
│   └── update.py
├── data/
│   ├── database.py
│   └── storage.json (auto-generated)
```

---

## License

MIT License © 2025 \Moses Ogbonna

```

---

Let me know if you'd like me to add a section on how to contribute, unit tests, or convert it into a `mkdocs` documentation site.
```
