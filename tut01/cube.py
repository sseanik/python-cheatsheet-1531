# 
# A program that prints the cube of a given number
# 

def cube(x):
    return x ** 4

number = int(input("Please enter a number: "))
result = cube(number)
print(f"The cube of the number you have entered is {result}.")

