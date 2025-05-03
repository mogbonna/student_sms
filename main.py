import argparse
import sys
from students.add import add_student
from students.display import display_students
from students.search import search_student
from students.delete import delete_student
from students.update import update_student



def cli_mode():
    parser = argparse.ArgumentParser(description="Student Management System")

    parser.add_argument('--add', action='store_true', help="Add a new student")
    parser.add_argument('--display', action='store_true', help="Display all students")
    parser.add_argument('--search', action='store_true', help="Search for a student")
    parser.add_argument('--delete', action='store_true', help="Delete a student")
    parser.add_argument('--update', action='store_true', help="Update a student")

    parser.add_argument('--name', type=str, help="Name of the student")
    parser.add_argument('--age', type=str, help="Age of the student")
    parser.add_argument('--new-name', type=str, help="New name of the student")
    parser.add_argument('--new-age', type=str, help="New age of the student")

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

    elif args.delete:
        if args.name:
            delete_student(args.name)
        else:
            print("Error: --delete requires --name")

    elif args.update:
        if args.name and (args.new_name or args.new_age):
            update_student(args.name, args.new_name, args.new_age)
        else:
            print("Error: --update requires --name and at least one of --new-name or --new-age")

    else:
        parser.print_help()

def menu_mode():
    while True:
        try:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Exit")

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
                name = input("Enter name to delete: ")
                delete_student(name)
            elif choice == '5':
                old_name = input("Enter the current name: ")
                new_name = input("Enter the new name (or press Enter to skip): ")
                new_age = input("Enter the new age (or press Enter to skip): ")
                update_student(old_name, new_name, new_age)
            elif choice == '6':
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
