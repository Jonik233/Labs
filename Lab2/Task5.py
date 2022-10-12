from xml.dom import NotFoundErr

class Student:

    def __init__(self, name:str, surname:str, record_book_number:int, grades: list[int]):
        self.name = name
        self.surname = surname
        self.record_book_number = record_book_number
        self.grades = grades
        self.average_score = sum(self.grades) // len(grades)
        
    def __str__(self):
        return (f"Name: {self.name}\n" + 
                f"Surname: {self.surname}\n" + 
                f"Record book number: {self.record_book_number}\n" + 
                f"Grades: {self.grades}\n" + 
                f"Average score: {self.average_score}\n")
        
    def __eq__(self, other):
        if isinstance(other,Student):
            return (other.name == self.name and other.surname == self.surname and other.record_book_number == self.record_book_number)
        else:
            raise TypeError("TypeValue of a given parameter must be Student!")

class Group:
    
    def __init__(self, group_name, capacity=20, student_group:list[Student] = list()):
        self.group_name = group_name
        self.capacity = capacity
        self.student_group = student_group
        
    def add_student(self, student: Student):
        if isinstance(student, Student):
            
            if len(self.student_group) != self.capacity:
            
                if not self.student_group.__contains__(student):
                    self.student_group.append(student)
                else:
                    raise Exception("Student group already contains such a student")
            
            else:
                raise Exception("Group is already full")
        else:
            raise TypeError("The type of member of the group must be Student")
        
    def remove_student(self, student: Student):
        if isinstance(student, Student):       
            if self.student_group.__contains__(student):
                self.student_group.remove(student)
            else:
                raise NotFoundErr("Group doesn't contain such a student")
        else:
            raise TypeError("The type of member of the group must be Student")

    def get_student(self, name:str, surname:str):
        isFound = False
        
        for student in self.student_group:
            if (student.name, student.surname) == (name, surname):
                isFound = True
                return student
            
            if not isFound:
                raise NotFoundErr("Group doesn't contain such a student")
            
    
    def __str__(self):
        students = ""
        
        for student in self.student_group:
                students += student.__str__() + "\n\n"
        
        return students
    
    def top5_students(self):
        leader_board = sorted([(student, student.average_score) for student in self.student_group], key=lambda student: student[1], reverse=True)
        return leader_board[:5]
    
if __name__ == '__main__':
    group = Group("Oplot")
    group.add_student(Student("Silly", "Gypsy", 1, [3,3,3,3]))
    group.add_student(Student("Comrade", "Gagarin", 2, [5,5,5,5]))
    group.add_student(Student("Captain", "Sparrow", 3, [4,4,3,3]))
    group.add_student(Student("Maestro", "Ponasenkov", 4, [1,2,3,4]))
    group.add_student(Student("Vitaly", "Gromiako", 5, [4,4,4,4]))
    group.add_student(Student("Doctor", "Tenma", 6, [2,2,3,5]))
    group.add_student(Student("Billy", "Herrington", 7, [4,4,4,5]))

    for student in group.top5_students():
        print(student[0])
        
