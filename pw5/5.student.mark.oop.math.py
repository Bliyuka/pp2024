from Management_system import Management_system


mark_management = Management_system()

choose = ("""0. Exit
    1. Input STUDENT
    2. Input COURSE
    3. Select a course ID and input student marks
    4. Display STUDENT list
    5. Display COURSE list
    6. show mark from a chosen course
    7. Show GPA of a student
    8. Sort student list by GPA descending""")

print()
print("What do you want to do?")

while True:
    print()
    print(choose)
    user = input("--> CHOOSE AN OPTION: ")
    print()
    if user == "0":
        mark_management.Zipfile()
        break
    elif user == "1":
        mark_management.add_student()
        mark_management.add_course_into_student()
    elif user == "2":
        mark_management.add_course()
        mark_management.add_course_into_student()
    elif user == "3":
        mark_management.add_mark()
    elif user == "4":
        mark_management.list_student()
    elif user == "5":
        mark_management.list_course()
    elif user == "6":
        mark_management.show_mark()
    elif user == "7":
        mark_management.GPA_one()
    elif user == "8":
        mark_management.GPA_descending()
    else:
        print("Please enter a valid option\n")
