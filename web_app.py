from flask import Flask, render_template, request, redirect
from database import get_connection

app = Flask(__name__)


@app.route("/")
def home():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        students=students
    )
@app.route("/add", methods=["GET", "POST"])

def add_student():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        email = request.form["email"]
        phone = request.form["phone"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO students
            (name, age, course, email, phone)
            VALUES (?, ?, ?, ?, ?)
        """, (name, age, course, email, phone))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_student.html")

@app.route("/delete/<int:id>")
def delete_student(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    ) 

    conn.commit()
    conn.close()

    return redirect("/")
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_student(id):

    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        email = request.form["email"]
        phone = request.form["phone"]

        cursor.execute("""
            UPDATE students
            SET name=?, age=?, course=?, email=?, phone=?
            WHERE id=?
        """, (name, age, course, email, phone, id))

        conn.commit()
        conn.close()

        return redirect("/")

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    )

    student = cursor.fetchone()

    conn.close()

    return render_template(
        "update_student.html",
        student=student
    )

if __name__ == "__main__":
    app.run(debug=True)