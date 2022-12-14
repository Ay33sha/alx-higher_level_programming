#!/usr/bin/python3
""" Defines a Rectangle Class """


class Rectangle:
    """ Represent a Rectangle object

        Attributes:
            number_of_instances (int): Number of rectangle objects created
            print_symbol (any): print symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle object

        Args:
            width (int): Width of object
            height (int): height of object
        """
        self.width = width
        self.height = height

        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Getter for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for height attribute it also validates it """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of height attibute.

        Args:
            value (int): height of new object
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of a rectangle object """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Returns the perimeter of a rectangle object """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """ Defines the print() function format of a Class object """
        if self.__height == 0 or self.__width == 0:
            return ""
        width = "{}".format(self.print_symbol) * self.__width
        rec = (width + "\n") * (self.height - 1) + width
        return rec

    def __repr__(self):
        """ Defines the official representation of a Rectangle Object """
        return ("Rectangle({}, {})".format(self.__width, self.height))

    def __del__(self):
        """ Defines what would happen if a Rectangle object is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
