# Python Cheatsheet for COMP1531 21T3 F11A

- [Table of Contents](#table-of-contents)
    * [Data Structures](#data-structures)
        + [Looping with Lists](#looping-with-lists)
        + [List Slicing](#list-slicing)
        + [Dictionaries](#dictionaries)
        + [Looping with Dictionaries](#looping-with-dictionaries)
        + [Sets](#sets)
        + [Tuples](#tuples)
    * [Pythonic Code/Style](#pythonic-code-style)
        * [Operators](#operators)
        + [If Statements](#if-statements)
        + [List/Dictionary Comprehension](#list-dictionary-comprehension)
        + [One liner functions](#one-liner-functions)
    * [Testing](#testing)
        + [Pytest](#pytest)
        + [Exceptions](#exceptions)
    * [Importing & Packages](#importing---packages)
        + [Importing](#importing)

## Data Structures

### Lists - Looping
Similar to arrays in C, except their size is dynamic and can have potentially different types e.g. ["goose", "duck", True, 5, None, 4.2]
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
A powerful extension on 'indexing' an array/list
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

### Dictionary - Looping
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
```

### If Statements
```python
weather = "Sunny"

# Remember code blocks are denoted by the ':' colon symbol and indentation
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

### List/Dictionary Comprehension
```python
# Ternary
# List Comprehension
# Dictionary Comprehension
```

### Useful One liner functions
```python
# Python functions e.g. join
# any
# types
```

## Testing

### Pytest
```python
# TODO
# Markers
# Scope
# Params
```

### Exceptions
```python
# TODO
```

## Importing & Packages

### Importing
```python
# TODO
# if __name__ == "__main__"
```

### Packages & virtualenv
```python
# TODO
```