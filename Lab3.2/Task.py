class ICourse:
    def __init__(self, name, teacher, course_program):
        self.name = name
        self.teacher = teacher
        self.course_program = course_program
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("Invalid name")
       
    @property
    def teacher(self):
        return self.__teacher
    
    @teacher.setter
    def teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.__teacher = teacher
        else:
            raise Exception("Invalid teacher")
    
    @property
    def course_programs(self):
        return self.__course_program
    
    @course_programs.setter
    def course_program(self, course_program):
        if isinstance(course_program, CourseProgram):
            self.__course_program = course_program
        else:
            raise Exception("Invalid course program")
    
    def __str__(self):
        return f"Course name: {self.name}\nTeacher: {self.teacher}\nCourse program: {self.course_program}"

class ILocalCourse(ICourse):
    pass

class IOffsiteCourse(ICourse):
    pass

class ITeacher:
    def __init__(self, name, course_program):
        self.name = name
        self.course_program = course_program
        
    @property
    def course_program(self):
        return self.__course_program
    
    @course_program.setter
    def course_program(self, course_program):
        if isinstance(course_program, CourseProgram):
            self.__course_program = course_program
        else:
            raise Exception("Invalid Course Program")
        
    def __str__(self):
        return self.name

class LocalCourse(ILocalCourse):
    pass

class OffsiteCourse(IOffsiteCourse):
    pass

class CourseProgram:
    def __init__(self, topics:list):
        self.topics = topics
    
    def __getitem__(self, item):
        if isinstance(item, int):
            if self.__len__() > item: 
                return self.topics[item]
            raise IndexError
        
        if isinstance(item, slice):
            start = item.start or 0
            stop = item.stop or 0
            step = item.step or 1
            
            res = []
            for i in range(start, stop, step):
                res.append(self.topics[i])
            
            return res
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.__len__() > self.index:
            self.index +=1
            return self.topics[self.index - 1]
        raise StopIteration
        
    def __len__(self):
        return len(self.topics)
    
class Teacher(ITeacher):
    pass

class ICourseFactory:
    
    @staticmethod
    def createCourse(object:ICourse, *parametres):
        pass
    
    @staticmethod
    def createTeacher(object:ITeacher, *parametres):
        pass

class CuourseFactory(ICourseFactory):
    
    @staticmethod
    def createCourse(object:ICourse, *parametres):
        if object.__base__ is ILocalCourse or IOffsiteCourse:
            return object(*parametres)
        raise TypeError
    
    @staticmethod
    def createTeacher(object:ITeacher, *parametres):
        if object.__base__ is ITeacher:
            return object(*parametres)
        raise TypeError