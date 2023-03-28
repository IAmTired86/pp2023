from domains.Uni import University
class Course(University):
    def __init__(self, name, id, credit):
        self.__name = name
        self.id = id
        self.__credit = credit
        self.__marks = {}

    def _getName(self):
        return self.__name

    def _getMarks(self):
        return self.__marks
    
    def _getCredit(self):
        return self.__credit
    
    def __str__(self):
        return f"Name: {self.__name}, ID: {self.id}, Marks: {self.__marks}"
    
    def set_marks(self, student, mark):
        self.__marks[student] = mark
        
    def show_marks(self):
        for student, mark in self.__marks.items():
            print(student)
            print(f"Mark: {mark}")
