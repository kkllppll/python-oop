
import math
from fractions import Fraction
def gcd(a, b):
        if (a == 0):
            return b
        return gcd(b % a, a)

def lowest(den3, num3):
    common_factor = gcd(num3, den3)

    den3 = int(den3 / common_factor)
    num3 = int(num3 / common_factor)
    return f'{num3} / {den3} |||| {Fraction(num3, den3)}'

 


class Rational():
    def __init__(self, numerator1=0, denominator1 = 1, numerator2=0, denominator2 = 1):  
        self.__numerator1 = numerator1
        self.__denominator1 = denominator1

        self.__numerator2 = numerator2
        self.__denominator2 = denominator2

        @property
        def numerator1(self):
            return self.__numerator1
        
        @property
        def denominator1(self):
            return self.__denominator1

        @denominator1.setter
        def denominator1(self, new_denominator1):
            if denominator1 == 0:
                raise ZeroDivisionError
            
            self.__denominator1 = new_denominator1


        @property
        def numerator2(self):
            return self.__numerator1
        
        @property
        def denominator2(self):
            return self.__denominator2

        @denominator2.setter
        def denominator2(self, new_denominator2):
            if denominator2 == 0:
                raise ZeroDivisionError
            
            self.__denominator2 = new_denominator2


    def function(self):
        result1 = float(eval(str(self.__numerator1 / self.__denominator1)))
        result2 = float(eval(str(self.__numerator2 / self.__denominator2)))
        print(f'{self.__numerator1} / {self.__denominator1} --> {Fraction(result1)}')
        print(f'{self.__numerator2} / {self.__denominator2} --> {Fraction(result2)}')
        
    
    

    def adding(self):
        
        den3 = gcd(self.__denominator1, self.__denominator2)
        den3 = (self.__denominator1 * self.__denominator2) / den3
        num3 = ((self.__numerator1) * (den3 / self.__denominator1) + (self.__numerator2) * (den3 / self.__denominator2))

        return lowest(den3, num3)
   
    def subtracting(self):
        den3 = gcd(self.__denominator1, self.__denominator2)
        den3 = (self.__denominator1 * self.__denominator2) / den3
        num3 = ((self.__numerator1) * (den3 / self.__denominator1) - (self.__numerator2) * (den3 / self.__denominator2))
        return lowest(den3, num3)

    def multiplying(self):
        num3 = self.__numerator1 * self.__numerator2
        den3 = self.__denominator1 * self.__denominator2
        return f'{num3} / {den3} |||| {Fraction(num3, den3)}'

    def dividing(self):
        num3 = self.__numerator1 * self.__denominator2 
        den3 = self.__denominator1 * self.__numerator2
        
        return f'{num3} / {den3} |||| {Fraction(num3, den3)}'


    def comparison(self):
        if self.__numerator1 / self.__denominator1 > self.__numerator2 / self.__denominator2:
            return f"Number {self.__numerator1}/{self.__denominator1} > {self.__numerator2}/{self.__denominator2}"
        elif self.__numerator1 / self.__denominator1 < self.__numerator2 / self.__denominator2:
            return f"Number {self.__numerator1}/{self.__denominator1} < {self.__numerator2}/{self.__denominator2}"
        elif self.__numerator1 / self.__denominator1 == self.__numerator2 / self.__denominator2:
            return f"Number {self.__numerator1}/{self.__denominator1} = {self.__numerator2}/{self.__denominator2}"
        else:
            return "Error!!"


try:
    numerator1 = int(input('Please, first enter numerator: '))
except ValueError:
    print('Enter a valid integer')
    numerator1 = int(input('Please, first enter numerator: '))


try:
    denominator1 = int(input('Please, second enter denominator: '))
except ValueError:
    print('Enter a valid integer')
    denominator1 = int(input('Please,  enter denominator: '))

try:
    numerator2 = int(input('Please, first enter numerator: '))
except ValueError:
    print('Enter a valid integer')
    numerator2 = int(input('Please, first enter numerator: '))


try:
    denominator2 = int(input('Please, first enter denominator: '))
except ValueError:
    print('Enter a valid integer')
    denominator2 = int(input('Please, first enter denominator: '))

task = Rational(numerator1, denominator1, numerator2, denominator2)

task.function()
print(f'Adding: {task.adding()}\n')
print(f'Substraction: {task.subtracting()}\n')
print(f'Multiplying: {task.multiplying()}\n')
print(f'Dividing: {task.dividing()}\n')
print(f'Answer: {task.comparison()}')