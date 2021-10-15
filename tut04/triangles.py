from my_math_library import Triangle, my_angle_finder

shape = Triangle("Blue", 4, 5, 6)

# How many sides does the triangle have?
print(shape.NUM_SIDES)

# What is the area of the triangle?
print(shape.area())

# What is the perimeter of the triangle?
print(shape.perimeter())

# Find the angle between the side of length 5 and 3.
print(my_angle_finder(adjacent=3, hypotenuse=5))

shape.colour = "Red"

shape.colour
