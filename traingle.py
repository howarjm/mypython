def area(base, height):
        '''(number, number) -> number

        Return the area of a traingle with given base and height.

        >>> area(10, 40)
        200.0
        >>> area(3.4, 7.5)
        12.75
        '''
        
        return base * height / 2

def perimeter(side1, side2, side3):
        '''(number, number, number) -> number

        Return the perimeter of a traingle with sides of length
        side1, side2, side3

        >>> perimeter(3, 4, 5)
        12
        >>> perimeter(10.5, 6, 9.3)
        25.8
        '''
        
        return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
        '''(number, number, number) -> number

        Return the semiperimeter of a traingle with sides of length
        side1, side2, side3

        >>> perimeter(3, 4, 5)
        6.9
        >>> perimeter(10.5, 6, 9.3)
        12.9
        '''
        
        return perimeter(side1, side2, side3) / 2
