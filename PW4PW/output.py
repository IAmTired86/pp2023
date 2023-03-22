from domains.students import Student
from domains.Courses import Course

import input
students = input.students
courses = input.courses

# Show student info
def show_students():
    print("Student list:")
    for student in students:
        print(student)

# Show course info
def show_courses():
    print("Course list:")
    for course in courses:
        print(course)

# Show marks for student
def show_marks():
    id = input("Enter course id to show marks: ")
    found = False
    for course in courses:
        if course.id == id:
            found = True
            print("Marks:")
            course.show_marks()
            break
    if not found:
        print("Course not found!!!!!")
        print("Input valid course id >:( ")

def show_gpa():
    id = input("Enter student id to show GPA: ")
    for student in students:
        if student._getId() == id:
            print(f"Name: {student._getName()}")
            print(f"GPA: {calculate_gpa()}")
