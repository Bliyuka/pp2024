class Course:
    def __init__(self, id, name, cred):
        self.__id = id
        self.__name = name
        self.__cred = cred
    
    def course_info(self):
        print(f"COURSE id: {self.__id} - {self.__name}")
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_cred(self):
        return self.__cred