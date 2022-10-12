import os.path

class TextReader:
    
    def __init__(self, file_path:str):
        self.file_path = file_path
    
    @property    
    def file_path(self):
        return self.__file_path
    
    @file_path.setter
    def file_path(self, file_path):
        if isinstance(file_path, str):
            if os.path.exists(file_path):
                if os.path.isfile(file_path) and file_path.split('.')[1] == "txt":
                    self.__file_path = file_path
                else:
                    raise ValueError("It is not a text file!")
            else:
                raise FileNotFoundError("There is no such directory!")
        else:
            raise ValueError("File_Path value must be str!")
                
                
    def get_number_of_characters(self):
        with open(self.__file_path) as file:
            lines = file.readlines()
              
        sum = 0
        for line in lines:
            sum += len(line)
                   
        return sum
    
    
    def get_number_of_lines(self):
        with open(self.__file_path) as file:
            lines = file.readlines()
        
        return len(lines)
        
    def get_number_of_words(self):
        with open(self.__file_path) as file:
            lines = file.readlines()
        
        number_of_words = 0
        for line in lines:
            words = line.split()
            number_of_words += len(words)
            
        return number_of_words
    
    def __str__(self):
        return f"Filepath: {self.__file_path}"
    
