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

            print("\n----- Student Records -----")

            for i, s in enumerate(students, 1):
                name, age, course = s.strip().split(",")
                
                print(f"\nStudent {i}")
                print(f"Name   : {name}")
                print(f"Age    : {age}")
                print(f"Course : {course}")
                print("---------------------------")

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
    query = input("Enter name to search: ").strip().lower()

    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
    except FileNotFoundError:
        print("No file found!")
        return

    if not students:
        print("No records available!")
        return

    found = False

    for s in students:
        try:
            name, age, course = s.strip().split(",")
        except ValueError:
            continue  # skip bad lines safely

        if query in name.lower():   # 🔥 partial match
            print(f"Name: {name} | Age: {age} | Course: {course}")
            found = True

    if not found:
        print("No matching student found!")

def sort_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if not students:
            print("No records to sort!")
            return

        print("1. Sort by Name")
        print("2. Sort by Age")
        choice = input("Choose: ")

        data = []
        for s in students:
            name, age, course = s.strip().split(",")
            data.append([name, int(age), course])

        if choice == "1":
            data.sort(key=lambda x: x[0].lower())
        elif choice == "2":
            data.sort(key=lambda x: x[1])
        else:
            print("Invalid choice!")
            return

        print("\nSorted Students:")
        for i, (name, age, course) in enumerate(data, 1):
            print(f"{i}. {name} | Age: {age} | Course: {course}")

    except:
        print("Error sorting students!")

def export_to_csv():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if not students:
            print("No data to export!")
            return

        with open("students.csv", "w") as file:
            file.write("Name,Age,Course\n")
            for s in students:
                file.write(s)

        print("Exported to students.csv successfully!")

    except:
        print("Error exporting!")
def count_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if not students:
            print("No students found!")
            return

        print(f"Total students: {len(students)}")

    except FileNotFoundError:
        print("No file found!")

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Search 6.Sort 7.Export to CSV 8.Count Students 9.Exit")
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
         sort_students()
    elif ch == "7":
        export_to_csv()
    elif ch == "8":
        count_students()
    elif ch == "9": 
        break
        
    else:
            print("Invalid choice") 