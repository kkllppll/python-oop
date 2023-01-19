class Rectangle():
    def __init__(self, length = 1, width = 1):
        self.length = length
        self.width = width

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length


    @width.setter
    def width(self, new_width):
        if new_width <= 0 or new_width > 20:
            print("Width is not in range from 0.00 to 20.00")
        self._width = new_width

    @length.setter
    def length(self, new_length):
        if new_length <= 0 or new_length > 20:
           print("Length is not in range from 0.00 to 20.00")
        self._length = new_length


    def perimeter(self):
        return str(2 * (self.length + self.width))

    def area(self):
        return str(self.length * self.width)


try:
    length = float(input('Please, enter Length: '))
    print(length)
except ValueError:
    print('Enter a valid float')
    length = float(input('Please, enter Length: '))


try:
    width = float(input('Please, enter Width: '))
    print(width)
except ValueError:
    print('Enter a valid float')
    width = float(input('Please, enter Width: '))

rectangle = Rectangle(length, width)

print("The Area: ", rectangle.area())
print("The Perimeter: ", rectangle.perimeter())

