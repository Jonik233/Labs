import math

class Rational:
    
    def __init__(self,  numerator=1, denominator=1):
        if isinstance(numerator, int) and isinstance(denominator, int):
            if denominator != 0:
                self.numerator = numerator
                self.denominator = denominator
            else:
                raise ZeroDivisionError("Denominator can't be 0!")
        else:
            raise TypeError("Type of values must be int!")
        
    def __str__(self):
        
        numerator = self.numerator
        denominator = self.denominator
        
        gcd = math.gcd(numerator, denominator)
        while gcd != 1:
            gcd = math.gcd(numerator, denominator)
            numerator = numerator // gcd  
            denominator = denominator // gcd
        
        return f"{numerator}/{denominator}"        
    
    def get_simplified_form(self):
        return self.__str__()

    def get_float_form(self):
        return self.numerator / self.denominator
