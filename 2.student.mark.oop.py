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

    def add_course(self, course_id, course_name):
        self.__course[course_id] = {"name" : course_name, "mark": ""}

    def add_mark(self, course_id, mark):
        self.__course[course_id]["mark"] = mark

    def get_mark(self,course_id):
        return self.__course[course_id]["mark"]

class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def course_info(self):
        print(f"COURSE id: {self.__id} - {self.__name}")
        
    def get_name(self):
        return self.__name

class Management_system(Course, Student):
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
            print(f"Enter COURSE info {i+1}")
            C_id = input("id: ")
            C_name = input("Name: ")
            print()
            self.__course[C_id] = Course(C_id, C_name)
            for i in self.__student:
                self.__student[i].add_course(C_id, C_name)
        
    def add_mark(self):
        course_id = input("Enter a COURSE ID to input student marks: ")
        for i in self.__student:
            mark = input(f"Enter {self.__student[i].get_name()}'s mark: ")
            self.__student[i].add_mark(course_id, mark)
        
    def show_mark(self):
        print()
        course_id = input("Enter a COURSE ID you want to see the marks: ")
        print()
        print(f"DISPLAYING STUDENT MARKS IN COURSE: {self.__course[course_id].get_name()}")
        for i in self.__student:
            print(f"{self.__student[i].get_name()}: {self.__student[i].get_mark(course_id)}")

    def list_course(self):
        print()
        print("SHOWING COURSE(S)")
        x = 1
        for i in self.__course:
            print(f"{x}) {self.__course[i].get_name()}")
            x += 1

    def list_student(self):
        print()
        print("SHOWING STUDENT(S)")
        x = 1
        for i in self.__student:
            print(f"{x}) {self.__student[i].get_name()}")
            x += 1

def main():

    mark_management = Management_system()

    mark_management.add_student()

    mark_management.add_course()

    mark_management.add_mark()

    mark_management.list_course()

    mark_management.list_student()

    mark_management.show_mark()

main()