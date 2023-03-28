# Main program
import domains
import input
import output
from input import *
from output import *
input_students()
input_courses()
while True:
    print("\nSelect option:")
    print("1. Input mark")
    print("2. Show student")
    print("3. Show course")
    print("4. Show mark")
    print("5. Calculate GPA")
    print("6. Exit")
    
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
            show_gpa()
        elif option == 6:
            break
        else:
            print("Invalid option! Please input valid choice!")
    except ValueError:
        print("Invalid value entered! Please enter the correct value with specified TYPE i.e. INTEGER etc!")
