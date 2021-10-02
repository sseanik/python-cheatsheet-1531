# Python Cheatsheet

Brought to you by COMP1531 tutors Sean Smith and Miguel Guthridge, and the [F11A COMP1531 Class of 21T3](drawing.png).

## Table of Contents

* [Data Structures](#data-structures)
    + [Lists](#lists)
    + [List Looping](#list-looping)
    + [List Slicing](#list-slicing)
    + [Dictionaries](#dictionaries)
    + [Dictionary Looping](#dictionary-looping)
    + [Sets](#sets)
    + [Tuples](#tuples)
* [Pythonic Code](#pythonic-code)
    * [Operators](#operators)
    + [If Statements](#if-statements)
    + [List/Dictionary Comprehension](#listdictionary-comprehension)
    + [Useful One liner functions](#useful-one-liner-functions)
    + [Sorting & Lambda functions](#sorting---lambda-functions)
* [Testing](#testing)
    + [Pytest](#pytest)
    + [Exceptions](#exceptions)
* [Importing & Packages](#importing---packages)
    + [Importing](#importing)
    + [Packages](#packages)
    + [Virtual Environment](#virtual-environment)


## Data Structures

### Lists
Similar to arrays in C, except their size is dynamic and you can have potentially different types. In these examples, if I do not assign an example to a variable, it is because function returns None (e.g. wacky_types.reverse() returns a None as it reverses the list in place, so no need to assign it to a variable).
```python
wacky_types = ["goose", "duck", True, 5, None, 4.2]

# Indexing and assigning
wacky_types[2] = False # ["goose", "duck", False, 5, None, 4.2]

# Extracting the element length of a list
length = len(wacky_types) # length = 6

# Adding to the end of a list
wacky_types.append("duck") # ["goose", "duck", False, 5, None, 4.2, "Duck"]

# Count the occurances in a list
duck_count = wacky_types.count("duck") # duck_count = 2

# Retrieve the index of the first occurance of a value
duck_index = wacky_types.index("duck") # duck_index = 1
# You can also add an optional start and end index range
duck_index = wacky_types.index("duck", 2) # duck_index = 6
duck_index = wacky_types.index("duck", 3, 6) # duck_index = 6
# Note: A ValueError is raised if the value is not present in the list (or in the given range)

# You can insert a value at a given index, which shifts values to the right
wacky_types.insert(2, "swan") # ["goose", "duck", "swan", False, 5, None, 4.2, "Duck"]

# Pop will remove and return a value at a given index
last_element = wacky_types.pop() # No arguments, will take the last element -> "Duck"
print(wack_types) # ["goose", "duck", "swan", False, 5, None, 4.2]
index_element = wacky_types.pop(2) # Removes and returns wacky_types[2] -> "swan"
print(wack_types) # ["goose", "duck", False, 5, None, 4.2]
# Note: An IndexError is raised if the list is empty, or index is out of bounds

# Reverse will mirror the list in place (it returns None)
wacky_types.reverse() # [4.2, None, 5, False, "duck", "goose"]

# Remove the first matching element from a list
wacky_types.remove(5) # # [4.2, None, False, "duck", "goose"]
# Note: A ValueError is raised if the element is not present in the list

# extend

# Empties the list
wacky_types.clear() # wacky_types is now == []
```

### List Looping
```python
shopping = ["bread", "milk", "apple", "banana", "weetbix"]

# For range loop (You CANNOT edit the shopping list directly with item = "Goose" in the loop)
for item in shopping:
    print(item)

# Traditional loop with index variable (You CAN edit the shopping list directly with shopping[i] = "Goose")
for i in range(len(shopping)):
    print(shopping[i])

# Loop with both the index and element available
for i, item in enumerate(shopping):
    print(f"Item: {item}, Index: {i}")

# While loops
i = 0
while i < len(shopping):
    print(shopping[i])
    i += 1 # There's no i++ in Python
```

### List Slicing
A powerful extension on 'indexing' a list
```python
output = [0, 1, 2, 3, 4, 5]

output[-1]   # Will retrive the last element -> 5
output[::-1] # Will reverse the list -> [5, 4, 3, 2, 1, 0]
output[2:5]  # Inclusive of 2nd index, but exclusive of the 5th index -> [2, 3, 4]
output[2:]   # Will include index values from 2 until the end -> [2, 3, 4, 5]
output[:4]   # Will include first 4 elements -> [0, 1, 2, 3]
output[-3:]  # Will include last 3 elements -> [3, 4, 5]
output[:99]  # Python figures out you don't have 99 elements -> [0, 1, 2, 3, 4, 5]
```

### Dictionaries
Similar to structs from C, there are key value 'pairs' of (potentially) different data types
```python
# Initialising a dictionary
tutors = dict()
tutors_alternative = {} 

# Populating a dictionary
tutors["Hayden"] = "Pretty cool" # Using a string as a key (Key is "Hayden", value is "Pretty cool")
favourite_tutor = "Sean"
tutors[favourite_tutor] = "Variable speaks for itself" # Using a variable of a string as a key

# Defining an entire dictionary
lab_assitants = {
    "Miguel": "Python genius", # Notice the commas
    "Jake": "Brilliant at AI",
    "Sean": "He's a lab assistant as well?"
}

# You can also mix up data types in a dictionary
comp1531_teaching = {
    "tutors": ["Sean", "Yasmin", "Nick"], # A string key and list value 
    "lab_assistants": lab_assitants, # A string key and a value of a dictionary
    2021: True, # An integer key, with a boolean value
    1.5: None # A float key, with a None value
}
```

### Dictionary functions
```python
# clear()
# copy()
# fromkeys()
# get()
# items()
# keys()
# pop()
# popitem()
# setdefault()
# update()
# values()
```

### Dictionary Looping
Looping through dictionaries we need to be aware of both the key and/or value.
```python
comp1531_f11a_drawings = {
    "ALPACA": ["Cat", "Monkey", "Shapes", "Pickaxe", "Line"],
    "BEAGLE": ["Elephant", "Sun", "Dagger", "Sword", "Triangles"],
    "CAMEL": ["Cat", "Python", "Sheep", "Sunflower", "Cloud"],
    "DODO": ["Pencil", "Happy", "Face", "Pikachu", "Hello"],
    "EAGLE": ["Prism", "Person", "Abstract", "Wizard", "Fish"]
}

# Looping over each key -> ALPACA, BEAGLE, CAMEL, DODO, EAGLE
for key in comp1531_f11a_drawings.keys(): # Removing .keys() is equivalent
    print(key)
    # You can access the values with the key
    for drawing in comp1531_f11a_drawings[key]:
        print(drawing)

# Looping over each value -> ["Cat", "Monkey"...], ["Elephant", "Sun"...], ...
for value in comp1531_f11a_drawings.values():
    print(value)
    # Since each value of the dictionary is a list, you can loop over the individual list elements too
    for drawing in value:
        print(drawing)

# Looping over both key and values
for key, value in comp1531_f11a_drawings.items():
    print(f"Key: {key}, Value: {value}")
```

### Sets
```python
# TODO
```

### Tuples
```python
# TODO
```

## Pythonic Code

## Operators
```python
# TODO
# 3 * 'goose'
```

### If Statements
Remember code blocks in python denoted by the ':' colon symbol and using indentation
```python
weather = "Sunny"

if weather == "Sunny":
    print("Wow it is a lovely day")
elif weather == "Rainy":
    print("Better bring my umbrella today")
else:
    print("I need to go check the weather")

# Long If Statements with brackets (Recommended)
if (weather == "Sunny" or weather == "Windy" or weather == "Cloudy" or # You can even put a comment here
    weather == "Rainy"):
    print("Weather is very weathery today")

# Long If Statements with backslash (Not recommended)
# Why? Potentially bad alignment and no trailing space or comment after '\' allowed
if weather == "Sunny" or weather == "Windy" or weather == "Cloudy" or \
    weather == "Rainy":
    print("Weather is very weathery today")
```

### Ternary Operators
Ternary Operators allow us to combine a singular if and else statement into one line.
```python
lost_headphones = True
# Returning Method 1 (Non-ternary)
if lost_headphones:
    return "Where are they?"
else:
    return "In your pocket"
# Returning Method 2 (Ternary)
return "Where are they?" if lost_headphones else "In your pocket"

hand = [1, 7, "Jack", "King"]
# Assigning Method 1 (Non-ternary)
if "Queen" in hand:
    win = True
else:
    win = False
# Assigning Method 2 (Ternary)
win = True if "Queen" in hand else False
```

### List Comprehension
The structure of list comprehension will usually be [EXPRESSION - FOR RANGE LOOP - CONDITIONAL]
```python
'''
Copying a list
'''
pokedex = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]
# Method 1 - For range loop and append
pokedex_copy = []
for pokemon in pokedex:
    pokedex_copy.append(pokemon)
# Method 2 - Basic List Comprehension
pokedex_copy = [pokemon for pokemon in pokedex]

'''
Filtering a list into a new list
'''
cards = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, "Jack", "Queen", "King"]
# Method 1 - For range loop with an if statement
royal_cards = []
for card in cards:
    if isinstance(card, str):
        royal_cards.append(card)
# Method 2 - Conditional List Comprehension
royal_cards = [card for card in cards if isinstance(card, str)]

'''
Manipulating list elements into a new list
'''
numbers = [1, 2, 3, 4, 5]
# Method 1 - For range loop with an expression
squares = []
for num in numbers:
    squares.append(num * num)
# Method 2 - Expression inside List Comprehension
squares = [(num * num) for num in numbers]

'''
Combining Expression and Conditionals
'''
numbers = [1, 2, 3, 4, 5]
# Method 1 - For range loop with an expression
even_squares = []
for num in numbers:
    if num % 2 == 0:
        squares.append(num * num)
# Method 2 - Expression inside List Comprehension
even_squares = [(num * num) for num in numbers if num % 2 == 0]
```

### Dictionary Comprehension
```python
# TODO
```

### Useful One liner functions
```python
# Python functions e.g. join
# any
# types
```

### Copying
```python
# Performs a shallow copy (i.e. if you change wacky_types, it)
wacky_copy = wacky_types.copy()
```

### Sorting & Lambda functions
```python
# TODO
# sorting
# reverse sorting
# sorting dictionaries based on key/value
```

## Testing

### Pytest
```python
# TODO
# simple reusable
# Markers
# Scope
# Params
```

### Exceptions
```python
# TODO
# types of exceptions
```

## Importing & Packages

### Importing
```python
# TODO
# types of imports
# if __name__ == "__main__"
```

### Packages & Virtual Environment
```python
# TODO
# requirements.txt
```