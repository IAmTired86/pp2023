# University class for polymorphism
class University:
    def _print(self):
        pass

# Student class
class Student(University):
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, DOB: {self.dob}"

# Course class    
class Course(University):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.marks = {}
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Marks: {self.marks}"
    
    def set_marks(self, student, mark):
        self.marks[student] = mark
        
    def show_marks(self):
        for student, mark in self.marks.items():
            print(student)
            print(f"Mark: {mark}")

# Create student list
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
        courses.append(Course(name, id))
        print("Course added successfully")
        
# Input marks for student
def input_marks():
    id = input("Enter course id: ")
    found = False
    for course in courses:
        if course.id == id:
            found = True
            for student in students:
                mark = int(input(f"Enter mark for {student.name}: "))
                course.set_marks(student, mark)
            print("Marks added successfully")
            break
    if not found:
        print("Course not found!!!!!")
        print("Input valid course id >:( ")

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
          
# Main program
input_students()
input_courses()
while True:
    print("\nSelect option:")
    print("1. Input mark")
    print("2. Show student")
    print("3. Show course")
    print("4. Show mark")
    print("5. Exit")
    
    try:
        option = int(input("Enter option: "))
        if option == 1:
            input_marks()
        elif option == 2:
            show_students()
        elif option == 3:
            show_courses()
        elif option == 4:
            show_marks()
        elif option == 5:
            break
        else:
            print("Invalid option! Please input valid choice!")
    except ValueError:
        print("Invalid value entered! Please enter the correct value with specified TYPE i.e. INTEGER etc!")
