from fractions import Fraction
class Rational():
    def __init__(self, numerator=0, denominator = 1):
            
        self.__numerator = numerator
        self.__denominator = denominator


        @property
        def numerator(self):
            return self.__numerator
        
        @property
        def denominator(self):
            return self.__denominator

        @denominator.setter
        def denominator(self, new_denominator):
            if denominator == 0:
                raise ZeroDivisionError
            
            self.__denominator = new_denominator


    def function(self):
        

        result = float(eval(str(self.__numerator / self.__denominator)))
        return (f'{self.__numerator} / {self.__denominator} -->{Fraction(self.__numerator, self.__denominator)} --> {result}')
       
        



try:
    numerator = int(input('Please, enter numerator: '))
except ValueError:
    print('Enter a valid integer')
    numerator = int(input('Please, enter numerator: '))


try:
    denominator = int(input('Please, enter denominator: '))
except ValueError:
    print('Enter a valid integer')
    denominator = int(input('Please, enter denominator: '))

task = Rational(numerator, denominator)

print(task.function())
