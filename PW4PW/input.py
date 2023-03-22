from domains.students import Student
from domains.Courses import Course

import math

students = []
def input_students():
    num_of_students = int(input("Enter number of students: "))
    for i in range(num_of_students):
        name = input("Enter student name: ")
        id = input("Enter student id: ")
        dob = input("Enter student dob: ")
        
        students.append(Student(name, id, dob))
        print("Student added successfully")

# Create course list
courses = []  
def input_courses():
    num_of_courses = int(input("Enter number of courses: "))
    for i in range(num_of_courses):
        name = input("Enter course name: ") 
        id = input("Enter course id: ")
        credit = int(input("Enter course credit: "))
        courses.append(Course(name, id, credit))
        print("Course added successfully")
        
# Input marks for student
def input_marks():
    id = input("Enter course id: ")
    found = False
    for course in courses:
        if course.id == id:
            found = True
            for student in students:
                mark = float(input(f"Enter mark for {student._getName()}: "))
                if mark > 0.0 and mark < 20.0:
                    mark=math.floor(mark * 10)/10
                    course.set_marks(student, mark)
                    print("Marks added successfully")
                    break
                else:
                    print("Invalid mark")
                    break
    if not found:
        print("Course not found!!!!!")
        print("Input valid course id >:( ")

def calculate_gpa():
    gpa = float(0.0)
    total_credit = 0
    total_marks = 0
    for course in courses:
        for student in students:
            mark = course._getMarks()[student]
            credit = course._getCredit()
            total_credit += credit
            total_marks += (mark * credit)
    gpa = round((total_marks / total_credit), 2)
    return gpa