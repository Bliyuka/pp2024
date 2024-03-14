from math import floor

class Student:
    def __init__(self, id, name, DoB):
        self.__id = id
        self.__name = name
        self.__DoB = DoB
        self.__GPA = 0
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
        self.__course[course.get_id()] = {"name": course.get_name(), "mark": -1}

    def set_mark(self, course_id, mark):
        file = open("marks.txt","a")
        self.__course[course_id]["mark"] = floor(mark)
        mark_info = f"{course_id} - {self.__name}: {mark}\n"
        file.write(mark_info)
        file.close()
    
    def get_mark(self, course_id):
        return self.__course[course_id]["mark"]

    def set_GPA(self, gpa):
        self.__GPA = gpa
    
    def get_GPA(self):
        return self.__GPA