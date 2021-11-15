class Point:
    def __init__(self, x_arg, y_arg):
        '''
        Initialises the point with the given co-ordinates
        '''
        self.x = x_arg
        self.y = y_arg

    def get_coords(self):
        '''
        Returns the co-ordinates as a tuple
        '''
        return (self.x, self.y)

    def set_x(self, x):
        '''
        Sets the x co-ordinate
        '''
        self.x = x

    def set_y(self, y):
        '''
        Sets the y co-ordinate
        '''
        self.y = y

    def __add__(self, point):
        '''
        Returns a new point which is the vector addition of this point,
        and the point given.

        Both this point and the point given remain unchanged.
        '''
        return Point(self.x + point.x, self.y + point.y)

    def __mul__(self, scalar):
        '''
        Returns a new point which is the scalar multiplication of this point and
        the given value.

        This point remains unchanged.
        '''
        return Point(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"The point has x = {self.x} and y = {self.y}"


if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(2, 3)

    p3 = p1 + p2
    p4 = p1 * 3

    print(p1.get_coords(), p2.get_coords(), p3.get_coords(), p4.get_coords())
    print(p1)


