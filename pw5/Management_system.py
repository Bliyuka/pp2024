from Course import Course
from Student import Student
import zipfile 
from pathlib import Path
import os

class Management_system():
    def __init__(self):
        self.__student = {}
        self.__course = {}
        
    def add_student(self):
        file = open("student.txt","a")
        
        S_num = int(input("Enter number of STUDENT: "))
        for i in range(S_num):
            print(f"Enter STUDENT info {i+1}")
            S_id = input("id: ")
            S_name = input("Name: ")
            S_DoB = input("DoB: ")
            print()
            self.__student[S_id] = Student(S_id, S_name, S_DoB)
            S_info = f"{S_id} - {S_name} - {S_DoB}\n"
            file.write(S_info)
        file.close()
        
    def add_course(self):
        file = open("course.txt","a")
        C_num = int(input("Enter number of COURSE: "))
        for i in range(C_num):
            print(f"Enter COURSE info {i+1}:")
            C_id = input("id: ")
            C_name = input("Name: ")
            C_cred = int(input("Credit(s): "))
            print()
            self.__course[C_id] = Course(C_id, C_name, C_cred)
            C_info = f"{C_id} - {C_name} - {C_cred}\n"
            file.write(C_info)
        file.close()
            
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
                mark = int(input(f"Enter {self.__student[i].get_name()}'s mark: "))
                self.__student[i].set_mark(course_id, mark)

    def show_mark(self):
        self.list_course()
        course_id = input("Enter a COURSE ID you want to see the marks: ")
        print()
        if course_id not in self.__course:
            print("NOT AVAILABLE COURSE ID")
        print(f"DISPLAYING STUDENT MARKS IN COURSE: {self.__course[course_id].get_name()}")
        for i in self.__student:
            print(f"{self.__student[i].get_id()} - {self.__student[i].get_name()}: {self.__student[i].get_mark(course_id)}")

    def list_course(self):
        print("SHOWING COURSE(s)")
        # x = 1
        # for i in self.__course: 
        #     print(f"{x}) {self.__course[i].get_id()} - {self.__course[i].get_name()}")
        #     x +=1
        try:
            with open("course.txt","r") as file:
                data = file.read()
                print(data)
        except:
            print("no course.txt found")

    def list_student(self):
        print("SHOWING STUDENT(s)")
        # x = 1
        # for i in self.__student:
        #     print(f"{x}) {self.__student[i].get_id()} - {self.__student[i].get_name()}")
        #     x += 1
        try:
            with open("student.txt", "r") as file:
                data = file.read()
                print(data)
        except:
            print("no student.txt found")

    def GPA_cal(self,S_id):
        tot_mark = 0
        tot_cred = 0
        if S_id not in self.__student:
            print("INVALID STUDENT ID")
        else:
            for i in self.__student[S_id].get_course():
                if self.__student[S_id].get_course()[i]["mark"] == -1:
                    print(f"Haven't input COURSE '{self.__student[S_id].get_course()[i]["name"]}' mark for {self.__student[S_id].get_name()}")
                    return False
                tot_mark += self.__student[S_id].get_course()[i]["mark"] * self.__course[i].get_cred()
                tot_cred += self.__course[i].get_cred()
            return tot_mark/tot_cred

    def GPA_one(self):
        self.list_student()
        student_id = input("Enter STUDENT ID to see the GPA: ")
        gpa = self.GPA_cal(student_id)
        print(f"{self.__student[student_id].get_name()}'s GPA: {gpa}")

    def GPA_descending(self):
        markList = []
        for i in self.__student:
            markList.append(self.GPA_cal(i))
            self.__student[i].set_GPA(self.GPA_cal(i))
        # print(markList)
        markList.sort(reverse = True)
        x = 1
        for i in markList:
            for j in self.__student:
                if i == self.__student[j].get_GPA():
                    print(f"{x}) {self.__student[j].get_id()} - {self.__student[j].get_name()}: {self.__student[j].get_GPA()}")
            x += 1

    def Zipfile(self):
        # path = Path("./students.dat")
        # if path.is_file() != True:
        student_system =  zipfile.ZipFile("students.dat", "w")
        try: student_system.write("student.txt")
        except: print("zipfile: no student.txt found")
        try: student_system.write("course.txt")
        except: print("zipfile: no course.txt found")
        try: student_system.write("marks.txt")
        except: print("zipfile: no marks.txt found")
        student_system.close()

        try: os.remove("student.txt")
        except: print("remove: no student.txt found")
        try: os.remove("course.txt")
        except: print("remove: no course.txt found")
        try: os.remove("marks.txt")
        except: print("remove: no marks.txt found")