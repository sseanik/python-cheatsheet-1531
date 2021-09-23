# COMP1531 21T3 F11A

## Python Cheatsheet

### Looping with Lists
```python
shopping = ["bread", "milk", "apple", "banana", "weetbix"]

# For range loop 
# (You can't do item = "something" in the loop to edit the shopping list)
for item in shopping:
    print(item)

# Traditional loop with index variable 
# (You're allowed to do shopping[i] = "something" in the loop to edit the shopping list)
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


### If Statements
```python
day = "Sunny"

# Remember code blocks are denoted by the ':' colon symbol and indentation
if day == "Sunny":
    print("Wow it is a lovely day")
elif day == "Rainy":
    print("Better bring my umbrella today")
else:
    print("I need to go check the weather")
```

### List Slicing
```python
output = [0, 1, 2, 3, 4, 5]

output[::-1] # Will reverse the list -> [5, 4, 3, 2, 1, 0]
output[2:5]  # Inclusive of 2nd index, but not 5th -> [2, 3, 4]
output[2:]   # Will include index values from 2 until the end -> [2, 3, 4, 5]
output[:4]   # Will include first 4 elements -> [0, 1, 2, 3]
output[-3:]  # Will include last 3 elements -> [3, 4, 5]
output[:99]  # Python figures out you don't have 99 elements -> [0, 1, 2, 3, 4, 5]
```

### Dictionaries
```python
# Think of dictionaries as arrays, but the 'key' can be a string/int/float

# Initialising dictionaries
tutors = dict()
tutors_alternative = {} 

# Populating a dictionary
tutors["Hayden"] = "Pretty cool" # Using a string as a key
favourite_tutor = "Sean"
tutors[favourite_tutor] = "Variable speaks for itself" # Using a variable of a string as a key
# Defining an entire dictionary
lab_assitants = {
    "Miguel": "Python genius",
    "Jake": "Brilliant at AI",
    "Sean": "He's a lab assistant as well?"
}

# You can also mix up data types in a dictionary
comp1531_teaching = {
    "tutors": ["Sean", "Yasmin", "Nick"], # A list
    "lab_assistants": lab_assitants, # A dictionary within a dictionary
    2021: "Term 3" # An integer key, with a string value
}
```

### Looping with Dictionaries
```python
comp1531_f11a_drawings = {
    "ALPACA": ["Cat", "Monkey", "Shapes", "Pickaxe", "Line"],
    "BEAGLE": ["Elephant", "Sun", "Dagger", "Sword", "Triangles"],
    "CAMEL": ["Cat", "Python", "Sheep", "Sunflower", "Cloud"],
    "DODO": ["Pencil", "Happy", "Face", "Pikachu", "Hello"],
    "EAGLE": ["Prism", "Person", "Abstract", "Wizard", "Fish"]
}

# Looping over each key -> ALPACA, BEAGLE, CAMEL, DODO, EAGLE
for key in comp1531_f11a_drawings: # comp1531_f11a_drawings.keys() is equivalent
    print(key)
    # To loop over the value given the key -> "Cat", "Monkey", "Shapes", "Pickaxe", "Line"
    for drawing in comp1531_f11a_drawings[key]:
        print(drawing)

# Looping over each value -> ["Cat", "Monkey", "Shapes", "Pickaxe", "Line"], ...
for value in comp1531_f11a_drawings.values():
    print(value) # Will print a list
    # Will loop over the list
    for drawing in value:
        print(drawing)

# Looping over key and values
for key, value in comp1531_f11a_drawings.items():
    print(f"Key: {key}, Value: {value}")

```

### Pythonic One Liners
```python
# Ternary
# List Comprehension
# Dictionary Comprehension
# Python functions e.g. join

```

### Pytest
```python
# TODO
# Markers
# Scope
# Params
```


To Add Maybe?:
* Operators, e.g. 3 * "hello"
* Printing
* Types
* Tuples
* functions
* Git? 
* Sets
* Importing + if __name__
* Packages + virtualenv
* Exceptions

