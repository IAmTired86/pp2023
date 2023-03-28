from domains.Uni import University
class Student(University):
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
    
    def _getName(self):
        return self.__name
    
    def _getId(self):
        return self.__id
    
    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__id}, DOB: {self.__dob}"