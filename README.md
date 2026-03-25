# 🎓 Student Management System

A simple Python CLI application to manage student records using file handling.

## 🚀 Features
- Add student details
- View all students
- Update student info
- Delete student

## 🛠 Tech Used
- Python
- File Handling

## ▶️ How to Run
```bash
python app.py
def add_student():
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    age = input("Enter age: ").strip()
    if not age.isdigit():
        print("Age must be a number!")
        return

    course = input("Enter course: ").strip()
    if not course:
        print("Course cannot be empty!")
        return

    with open("students.txt", "a") as file:
        file.write(f"{name},{age},{course}\n")

    print("Student added!")



