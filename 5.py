student_ids = set()
students = {}

def add_student(student_id, name, marks):
    if student_id in student_ids:
        print("Student ID already exists!")
    else:
        student_ids.add(student_id)
        students[student_id] = {
            "name": name,
            "marks": marks
        }
        print("Student added successfully!")

def update_marks(student_id, new_marks):
    if student_id in students:
        students[student_id]["marks"] = new_marks
        print("Marks updated successfully!")
    else:
        print("Student not found!")

def get_student(student_id):
    if student_id in students:
        return students[student_id]
    else:
        return "Student not found!"

add_student(101, "Alice", 85)
add_student(102, "Bob", 90)

update_marks(101, 95)

print(get_student(101))