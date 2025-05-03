import argparse
import sys
from students.add import add_student
from students.display import display_students
from students.search import search_student

def cli_mode():
    parser = argparse.ArgumentParser(description="Student Management System")

    parser.add_argument('--add', action='store_true', help="Add a new student")
    parser.add_argument('--display', action='store_true', help="Display all students")
    parser.add_argument('--search', action='store_true', help="Search for a student")
    parser.add_argument('--name', type=str, help="Name of the student")
    parser.add_argument('--age', type=str, help="Age of the student")

    args = parser.parse_args()

    if args.add:
        if args.name and args.age:
            add_student(args.name, args.age)
        else:
            print("Error: --add requires both --name and --age")

    elif args.display:
        display_students()

    elif args.search:
        if args.name:
            search_student(args.name)
        else:
            print("Error: --search requires --name")

    else:
        parser.print_help()

def menu_mode():
    while True:
        try:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter name: ")
                age = input("Enter age: ")
                add_student(name, age)
            elif choice == '2':
                display_students()
            elif choice == '3':
                name = input("Enter name to search: ")
                search_student(name)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print("An error occurred:", e)

def main():
    if len(sys.argv) > 1:
        cli_mode()
    else:
        menu_mode()

if __name__ == "__main__":
    main()
