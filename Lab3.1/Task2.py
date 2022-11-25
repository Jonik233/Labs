import datetime

class Notebook:
    
    def __init__(self, name, surname, phone_number, birth_date):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.__content_elements = []
    
    @property
    def name(self):
        return self.__name    
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
            return
        raise TypeError("Incorrect name value")
    
    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname
            return
        raise TypeError("Incorrect surname value")
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        if isinstance(phone_number, str):
            self.__phone_number = phone_number
            return
        raise TypeError("Incorrect phone number value")
    
    @property
    def birth_date(self):
        return self.__birth_date
    
    @birth_date.setter
    def birth_date(self, date):
        if isinstance(date, datetime.datetime):
            self.__birth_date = date
            return
        raise TypeError("Incorrect date time")

    def __add__(self, other):
        if isinstance(other, Element):
            if self.__content_elements.__contains__(other):
                return self
            self.__content_elements.append(other)
            return self
        raise TypeError("Incorrect element value")
    
    def __sub__(self, other):
        if isinstance(other, Element):
            if self.__content_elements.__contains__(other):
                self.__content_elements.remove(other)
                return self
            raise Exception("NoteBook doesn't contain such an element")
        raise TypeError
    
    def __mul__(self, date):
        if isinstance(date, datetime.datetime):
            elements_at_date = []
            for element in self.__content_elements:
                if element.date == date:
                    elements_at_date.append(element)
            return elements_at_date
        raise TypeError
    
    def __str__(self):
        content = ""     
        for i in self.__content_elements:
            content += f"{i}\n"

        return content
    
class Element:
    
    def __init__(self, content:str, date:datetime.datetime):
        self.content = content
        self.date = date
    
    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, content):
        if isinstance(content, str):
            self.__content = content
            return
        raise TypeError("Incorrect content value")
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        if isinstance(date, datetime.datetime):
            self.__date = date
            return
        raise TypeError("Incorrect date value")
    
    def __str__(self):
        return f"Publication date: {self.date}\n{self.content}"

    def __eq__(self, other):
        if isinstance(other, Element):
            return self.content == other.content and self.date == other.date
        raise TypeError

if __name__ == '__main__':
    noteBook = Notebook("Nick", "Bostrom", "+380421", datetime.datetime(2003, 11, 3))
    noteBook += Element("First note", datetime.datetime(2003, 11, 3))
    noteBook += Element("Second note", datetime.datetime(2003, 11, 3))
    elements = noteBook * datetime.datetime(2003, 11, 3)
    print(noteBook)