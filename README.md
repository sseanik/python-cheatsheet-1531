Table of Contents

- [Lists](#lists)
  - [List Looping](#list-looping)
  - [List Slicing](#list-slicing)
  - [List Comprehension](#list-comprehension)
  - [List Functions](#list-functions)
  - [Extending Lists](#extending-lists)
- [Dictionaries](#dictionaries)
  - [Dictionary Initialisation](#dictionary-initialisation)
  - [Dictionary Looping](#dictionary-looping)
  - [Dictionary Comprehension](#dictionary-comprehension)
  - [Dictionary Functions](#dictionary-functions)
- [Misc Data Structures](#misc-data-structures)
  - [Sets](#sets)
  - [Tuples](#tuples)
  - [Copying](#copying)
- [Conditionals](#conditionals)
  - [If Statements](#if-statements)
  - [Conditional Expressions](#conditional-expressions)
- [Testing](#testing)
  - [Pytest](#pytest)
  - [Exceptions](#exceptions)
  - [Coverage](#coverage)
  - [Pylint](#pylint)
- [Importing & Packages](#importing--packages)
  - [Importing](#importing)
  - [Packages & Virtual Environment](#packages--virtual-environment)
- [Flask](#flask)
  - [Skeleton](#skeleton)
- [Pythonic Code](#pythonic-code)
  - [Operators](#operators)
  - [Useful One liner functions](#useful-one-liner-functions)
  - [Sorting & Lambda functions](#sorting--lambda-functions)
  - [Classes](#classes)
  - [Files](#files)
  - [Pickle](#pickle)
  - [Reduce, map, filter](#reduce-map-filter)
  - [Decorators](#decorators)

## Lists

### List Looping

What are the different ways we can loop through a list? Take note of situations where you want to edit the list directly in the loop.

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
    print(f"Index: {i}, Item: {item}")

# While loops
i = 0
while i < len(shopping):
    print(shopping[i])
    i += 1 # There's no i++ in Python
```

### List Slicing

A powerful extension on 'indexing' a list where we able to not just index a list and extract a value, but have a potential 'range' of indices to extract a sub-list or reversed (sub) list.

```python
output = [0, 1, 2, 3, 4, 5]

output[-1]   # Will retrieve the last element -> 5
output[::-1] # Will reverse the list -> [5, 4, 3, 2, 1, 0]
output[2:5]  # Inclusive of the 2nd index, but exclusive of the 5th index -> [2, 3, 4]
output[2:]   # Will include index values from 2 until the end -> [2, 3, 4, 5]
output[:4]   # Will include first 4 elements -> [0, 1, 2, 3]
output[-3:]  # Will include last 3 elements -> [3, 4, 5]
output[:99]  # Python figures out you don't have 99 elements -> [0, 1, 2, 3, 4, 5]
```

### List Comprehension

A shorthand variation of looping and creating a list. The structure of list comprehension will usually be: [**Expression** - **For Range Loop** - **Conditional**] where the conditional is optional.

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
Filtering a list with an if statement into a new list
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
Taking an expression over list elements into a list
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

### List Functions

Similar to arrays in C, except their size is dynamic and you can have  different types. **Note**: Most of these list functions return _None_ and modify the list in place (e.g. wacky*list.reverse() returns *None* and reverses the list directly).

```python
wacky_list = ["goose", "duck", True, 5, None, 4.2]

# Indexing and assigning
wacky_list[2] = False # ["goose", "duck", False, 5, None, 4.2]

# len - Extracting the element length of a list
length = len(wacky_list) # length = 6

# append - Adding a new element to the end of a list
wacky_list.append("duck") # ["goose", "duck", False, 5, None, 4.2, "Duck"]

# count - Count the occurrences of an element in a list
duck_count = wacky_list.count("duck") # duck_count = 2

# index - Retrieve the index of the first occurrences of a value
duck_index = wacky_list.index("duck") # duck_index = 1
# You can also add an optional start and end index range
duck_index = wacky_list.index("duck", 2) # duck_index = 6
duck_index = wacky_list.index("duck", 3, 6) # duck_index = 6
# NOTE: A ValueError is raised if the value is not present in the list (or in the given range)

# insert - You can insert an element at a given index, which shifts existing elements to the right
wacky_list.insert(2, "swan") # ["goose", "duck", "swan", False, 5, None, 4.2, "Duck"]

# pop - Pop will retrieve and remove a value at a given index
last_element = wacky_list.pop() # No argument will grab the last element -> "Duck"
index_element = wacky_list.pop(2) # Retrieves and removes wacky_list[2] -> "swan"
# ["goose", "duck", False, 5, None, 4.2]
# NOTE: An IndexError is raised if the list is empty, or index is out of bounds

# reverse - Reverse will mirror the list in place
wacky_list.reverse() # [4.2, None, 5, False, "duck", "goose"]

# remove - Remove the first matching element from a list
wacky_list.remove(5) # [4.2, None, False, "duck", "goose"]
# NOTE: A ValueError is raised if the element is not present in the list

# clear - Clears the list
wacky_list.clear() # wacky_list is now == []
```

### Extending Lists

What happens when we want to concatenate a list onto a list?

```python
numbers = [1, 2]
# Extend will add the string_num list to the end of the numbers list
string_nums = ["3", "4"]
numbers.extend(string_nums) # numbers == [1, 2, '3', '4']

# The += operator can be used also
tup_nums = (5.0, 6.0)
numbers += tup_nums # numbers == [1, 2, '3', '4', 5.0, 6.0]

# List slicing the end of the list can be used as well
set_nums = {7, 8, 9}
numbers[len(numbers):] = set_nums # numbers == [1, 2, '3', '4', 5.0, 6.0, 8, 9, 7]
```

## Dictionaries

### Dictionary Initialisation

Similar to structs from C, there are key value 'pairs' of potentially different data types

```python
# Initialising a dictionary
tutors = dict()
tutors_alternative = {}

# Populating a dictionary
tutors["Yasmin"] = "W17A" # Using a string as a key (Key is "Yasmin", value is "W17A")
fav_tutor = "Sean"
tutors[fav_tutor] = "F11A" # Using a variable of a string as a key

# Defining an entire dictionary
lab_assistants = {"Miguel": "F11A", "Sean": "W17A"}

# You can also mix up data types in a dictionary
comp1531_teaching = {
    "tutors": ["Sean", "Yasmin", "Nick"], # A string key and list value
    "lab_assistants": lab_assistants, # A string key and a value of a dictionary
    2021: True, # An integer key, with a boolean value
    1.5: None # A float key, with a None value
}
```

### Dictionary Looping

When looping through dictionaries we need to be aware of both the key and/or value.

```python
comp1531_f11a_class = {
    "Groups": ["ALPACA", "BEAGLE", "CAMEL", "DODO", "EAGLE"],
    "Team Names": ["Throne Trouble", "Celery Creature", "Pig Partner", "Sun Surprise", "Waste Wish"],
    "Tutors": ["Sean", "Miguel"]
}

# Looping over each key -> "Groups", "Team Names", "Tutors"
for key in comp1531_f11a_class.keys(): # Removing .keys() is equivalent
    print(key)
    # You can access the values with the key
    for value in comp1531_f11a_class[key]:
        print(value)

# Looping over each value -> ["ALPACA", "BEAGLE", ...], ["Throne Trouble", "Celery Creature", ...], ...
for value in comp1531_f11a_class.values():
    print(value)
    # Since each value of the dictionary is a list, you can loop over the individual list elements too
    for value in value:
        print(value)

# Looping over both key and values
for key, value in comp1531_f11a_class.items():
    print(f"Key: {key}, Value: {value}")
```

### Dictionary Comprehension

Similar to list comprehension, but we need to make sure we define the **key** and **value**

```python
'''
Performing operations on a list to create a dictionary
'''
squares = dict()
# Method 1
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    squares[num] = num * num

# Method 2
squares = {num: num * num for num in numbers}

'''
Transforming a dictionary
'''
usd_prices = {'chair': 250, 'desk': 399, 'monitor': 549.99, 'pc': 2000.00}
usd_to_aud = 1.35
# Method 1
aud_prices = {}
for key, value in usd_prices:
    aud_prices[key] = value * usd_prices

# Method 2
aud_prices = {key: value * usd_to_aud for key, value in usd_prices.items()}

'''
Conditionals in dictionary comprehension
'''
marks = {'Sean': 86, 'Austin': 90, 'Stella': 67, 'Lachlan': 82}
# Method 1
hd_marks = dict()
for key in marks:
    if marks[key] >= 85:
        hd_marks[key] = marks[key]

# Method 2
hd_marks = {key: value for key, value in marks.items() if value >= 85}
```

### Dictionary Functions

```python
fruits = {"apple": 5, "orange": 4, "pear": 3, "lemon": 1}

# Gather a view object of the dictionary's keys, values or both
fruits.keys() # dict_keys(['apple', 'orange', 'pear', 'lemon'])
fruits.values() # dict_values([5, 4, 3, 1])
fruits.items() # dict_items([('apple', 5), ('orange', 4), ('pear', 3), ('lemon', 1)])

# Returns the value using a specified key
fruits.get("apple") # 5
fruits.get("watermelon") # None

# Adds or updates an existing key value pair
fruits.update({"watermelon": 1}) # Adds
fruits.update({"apple": 6}) # Changes existing
fruits.update(orange=5) # # Changes existing

# Removes and returns an element
# Before: {'apple': 6, 'orange': 5, 'pear': 3, 'lemon': 1, 'watermelon': 1}
fruits.pop("apple") # 5
# After: {'orange': 5, 'pear': 3, 'lemon': 1, 'watermelon': 1}

# Removes and returns the last element of a dictionary
fruits.popitem() # ('watermelon', 1)
# After: {'orange': 5, 'pear': 3, 'lemon': 1}

# Return a value from a dictionary given the key, otherwise insert a new key and/or value
fruits.setdefault("orange") # 5
fruits.setdefault("apple", 4) # 4
# After: {'orange': 5, 'pear': 3, 'lemon': 1, 'apple': 4}

# Create a new dictionary based on a provided sequence (key, default value)
name = dict.fromkeys({'s', 'e', 'a', 'n'}) # {'s': None, 'e': None, 'a': None, 'n': None}
vowels = dict.fromkeys({'a', 'e', 'i', 'o', 'u'}, 'vowel') # {'a': 'vowel', 'u': 'vowel', 'o': 'vowel', 'e': 'vowel', 'i': 'vowel'}

# Clear the dictionary
fruits.clear() # fruits == {}
```

## Misc Data Structures

### Sets

```python
# TODO
```

### Tuples

```python
# TODO
```

### Copying

When copying nested data structures, we need to be wary that `.copy()` will handle nested data as pointers. The way to solve this is to use `deepcopy()` from the copy library.

```python
# If you have a single layer list of non-container values, you don't need to worry about references
colours = ['red', 'green', 'blue']
colours_copy = colours.copy()

# Perform a shallow copy (it will copy each sub list as a reference/pointer)
shallow_a = [['r', 'g', 'b'], ['c', 'm', 'y', 'k']]
shallow_b = shallow_a.copy()
shallow_a[0][0] = 'Red' # Will update both shallow_a and shallow_b
# shallow_b == [['Red', 'g', 'b'], ['c', 'm', 'y', 'k']]
shallow_b[0][1] = "Green" # Will update both shallow_b and shallow_a
# shallow_a == [['Red', 'Green, 'b'], ['c', 'm', 'y', 'k']]

# Perform a deep copy
import copy
deep_a = [['r', 'g', 'b'], ['c', 'm', 'y', 'k']]
# Perform a deep copy (it will copy each sub list as unique elements not references)
deep_b =  copy.deepcopy(deep_a)
deep_a[0][0] = 'Red' # Will update only deep_a
deep_b[0][1] = "Green" # Will update only deep_b
# deep_a == [['Red', 'g, 'b'], ['c', 'm', 'y', 'k']]
# deep_b == [['r', 'Green, 'b'], ['c', 'm', 'y', 'k']]
```

## Conditionals

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

# Long If Statements with backslash
# Note: Can potentially result in bad alignment and no trailing space or comment after '\' allowed
if weather == "Sunny" or weather == "Windy" or weather == "Cloudy" or \
    weather == "Rainy":
    print("Weather is very weathery today")
```

### Conditional Expressions

Conditional Expressions (sometimes known as Ternary Operators) allow us to combine a singular if and else statement into one line.

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

## Testing

### Pytest

```python
# TODO
# simple reusable
# Markers
# Scope
# Params
# Mark
```

### Exceptions

```python
# TODO
# types of exceptions
# try/except
```

### Coverage

```python
# TODO
```

### Pylint

```python
# TODO
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
# pip3
# requirements.txt
```

## Flask

### Skeleton

```python
# TODO
```

## Pythonic Code

### Operators

```python
# TODO
# 3 * 'goose'
# Printing decimal places
```

### Useful One liner functions

```python
# Python functions e.g. join
# any
# all
# types
```

### Sorting & Lambda functions

```python
# TODO
# sorting
# reverse sorting
# sorting dictionaries based on key/value
```

### Classes

```python
# TODO
```

### Files

```python
# TODO
```

### Pickle

```python
# TODO
```

### Reduce, map, filter

```python
# TODO
```

### Decorators

```python
# TODO
```
