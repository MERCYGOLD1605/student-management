import csv
from database import get_connection


def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def add_student():
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not age or not course or not email or not phone:
        print("All fields are required!")
        return

    if not age.isdigit():
        print("Age must be a number!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (name, age, course, email, phone)
        VALUES (?, ?, ?, ?, ?)
        """,
        (name, int(age), course, email, phone)
    )

    conn.commit()
    conn.close()

    print("Student added successfully!")


def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    if not students:
        print("No records found!")
        return

    print("\n----- Student Records -----")

    for student in students:
        student_id, name, age, course, email, phone = student

        print(f"\nID     : {student_id}")
        print(f"Name   : {name}")
        print(f"Age    : {age}")
        print(f"Course : {course}")
        print(f"Email  : {email}")
        print(f"Phone  : {phone}")
        print("---------------------------")


def delete_student():
    view_students()

    try:
        student_id = int(input("Enter Student ID to delete: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))

        if cursor.rowcount == 0:
            print("Student not found!")
        else:
            print("Deleted successfully!")

        conn.commit()
        conn.close()

    except ValueError:
        print("Please enter a valid ID!")


def update_student():
    view_students()

    try:
        student_id = int(input("Enter Student ID to update: "))

        name = input("New name: ").strip()
        age = input("New age: ").strip()
        course = input("New course: ").strip()
        email = input("New email: ").strip()
        phone = input("New phone number: ").strip()

        if not name or not age or not course or not email or not phone:
            print("All fields are required!")
            return

        if not age.isdigit():
            print("Age must be a number!")
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE students
            SET name=?, age=?, course=?, email=?, phone=?
            WHERE id=?
        """, (name, int(age), course, email, phone, student_id))

        if cursor.rowcount == 0:
            print("Student not found!")
        else:
            print("Updated successfully!")

        conn.commit()
        conn.close()

    except ValueError:
        print("Please enter a valid ID!")


def search_student():
    query = input("Enter name to search: ").strip().lower()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE LOWER(name) LIKE ?",
        ('%' + query + '%',)
    )

    students = cursor.fetchall()

    conn.close()

    if not students:
        print("No matching student found!")
        return

    print("\nMatching Students:")

    for student in students:
        student_id, name, age, course, email, phone = student

        print(
            f"ID: {student_id} | "
            f"Name: {name} | "
            f"Age: {age} | "
            f"Course: {course} | "
            f"Email: {email} | "
            f"Phone: {phone}"
        )


def sort_students():
    print("1. Sort by Name")
    print("2. Sort by Age")

    choice = input("Choose: ")

    conn = get_connection()
    cursor = conn.cursor()

    if choice == "1":
        cursor.execute("SELECT * FROM students ORDER BY name ASC")
    elif choice == "2":
        cursor.execute("SELECT * FROM students ORDER BY age ASC")
    else:
        print("Invalid choice!")
        conn.close()
        return

    students = cursor.fetchall()
    conn.close()

    print("\nSorted Students:")

    for student in students:
        student_id, name, age, course, email, phone = student

        print(
            f"ID: {student_id} | "
            f"{name} | "
            f"Age: {age} | "
            f"Course: {course} | "
            f"Email: {email} | "
            f"Phone: {phone}"
        )

def export_to_csv():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        name,
        age,
        course,
        email,
        phone
        FROM students
    """)

    students = cursor.fetchall()
    conn.close()

    if not students:
        print("No data to export!")
        return

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Age",
            "Course",
            "Email",
            "Phone"
        ])

        writer.writerows(students)

    print("Exported to students.csv successfully!")


def count_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    conn.close()

    print(f"Total students: {count}")

def course_statistics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT course, COUNT(*)
        FROM students
        GROUP BY course
    """)

    results = cursor.fetchall()

    if not results:
        print("No student records found!")
        conn.close()
        return

    print("\n----- Course Statistics -----")

    for course, count in results:
        print(f"{course} : {count} student(s)")

    conn.close()


def search_student_by_id():
    try:
        student_id = int(input("Enter Student ID: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        conn.close()

        if student:
            student_id, name, age, course, email, phone = student

            print("\n----- Student Found -----")
            print(f"ID     : {student_id}")
            print(f"Name   : {name}")
            print(f"Age    : {age}")
            print(f"Course : {course}")
            print(f"Email  : {email}")
            print(f"Phone  : {phone}")

        else:
            print("Student not found!")

    except ValueError:
        print("Please enter a valid ID!")

def student_analytics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            AVG(age),
            MIN(age),
            MAX(age)
        FROM students
    """)

    result = cursor.fetchone()
    conn.close()

    total, average, youngest, oldest = result

    if total == 0:
        print("No student records found!")
        return

    print("\n----- Student Analytics -----")
    print(f"Total Students : {total}")
    print(f"Average Age    : {average:.2f}")
    print(f"Youngest Age   : {youngest}")
    print(f"Oldest Age     : {oldest}")


# Create database when application starts
create_database()


while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Search 6.Sort 7.Export to CSV 8.Count Students 9.Exit 10.Course Stats 11.Search by ID 12.Student Analytics")

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

    elif ch == "10":
         course_statistics()
    elif ch == "11":
        search_student_by_id()  
    elif ch == "12":
        student_analytics() 
    else:
        print("Invalid choice!")