def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{age},{course}\n")

    print("Student added!")

def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
            if not students:
                print("No records found!")
            for i, s in enumerate(students, 1):
                name, age, course = s.strip().split(",")
                print(f"{i}. {name} | Age: {age} | Course: {course}")
    except:
        print("No file found!")

def delete_student():
    view_students()
    try:
        num = int(input("Enter number to delete: "))
        with open("students.txt", "r") as file:
            students = file.readlines()
        students.pop(num - 1)
        with open("students.txt", "w") as file:
            file.writelines(students)
        print("Deleted successfully!")
    except:
        print("Invalid input!")

def update_student():
    view_students()
    try:
        num = int(input("Enter number to update: "))
        with open("students.txt", "r") as file:
            students = file.readlines()

        name = input("New name: ")
        age = input("New age: ")
        course = input("New course: ")

        students[num - 1] = f"{name},{age},{course}\n"

        with open("students.txt", "w") as file:
            file.writelines(students)

        print("Updated successfully!")
    except:
        print("Error updating!")
def search_student():
    name_to_search = input("Enter name to search: ").strip().lower()

    found = False
    with open("students.txt", "r") as file:
        students = file.readlines()

    for s in students:
        name, age, course = s.strip().split(",")
        if name.lower() == name_to_search:
            print(f"Found: {name} | Age: {age} | Course: {course}")
            found = True

    if not found:
        print("Student not found!")
        
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
        print("Invalid choice")
