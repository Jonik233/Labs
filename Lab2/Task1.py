class Rectangle:
    
    def __init__(self, length=1.0, width=1.0):
      self.set(length, width)
        
    def set(self, length=1.0, width=1.0):
        if isinstance(length, float) and isinstance(width, float):
            if 0.0 < length < 20.0 and 0.0 < width < 20.0:
                self.__length = length
                self.__width = width
            else:
                raise ValueError("Values must be in range(0.0, 20.0)!")
        else:
            raise TypeError("Type of value must be float!")
    
    def get_length(self):
        return self.__length
    
    def get_with(self):
        return self.__width
    
    def get_perimeter(self):
        return 2 * (self.__width + self.__length)
    
    def get_area(self):
        return self.__width * self.__length
    
    def __str__(self):
        return ("Class: " + self.__class__.__name__ + "\nWidth: " + self.width + "\nLength: " + self.length + "\n")
