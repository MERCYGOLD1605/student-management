def add_student():
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()

    if not name or not age or not course:
        print("All fields are required!")
        return

    if not age.isdigit():
        print("Age must be a number!")
        return

    with open("students.txt", "a") as file:
        file.write(f"{name},{age},{course}\n")

    print("Student added!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

            if not students:
                print("No records found!")
                return

            for i, s in enumerate(students, 1):
                name, age, course = s.strip().split(",")
                print(f"{i}. Name: {name} | Age: {age} | Course: {course}")
    except FileNotFoundError:
        print("No file found!")


def delete_student():
    view_students()
    try:
        num = int(input("Enter number to delete: "))

        with open("students.txt", "r") as file:
            students = file.readlines()

        if num < 1 or num > len(students):
            print("Invalid number!")
            return

        students.pop(num - 1)

        with open("students.txt", "w") as file:
            file.writelines(students)

        print("Deleted successfully!")
    except ValueError:
        print("Please enter a valid number!")


def update_student():
    view_students()
    try:
        num = int(input("Enter number to update: "))

        with open("students.txt", "r") as file:
            students = file.readlines()

        if num < 1 or num > len(students):
            print("Invalid number!")
            return

        name = input("New name: ").strip()
        age = input("New age: ").strip()
        course = input("New course: ").strip()

        if not name or not age or not course:
            print("All fields are required!")
            return

        if not age.isdigit():
            print("Age must be a number!")
            return

        students[num - 1] = f"{name},{age},{course}\n"

        with open("students.txt", "w") as file:
            file.writelines(students)

        print("Updated successfully!")
    except ValueError:
        print("Please enter a valid number!")


def search_student():
    name_to_search = input("Enter name to search: ").strip().lower()

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
    except FileNotFoundError:
        print("No file found!")
        return

    found = False

    for s in students:
        name, age, course = s.strip().split(",")

        # 🔥 Partial search (Day 3 feature)
        if name_to_search in name.lower():
            print(f"Found: Name: {name} | Age: {age} | Course: {course}")
            found = True

    if not found:
        print("No matching student found!")


while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Search 6.Exit")
    ch = input("Choose: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        update_student()
    elif ch == "4":
        delete_student()
    elif ch == "5":
        search_student()
    elif ch == "6":
        break
    else:
        print("Invalid choice")