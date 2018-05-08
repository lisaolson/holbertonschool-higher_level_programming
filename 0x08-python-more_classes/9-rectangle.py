class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return value

    def area(self):
        area = 0
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        perimeter = 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        new_list = []
        if self.__width == 0 or self.__height == 0:
            return ''.join(new_list).rstrip()

        for x in range(0, self.__height):
            for y in range(0, self.__width):
                if type(Rectangle.print_symbol) is list:
                    for x in Rectangle.print_symbol:
                        new_list.append(x)
                new_list.append(Rectangle.print_symbol)
            if x == len(new_list):
                return
            new_list.append('\n')
        return ''.join(new_list).rstrip()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
        if rect_1.area() == rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        width = size
        height = size
        return cls(width, height)
