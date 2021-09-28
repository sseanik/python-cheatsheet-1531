# What does it do? -> Doubles even numbers
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Normal loop, if/else, append method
result = []
for num in integers:
    if num % 2 == 0:
        result.append(num * 2)
    else:
        result.append(num)

# List comprehension one line solution
result_alt = [(num * 2 if num % 2 == 0 else num) for num in integers]

print(result)
print(result_alt)
