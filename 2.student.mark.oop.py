class Student:
    def __init__(self, id, name, DoB):
        self.__id = id
        self.__name = name
        self.__DoB = DoB
        self.__course = {}
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_DoB(self):
        return self.__DoB
    
    def get_course(self):
        return self.__course

    def add_course(self, course):
        self.__course[course.get_id()] = {"name": course.get_name(), "mark": ""}

    def set_mark(self, course_id, mark):
        self.__course[course_id]["mark"] = mark
    
    def get_mark(self, course_id):
        return self.__course[course_id]["mark"]

class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def course_info(self):
        print(f"COURSE id: {self.__id} - {self.__name}")
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
class Management_system():
    def __init__(self):
        self.__student = {}
        self.__course = {}
        
    def add_student(self):
        S_num = int(input("Enter number of STUDENT: "))
        for i in range(S_num):
            print(f"Enter STUDENT info {i+1}")
            S_id = input("id: ")
            S_name = input("Name: ")
            S_DoB = input("DoB: ")
            print()
            self.__student[S_id] = Student(S_id, S_name, S_DoB)
        
    def add_course(self):
        C_num = int(input("Enter number of COURSE: "))
        for i in range(C_num):
            print(f"Enter COURSE info {i+1}:")
            C_id = input("id: ")
            C_name = input("Name: ")
            print()
            self.__course[C_id] = Course(C_id, C_name)
            
    def add_course_into_student(self):
            for i in self.__student:
                for j in self.__course:
                    if self.__course[j].get_id() not in self.__student[i].get_course():
                        self.__student[i].add_course(self.__course[j])

    def add_mark(self):
        self.list_course()
        print()
        course_id = input("Enter a COURSE ID to input student marks: ")
        if course_id not in self.__course:
            print("NOT AVAILABLE COURSE ID")
        else:
            for i in self.__student:
                mark = input(f"Enter {self.__student[i].get_name()}'s mark: ")
                self.__student[i].set_mark(course_id, mark)

    def show_mark(self):
        course_id = input("Enter a COURSE ID you want to see the marks: ")
        print()
        if course_id not in self.__course:
            print("NOT AVAILABLE COURSE ID")
        print(f"DISPLAYING STUDENT MARKS IN COURSE: {self.__course[course_id].get_name()}")
        for i in self.__student:
            print(f"{self.__student[i].get_name()}: {self.__student[i].get_mark(course_id)}")

    def list_course(self):
        print("SHOWING COURSE(S)")
        for i in self.__course:
            print(f"{self.__course[i].get_id()} - {self.__course[i].get_name()}")

    def list_student(self):
        print("SHOWING STUDENT(S)")
        x = 1
        for i in self.__student:
            print(f"{x}) {self.__student[i].get_name()}")
            x += 1

def main():
    
    mark_management = Management_system()
    
    choose = ("""0. Exit
    1. Input STUDENT
    2. Input COURSE
    3. Select a course ID and input student marks
    4. Display STUDENT list
    5. Display COURSE list
    6. show mark from a chosen course""")

    print("What do you want to do?")
    print("---")
    
    while True:
        print()
        print(choose)
        user = input("--> CHOOSE AN OPTION: ")
        print()
        if user == "0":
            return False
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
        else:
            print("Please enter a valid option\n")

main()
