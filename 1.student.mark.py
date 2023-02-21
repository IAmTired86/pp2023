#Create a dictionary of students,their courses and their marks
Students = {}
Course = {}
Mark_student={}

#Create a function to input student
def Input_student():
    Number_of_student = int(input("Enter number of student: "))
    for i in range(Number_of_student):
        Students_id= input("Enter student id: ")
        Students_name = input("Enter student name: ")
        Students_dob = input("Enter student age: ")
        Students[Students_id]={'name':Students_name,'dob':Students_dob}

#Create a function to input course
def Input_course():
    Number_of_course = int(input("Enter number of course: "))
    for i in range(Number_of_course):
        Course_name = input("Enter course name: ")
        Course_id = input("Enter course id: ")
        Course[Course_id]={'name':Course_name}

#Create a function to input marks
def Input_mark():
    Course_id=input("Enter course id: ")
    if Course_id not in Course:
        print("Invalid course id")
        return
    else:
        for Student_id in Students:
            print("Student id: ",Student_id)
            print("Student name: ",Students[Student_id]['name'])
            print("Student dob: ",Students[Student_id]['dob'])
            for Course_id in Course:
                print("Course id: ",Course_id)
                print("Course name: ",Course[Course_id]['name'])
                Mark = input("Enter mark: ")
                if Student_id not in Mark_student:
                    Mark_student[Student_id]={}
                    Mark_student[Student_id][Course_id]=Mark
            
#Create a function to list student
def list_student():
    for Student_id in Students:
        print("Student id: ",Student_id)
        print("Student name: ",Students[Student_id]['name'])
        print("Student dob: ",Students[Student_id]['dob'])

#Create a function to list course
def list_course():
    for course_id in Course:
        print("Course id: ",course_id)
        print("Course name: ",Course[course_id]['name'])

#Create a function to list mark
def list_mark():
    for Student_id in Students:
        print("Student id: ",Student_id)
        print("Student name: ",Students[Student_id]['name'])
        print("Student dob: ",Students[Student_id]['dob'])
        for Course_id in Course:
            print("Course id: ",Course_id)
            print("Course name: ",Course[Course_id]['name'])
            print("Mark: ",Mark_student[Student_id][Course_id])

#Input student
Input_student()
#Input course
Input_course()

#Create a loop to select course
while True:
    print("1. Input mark")
    print("2. List student")
    print("3. List course")
    print("4. List mark")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Input_mark()
    elif choice == 2:
        list_student()
    elif choice == 3:
        list_course()
    elif choice == 4:
        list_mark()
    elif choice == 5:
        break
    else:
        print("Invalid choice")