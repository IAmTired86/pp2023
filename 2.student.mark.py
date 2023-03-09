#Student manager system using oops concept
#University class for polymorphism
class University:
    def _print(self):
        pass
#Student class
class Student(University):
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
    def _printStudent(self):
        print("Name: ", self.__name)
        print("ID: ", self.__id)
        print("DOB: ", self.__dob)
    def _getIdStudent(self):
        return self.__id
    def _getNameStudent(self):
        return self.__name


#Course class
class Course(University):
    
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__mark = {}
    
    def _printCourse(self):
        print("Name: ", self.__name)
        print("ID: ", self.__id)
        print("Mark: ", self.__mark)
    
    def _getIdCourse(self):
        return self.id
    def _getNameCourse(self):
        return self.__name
    def _getMarkCourse(self):
        return self.__mark
    def _setMarkCourse(self, mark):
        self.__mark.update({Student: mark})  
    def _showMarkCourse(self):
        for (student,id,mark) in self.__mark.items():
            print(f"Student: {student}")
            print(f"ID: {id}")
            print(f"Mark:  {mark}")


#Create student list
StudentList = []    
#Input student info
def inputStudent():
    NumberOfStudent = int(input("Enter number of student: "))
    for i in range(NumberOfStudent):
        name = input("Enter student name: ")
        id = input("Enter student id: ")
        dob = input("Enter student dob: ")
        StudentList.append(Student(name, id, dob))
        print("Student added successfully")

#Create course list
CourseList = []

#Input course info
def inputCourse():
    NumberOfCourse = int(input("Enter number of course: "))
    for i in range(NumberOfCourse):
        name = input("Enter course name: ")
        id = input("Enter course id: ")
        CourseList.append(Course(name, id))
        print("Course added successfully")

#input mark for student
def inputMark():
    id = input("Enter course id: ")
    if id not in CourseList:
        print("Course not found!!!!!")
        print("Input valid course id >:( ")
        return
    else:
        for student in StudentList:
            mark = int(input(f"Enter mark for {student._getNameStudent()}: "))
            CourseList[id]._setMarkCourse(student._getID(),mark)

        

#Show student info
def showStudent():
    print("Student list:")
    for student in StudentList:
        student._printStudent()

#Show course info
def showCourse():
    print("Course list:")
    for course in CourseList:
        course._printCourse()

#Show mark for student
def showMark():
    id = input("Enter course id to show marks: ")
    if id not in CourseList:
        print("Course not found!!!!!")
        print("Input valid course id >:( ")
        return
    else:
        CourseList[id]._showMarkCourse()



#main
inputStudent()
inputCourse()
while True:
    print("Select option:")
    print("1. Input mark")
    print("2. Show student")
    print("3. Show course")
    print("4.Show mark")
    print("5. Exit")
    option = int(input("Enter option: "))
    if option == 1:
        inputMark()
    elif option == 2:
        showStudent()
    elif option == 3:
        showCourse()
    elif option == 4:
        showMark()
    elif option == 5:
        break

    
    