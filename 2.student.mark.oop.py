class Student:
    def __init__(self, id, name, DoB): 
        self.__id = id
        self.__name = name
        self.__DoB = DoB
        self.__course = {}

    # def set_id(self, id):
    #     print(f"set STUDENT id to {id}")
    #     self.__id = id

    # def set_name(self, name):
    #     print(f"set STUDENT name to {name}")
    #     self.__name = name

    # def set_DoB(self, DoB):
    #     print(f"set STUDENT DoB to {DoB}")
    #     self.__DoB = DoB

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

    
    # def set_id(self, id):
    #     self.__id = id
    #     print(f"set COURSE id to {self.get_id()}")
    
    # def get_id(self):
    #     return self.__id
    
    # def set_name(self, name):
    #     self.__name = name
    #     print(f"set COURSE name to {self.get_id()}")
        
    def get_name(self):
        return self.__name

    # def add_course_info(self):
    #     Cid = input("Enter COURSE id: ")
    #     self.set_id(Cid)
    #     Cname = input ("Enter COURSE name: ")
    #     self.set_name(Cname)

class Management_system(Course, Student):
    def __init__(self):
        self.__student = {}
        self.__course = {}
        
    def add_student(self, id, name, DoB):
        self.__student[id] = Student(id, name, DoB)
        
    def add_course(self, c_id, c_name):
        self.__course[c_id] = Course(c_id, c_name)
        for i in self.__student:
            self.__student[i].add_course(c_id, c_name)
        
    def add_mark(self, std_id, course_id, mark):
        self.__student[std_id].add_mark(course_id, mark)
        
    def show_mark(self, course_id):
        print(f"DISPLAYING STUDENT MARKS IN COURSE: {self.__course[course_id].get_name()}")
        for i in self.__student:
            print(f"{self.__student[i].get_name()}: {self.__student[i].get_mark(course_id)}")
            
    def list_course(self):
        print("SHOWING COURSE(S)")
        for i in self.__course:
            print(self.__course[i].get_name())

    def list_student(self):
        print("SHOWING STUDENT(S)")
        for i in self.__student:
            print(self.__student[i].get_name())


mark_management = Management_system()

S_num = int(input("Enter number of STUDENT: "))
for i in range(S_num):
    print(f"Enter STUDENT info {i+1}")
    S_id = input("id: ")
    S_name = input("Name: ")
    S_DoB = input("DoB: ")
    print()
    mark_management.add_student(S_id, S_name, S_DoB)

C_num = int(input("Enter number of COURSE: "))
for i in range(C_num):
    print(f"Enter COURSE info {i+1}")
    C_id = input("id: ")
    C_name = input("Name: ")
    print()
    mark_management.add_course(C_id, C_name)

# course_id = input("Enter a COURSE ID to input student marks: ")
# for i in mark_management.__student:
#     print(i)

mark_management.add_mark("111", "11","19") #student_id - course_id - mark
mark_management.add_mark("222", "11","20")
mark_management.add_mark("111", "22","15")

mark_management.list_course()

mark_management.list_student()

mark_management.show_mark("11")