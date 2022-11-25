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
    
    def __add__(self, other):
        if isinstance(other, Rational):
            denominator = math.lcm(self.denominator, other.denominator)
            numerator = self.numerator * (denominator // self.denominator) + other.numerator * (denominator // other.denominator)
            return Rational(numerator, denominator)
        raise TypeError
    
    def __sub__(self, other):
        if isinstance(other, Rational):
            denominator = math.lcm(self.denominator, other.denominator)
            numerator = self.numerator * (denominator // self.denominator) - other.numerator * (denominator // other.denominator)
            return Rational(numerator, denominator)
        raise TypeError
    
    def __mul__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        raise TypeError
    
    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ZeroDivisionError
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Rational(numerator, denominator)
        raise TypeError
    
    def __eq__(self, other):
        if isinstance(other, Rational):
            return (self.numerator / self.denominator) == (other.numerator / other.denominator)
        raise TypeError
     
    def __lt__(self, other):
         if isinstance(other, Rational):
             return (self.numerator / self.denominator) < (other.numerator / other.denominator)
         raise TypeError
     
    def __gt__(self, other):
        if  isinstance(other, Rational):
            return (self.numerator / self.denominator) > (other.numerator / other.denominator)
        raise TypeError
     
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
