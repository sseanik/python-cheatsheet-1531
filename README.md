Python Cheatsheet

- [Lists](#lists)
  - [List Looping](#list-looping)
  - [List Slicing](#list-slicing)
  - [List Comprehension](#list-comprehension)
  - [List Functions](#list-functions)
- [Dictionaries](#dictionaries)
  - [Dictionary Initialisation](#dictionary-initialisation)
  - [Dictionary Looping](#dictionary-looping)
  - [Dictionary Comprehension](#dictionary-comprehension)
  - [Dictionary Functions](#dictionary-functions)
- [Sets & Tuples](#sets--tuples)
  - [Set Functions](#set-functions)
  - [Set Operations](#set-operations)
  - [Tuples](#tuples)
- [Conditionals](#conditionals)
  - [If Statements](#if-statements)
  - [Conditional Expressions](#conditional-expressions)
- [Testing](#testing)
  - [Pytest](#pytest)
  - [Exceptions](#exceptions)
  - [Pylint](#pylint)
  - [Coverage](#coverage)
  - [Property Based Testing](#property-based-testing)
- [Flask](#flask)
  - [CRUD Example](#crud-example)
  - [HTTP Testing](#http-testing)
- [Sorting & Lambda Functions](#sorting--lambda-functions)
  - [Sorting](#sorting)
  - [Lambda Functions](#lambda-functions)
  - [Sorting using Lambda functions](#sorting-using-lambda-functions)
  - [Filter](#filter)
  - [Map](#map)
  - [Reduce](#reduce)
- [Importing & Packages](#importing--packages)
  - [Importing](#importing)
  - [Packages & Virtual Environments](#packages--virtual-environments)
- [Miscellaneous Python](#miscellaneous-python)
  - [String Manipulation](#string-manipulation)
  - [Any & All](#any--all)
  - [Shallow & Deep Copying](#shallow--deep-copying)
  - [Files](#files)
  - [Decorators](#decorators)
  - [Docstrings](#docstrings)
  - [Types](#types)
  - [Type Hinting](#type-hinting)
  - [Classes](#classes)

## Lists

### List Looping

What are the different ways we can loop through a list? Take note of situations where you want to mutate (edit) the list directly inside the loop.

```python
shopping = ["bread", "milk", "apple", "banana", "weetbix"]

# For range loop (You CANNOT edit the shopping list directly with item = "Goose" in the loop)
for item in shopping:
    print(item)

# Traditional loop with index variable (You CAN edit the shopping list directly with shopping[i] = "Goose")
for i in range(len(shopping)):
    print(shopping[i])

# Loop with both the index and list element available
for i, item in enumerate(shopping):
    print(f"Index: {i}, Item: {item}")

# While loops
i = 0
while i < len(shopping):
    print(shopping[i])
    i += 1 # There's no i++ in Python
```

### List Slicing

An extension on 'indexing' a list where we able to not just index, but provide a potential 'range' of indices to extract a sub-list or potentially reversed (sub) list.

```python
output = [0, 1, 2, 3, 4, 5]

output[-1]   # The last element -> 5
output[::-1] # Reverse copy of the list -> [5, 4, 3, 2, 1, 0]
output[2:5]  # Inclusive of the 2nd index, but exclusive of the 5th index -> [2, 3, 4]
output[2:]   # Index values from 2 until the end -> [2, 3, 4, 5]
output[:4]   # First 4 elements -> [0, 1, 2, 3]
output[-3:]  # Last 3 elements -> [3, 4, 5]
output[:99]  # Python figures out you don't have 99 elements -> [0, 1, 2, 3, 4, 5]
```

### List Comprehension

A shorthand variation of looping and creating a list. The structure of list comprehension will usually be: `[Expression - For Range Loop - Conditional]` where the conditional is optional.

**Copying a list**
```python
pokedex = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]

# Method 1 - For range loop and append
pokedex_copy = []
for pokemon in pokedex:
    pokedex_copy.append(pokemon)

# Method 2 - Basic Loop List Comprehension
pokedex_copy = [pokemon for pokemon in pokedex]
```
**Filtering a list with an if statement into a new list**
```python
# Goal: ['Jack', 'Queen', 'King']
cards = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, "Jack", "Queen", "King"]

# Method 1 - For range loop with an if statement 
royal_cards = []
for card in cards:
    if isinstance(card, str):
        royal_cards.append(card)

# Method 2 - Conditional List Comprehension
royal_cards = [card for card in cards if isinstance(card, str)]
```
**Evaluating an expression over list elements into a list**
```python
# Goal: [1, 4, 9, 16, 25]
numbers = [1, 2, 3, 4, 5]

# Method 1 - For range loop with an expression
squares = []
for num in numbers:
    squares.append(num * num)

# Method 2 - Expression inside List Comprehension
squares = [(num * num) for num in numbers]
```
**Combining Expression and Conditionals**
```python
# Goal: [4, 16]
numbers = [1, 2, 3, 4, 5]

# Method 1 - For range loop with an expression and if statement
even_squares = []
for num in numbers:
    if num % 2 == 0:
        even_squares.append(num * num)

# Method 2 - Expression inside List Comprehension with conditional
even_squares = [(num * num) for num in numbers if num % 2 == 0]
```

### List Functions

Similar to arrays in C, except their size is dynamic and you can have  different types (not recommended, use tuples instead). 

**Note**: Most of these list functions return _None_ and modify the list in place (e.g. wacky_list.reverse() returns *None* and reverses the list directly).

**Gathering numeric attributes from a list (e.g. length, index)**
```python
birds = ["goose", "duck", "penguin", "hawk", "duck"]

# Indexing
birds[3] # "hawk"

# Extracting the element length of a list
len(birds) # 5

# Count the occurrences of an element in a list
birds.count("duck") # 2

# Retrieve the index of the first occurrences of a value
birds.index("duck") #  1
# You can also add an optional start and end index range
birds.index("duck", 2) # 4
birds.index("duck", 3, 5) # 4
# NOTE: A ValueError is raised if the value is not present in the list (or in the given range)
```
**Altering a list**
```python
colours = ["red", "green", "blue"]

# Indexing and assigning
colours[1] = "orange" # colours == ["red", "orange", "blue"]

# Adding a new element to the end of a list
colours.append("yellow") # colours == ["red", "orange", "blue", "yellow"]

# You can insert an element at a given index, which shifts existing elements to the right
colours.insert(2, "brown") # colours == ['red', 'orange', 'brown', 'blue', 'yellow']

# Reverse will mirror the list in place
colours.reverse() # colours == ['yellow', 'blue', 'brown', 'orange', 'red']
```
**Removing elements from a list**
```python
nums = [1.1, 2.2, 3.3, 4.4, 1.1, 5.5]

# Pop will retrieve and remove a value at a given index
nums.pop() # The last element -> 5.5 
# nums == [1.1, 2.2, 3.3, 4.4, 1.1]
nums.pop(2) # Formally nums[2] -> 3.3
# nums == [1.1, 2.2, 4.4, 1.1]
# NOTE: An IndexError is raised if the list is empty, or index is out of bounds

# Remove the first matching element from the list
nums.remove(1.1) # nums == [2.2, 4.4, 1.1]
# NOTE: A ValueError is raised if the element is not present in the list

# Emptying the list
nums.clear() # nums == []
```

**Extending Lists**

```python
numbers = [1, 2]

# Extend will add the string_num list to the end of the numbers list
string_nums = ["3", "4"]
numbers.extend(string_nums) # numbers == [1, 2, '3', '4']

# The += operator can be used also
tuple_nums = (5.0, 6.0)
numbers += tuple_nums # numbers == [1, 2, '3', '4', 5.0, 6.0]

# List slicing the end of the list can be used as well
set_nums = {7, 8, 9}
numbers[len(numbers):] = set_nums # numbers == [1, 2, '3', '4', 5.0, 6.0, 8, 9, 7]
```

## Dictionaries

### Dictionary Initialisation

Similar to structs from C, Dictionaries are basically a collection key value 'pairs' of (potentially different) data types.

```python
# Initialising a dictionary
tutors = dict()
tutors_alternative = {}

# Populating a dictionary
tutors["Yasmin"] = "W17A" # Using a string as a key (Key is "Yasmin", value is "W17A")
fav_tutor = "Sean"
tutors[fav_tutor] = "F11A" # Using a variable of a string as a key
# tutors == {'Yasmin': 'W17A', 'Sean': 'F11A'}

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
**Creating a new Dictionary based on other data structures**
```python
# Create a new dictionary based on a provided sequence (key, default value)
name = dict.fromkeys({'s', 'e', 'a', 'n'}) 
# name == {'n': None, 's': None, 'e': None, 'a': None}
vowels = dict.fromkeys({'a', 'e', 'i', 'o', 'u'}, 'vowel') 
# vowels == {'o': 'vowel', 'e': 'vowel', 'u': 'vowel', 'a': 'vowel', 'i': 'vowel'}

# Create a dictionary based on corresponding lists of keys and values
nums = ['one', 'two', 'three']
digits = [1, 2, 3]
key_values = dict(zip(nums, digits)) # {'one': 1, 'two': 2, 'three': 3}
```

### Dictionary Looping

When we loop through dictionaries we need to be aware of if we want to loop over the keys, values or both.

```python
comp1531_f11a_class = {
    "Groups": ["ALPACA", "BEAGLE", "CAMEL", "DODO", "EAGLE"],
    "Team Names": ["Abra", "Bulbasaur", "Charmander", "Dratini", "Eevee"],
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

Similar to list comprehension, but we need to make sure we define the **key** and **value** with a `key: value` syntax in the expression.

**Performing operations on a list to create a dictionary**
```python
# Goal: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

# Method 1
squares = dict()
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    squares[num] = num * num

# Method 2
squares = {num: num * num for num in numbers}
```
**Transforming a dictionary**
```python
# Goal: {'chair': 337.5, 'desk': 538.65, 'monitor': 742.49, 'pc': 2700.0}
usd_prices = {'chair': 250, 'desk': 399, 'monitor': 549.99, 'pc': 2000.00}

usd_to_aud = 1.35
# Method 1
aud_prices = {}
for key, value in usd_prices.items():
    aud_prices[key] = round(value * usd_to_aud, 2)

# Method 2
aud_prices = {key: round(value * usd_to_aud, 2) for key, value in usd_prices.items()}
```
**Conditionals in dictionary comprehension**
```python
# Goal: {'Sean': 86, 'Austin': 90}}
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

There are several dictionary functions that help to extract specific data from a dictionary or even manipulate it.

**Extracting elements from a dictionary**
```python
fruits = {"apple": 5, "orange": 4, "pear": 3, "lemon": 1}

# Gather a view object of the dictionary's keys, values or both
fruits.keys() # dict_keys(['apple', 'orange', 'pear', 'lemon'])
fruits.values() # dict_values([5, 4, 3, 1])
fruits.items() # dict_items([('apple', 5), ('orange', 4), ('pear', 3), ('lemon', 1)])

# Returns the value using a specified key
fruits.get("apple") # 5
fruits.get("watermelon") # None
```
**Altering a Dictionary**
```python
prices = {"watch": 60, "necklace": 40, "earrings": 30, "ring": 90}

# Adds or updates an existing key value pair
prices.update({"sunglasses": 10}) # prices == {"watch": 60, "necklace": 40, "earrings": 30, "ring": 90, "sunglasses": 10}
prices.update({"watch": 65}) # prices == {"watch": 65, "necklace": 40, "earrings": 30, "ring": 90, "sunglasses": 10}
prices.update(ring=80) # prices == {"watch": 65, "necklace": 40, "earrings": 30, "ring": 80, "sunglasses": 10}

# Return a value from a dictionary given the key, otherwise insert a new key and/or value
prices.setdefault("necklace") # 40
prices.setdefault("hat", 10) # 10
# prices == {"watch": 65, "necklace": 40, "earrings": 30, "ring": 80, "sunglasses": 10, "hat": 10}
```
**Removing elements from a dictionary**
```python
cart = {"bread": 3.5, "tomato sauce": 4.5, "beer": 7.95, "steak": 10.0}

# Removes and returns an element
cart.pop("beer") # 7.95
# cart == {"bread": 3.5, "tomato sauce": 4.5, "steak": 10.0}

# Removes and returns the last element of a dictionary
cart.popitem() # ('steak', 10.0)
# cart == {"bread": 3.5, "tomato sauce": 4.5}

del cart["bread"] # Removes the 'orange' key and its value
# cart == {"tomato sauce": 4.5}

# Clear the dictionary
cart.clear() # cart == {}
```

## Sets & Tuples

### Set Functions

Sets are a collection of distinct elements that contain no duplicates. When you tried to add a value that already exists, it will have no effect.

**Initialising a Set**
```python
# Creating an empty set
new_set = set()

# Creating a pre-populated set
primes = {2, 3, 5, 7}

# Converting a list into a set
duplicates = ['a', 'a', 'b', 'c', 'c', 'c']
letters = set(duplicates) # {'a', 'b', 'c'}

# Create an immutable set
immutable_set = frozenset([1, 2, 3, 4])
```
**Altering a Set**
```python
digits = {1, 2, 3, 4, 5, 6}

# Adding an element to the set
digits.add(7) # digits == {1, 2, 3, 4, 5, 6, 7}
digits.add(3) # Will have no affect, a is already in the set

# Removing an element from the set
digits.remove(4) # digits == {1, 2, 3, 5, 6, 7}
digits.remove(9) # Will result in a KeyError

# Removing an element from the set if it exists
digits.discard(3) # digits == {1, 2, 5, 6, 7}
digits.discard(100) # digits == {1, 2, 5, 6, 7}

# Adding other iterables to the set
digits.update({8, 9}) # digits == {1, 2, 5, 6, 7, 8, 9}
digits.update({10}) # digits == {1, 2, 5, 6, 7, 8, 9, 10}

# Remove and return a random element from the set
digits.pop()

# Remove all elements from a set
digits.clear() # len(digits) == 0
```

### Set Operations

There are several set 'operations' (functions) that allow the calculation or transformation involving multiple sets.

**Set Operations**
```python
a = {1, 2, 3}
b = {2, 3, 4}
c = {0, 1, 2, 3, 4, 5}

# Create a new set with distinct elements from multiple sets
a.union(b) # {1, 2, 3, 4}
a | b # {1, 2, 3, 4}

# Create a new set with elements common to multiple sets
a.intersection(b) # {2, 3}
a & b # {2, 3}

# Create a new set with the difference between two sets
a.difference(b) # {1}
b.difference(a) # {4}
b - a # {4}

# Create a new set with elements from two sets that do not intersect
a.symmetric_difference(b) # {1, 4}
```
**Set Inplace Operations**
```python
a = {1.1, 2.2, 3.3}
b = {2.2, 3.3, 4.4}
c = {0.0, 1.1, 2.2, 3.3, 4.4, 5.5}

# Modifies a set inplace keeping only the common elements
c.intersection_update(a, b) # c == {2.2, 3.3}

# Modifies a set inplace removing elements from another set from it
a.difference_update(b) # a == {1.1}

# Modifies a set inplace removing elements that intersect both sets
a.symmetric_difference_update(b) # a == {1.1, 2.2, 3.3, 4.4}
```
**Set Checks**
```python
a = {'a', 'b', 'c'}
b = {'b', 'c', 'd'}
c = {'A', 'a', 'b', 'c', 'd', 'e'}

# If a is a subset of c
a.issubset(c) # True

# If c is a superset of a
c.issuperset(a) # True

# If two sets have no common elements
a.isdisjoint(b) # False
d = {9, 8, 7}
d.isdisjoint(c) # True
```

### Tuples

Compared to lists, Tuples are immutable. You cannot use item assignment or remove individual elements.

```python
# Creating an empty tuple
new_tuple = ()

# Creating a pre-populated tuple
name = ('s', 'e', 'a', 'n', 123)

# Single pre-populated tuple
single = ("sean",) # ("Sean") will equate to a string

# Indexing/slicing a tuple (same as a list)
name[0] # 's'
name[-1] # 123

# Methods
name.count('a') # 1
name.index(123) # 4
```

## Conditionals

### If Statements

Code blocks in python denoted by the ':' colon symbol and using indentation.

```python
weather = "Sunny"

if weather == "Sunny":
    print("Wow it is a lovely day") # Prints
elif weather == "Rainy":
    print("Better bring my umbrella today")
else:
    print("I need to go check the weather")

# Long If Statements with brackets (Recommended)
if (weather == "Sunny" or weather == "Windy" or weather == "Cloudy" or # You can even put a comment here
    weather == "Rainy"):
    print("Weather is very weathery today") # Prints

# Long If Statements with backslash
# Note: Can potentially result in bad alignment and no trailing space or comment after '\' allowed
if weather == "Sunny" or weather == "Windy" or weather == "Cloudy" or \
    weather == "Rainy":
    print("Weather is very weathery today") # Prints
```

### Conditional Expressions

Conditional Expressions (sometimes known as Ternary Operators) allow us to combine a singular if and else statements into one line.

**Conditional Return**
```python
lost_headphones = True

# Returning Method 1 (Non-ternary)
if lost_headphones:
    return "Where are they?"
else:
    return "In your pocket"

# Returning Method 2 (Ternary)
return "Where are they?" if lost_headphones else "In your pocket"
```
**Conditional Assign**
```python
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

Test files must have a prefix of `test_` or have a suffix of `_test`. In the test file, functions must have a prefix of `test_`. In this course we use the pytest library to help us define further testing behaviour.

```python
import pytest
from random import randint

def acronym(phrase):
    '''Given a phrase, convert and extract its acronym abbreviation'''
    if not isinstance(phrase, str):
        raise TypeError("Phrase must be a string")
    return "".join(filter(str.isupper, phrase.strip().title()))

# Fixtures are functions that run before each test and are generally used to 
# feed some data to the tests
@pytest.fixture
def random_whitespace():
    return " " * randint(1, 999)

# The parametrize decorator allows for feeding in different arguments into a test function
@pytest.mark.parametrize('phrase, abbreviation',[
    ("Sun Protection Factor", "SPF"), ("You Only Live Once", "YOLO"),
    ("National Aeronautics & Space Administration", "NASA")
])
def test_simple(phrase, abbreviation):
    assert acronym(phrase) == abbreviation

def test_whitespace(random_whitespace):
    assert acronym(f"{random_whitespace}Hello") == "H"
    assert acronym(f"World{random_whitespace}") == "W"
    assert acronym(f"{random_whitespace}Hello World{random_whitespace}") == "HW"

def test_non_capitals():
    assert acronym("sean smith") == "SS"

def test_empty(random_whitespace):
    assert acronym("") == ""
    assert acronym(random_whitespace) == ""

def test_incorrect_type():
    # We can also catch specific or non-specific (Exception) exceptions
    with pytest.raises(TypeError):
        acronym(123)
```

### Exceptions

When an exception occurs, it will stop the current process, and if not handled, will crash the program. We can handle exceptions using a `try` statement. 

**Catching Exceptions**
```python
# Try block lets you test a block of code for errors
try:
    f = open("rocketship.txt")
    number = int(input("Enter a number: "))
    calculation = 4 / number
# The except block lets you handle the error.
except ValueError:
    print("A non-numeric value was inputted")
# You can catch specific exceptions
except ZeroDivisionError:
    print("The inputted number cannot be Zero")
    
try:
   f = open("rocketship.txt")
   pass
except:
    pass
# Finally block execute codes, regardless of the result of the try, except
finally:
   f.close()
```
**Raising Exceptions**
```python
# We can manually raise exceptions too
if not isinstance(num, int):
    raise TypeError("Number is not an integer")
```

### Pylint

Pylint is a static code analysis tool for Python which attempts to point out potential errors, helps enforce a good code standard, looks for potential code smells and offers refactoring suggestions.

```python
pylint name_of_file.py # Terminal command
# You can disable certain messages in code
if year % 4 != 0: #pylint: disable=no-else-return
```

### Coverage

Coverage is a python tool for measuring code coverage of programs, generally paired with pytest. It analyses which parts code have been executed and which have not.

```bash
coverage run --source=. -m pytest # Run Coverage.py for your pytests
coverage run --branch --source=. -m pytest # Run branch coverage for your pytests
coverage report # View the coverage report
coverage html # Generate HTML to see a breakdown (puts report in htmlcov/)
```

### Property Based Testing

Property based testing (using the Hypothesis library) involves generating different data matching a specification and checking that something should be true for every case, not just ones you can think of.

*merge_sort.py*
```python
def merge_sort(array):
    if len(array) < 2:
        return array

    result = []
    middle = len(array) // 2

    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    while (len(left) > 0) and (len(right) > 0):
            if left[0] > right[0]:result.append(right.pop(0))   
            else:result.append(left.pop(0))

    result.extend(left+right)
    return result
```
*merge_sort_test.py*
```python
from hypothesis import given, strategies, Verbosity, settings

# Verbosity helps you see how Hypothesis runs your tests
@given(strategies.lists(strategies.integers()))
@settings(verbosity=Verbosity.verbose)
def test_length(nums):
    assert len(merge_sort(nums)) == len(nums)

# Provide different lists of different integers
@given(strategies.lists(strategies.integers()))
def test_sorted(nums):
    assert sorted(nums) == merge_sort(nums)
```

## Flask

### CRUD Example

Post - Creating something, Get - Reading something, Put - Updating something, Delete - Deleting something. This Flask example aims to demonstrate Create, Read, Update and Delete through different routes.

```python
from flask import Flask, request
from json import dumps

APP = Flask(__name__)

pokemon_dict = {}

# POST Request will involve creating something. Data is passed in as JSON
# e.g. {"pokemon": "Charmander", "name": "Charlie"}
@APP.route('/catch', methods=["POST"])
def catch_pokemon():
    data = request.get_json()
    pokemon, name = data["pokemon"], data["name"]
    pokemon_dict.update({pokemon: name})
    return dumps({})

# GET Request reads data and can rely on a simple route with no arguments
@APP.route('/pokedex', methods=["GET"])
def pokedex():
    return dumps(pokemon_dict)

# You can also have a variable argument
# e.g. /pokemon/Charmander
@APP.route('/pokemon/<pokemon>', methods=["GET"])
def pokemon(pokemon):
    return dumps({"name": pokemon_dict.get(pokemon)})

# You can also have a query argument
# e.g. /name?pokemon=Charmander
@APP.route('/name', methods=["GET"])
def name():
    pokemon = request.args.get('pokemon')
    return dumps({"name": pokemon_dict.get(pokemon)})

# PUT allows you to edit existing data
@APP.route('/edit', methods=["PUT"])
def edit_pokemon_name():
    data = request.get_json()
    pokemon, name = data["pokemon"], data["name"]
    pokemon_dict.update({pokemon: name})
    return dumps({})

# A DELETE request allows for the removal of data
@APP.route('/release', methods=["DELETE"])
def delete_pokemon():
    data = request.get_json()
    pokemon = data["pokemon"]
    del pokemon_dict[pokemon]
    return dumps({}) 

if __name__ == "__main__":
    # Debug allows for hot reloading when you save, the server restarts
    APP.run(debug=True)
```

### HTTP Testing

We can use the request library to send requests to an API server, and retrieve the information.

```python
import requests
import pytest

URL = "http://127.0.0.1:5000"

@pytest.fixture
def catch_starters():
    requests.delete(f"{URL}/clear")
    requests.post(
        f"{URL}/catch",
        json={
            "pokemon": "Bulbasaur",
            "name": "Bulbasaur",
        },
    )
    requests.post(
        f"{URL}/catch",
        json={
            "pokemon": "Charmander",
            "name": "Charmander",
        },
    )
    requests.post(
        f"{URL}/catch",
        json={
            "pokemon": "Squirtle",
            "name": "Squirtle",
        },
    )

def test_pokedex(catch_starters):
    response = requests.get(f"{URL}/pokedex")
    assert response.json() == {
        "Bulbasaur": "Bulbasaur",
        "Charmander": "Charmander",
        "Squirtle": "Squirtle",
    }

def test_query_string(catch_starters):
    response = requests.get(f"{URL}/pokemon/Bulbasaur")
    assert response.json() == {"name": "Bulbasaur"}

def test_get_variable(catch_starters):
    response = requests.get(f"{URL}/name?pokemon=Squirtle")
    assert response.json() == {"name": "Squirtle"}

def test_rename(catch_starters):
    requests.put(
        f"{URL}/edit",
        json={
            "pokemon": "Charmander",
            "name": "Charlie",
        },
    )
    response = requests.get(f"{URL}/pokemon/Charmander")
    assert response.json() == {"name": "Charlie"}

def test_release(catch_starters):
    requests.delete(f"{URL}/release", json={"pokemon": "Squirtle"})
    response = requests.get(f"{URL}/pokedex")
    assert response.json() == {"Bulbasaur": "Bulbasaur", "Charmander": "Charmander"}
```

## Sorting & Lambda Functions

### Sorting

There are two main sorting paradigms in Python. Sorting in place and creating a new structure with sorted elements. Note: You cannot sort a collection with non-comparable data types.

```python
nums = [4, 6, 5, 3, 99, 44]

# Return a sorted list from an existing list
sorted(nums) # [3, 4, 5, 6, 44, 99]
# Sort in Place
nums.sort() # nums == [3, 4, 5, 6, 44, 99]

# Reverse Sorting
sorted(nums, reverse=True) # [99, 44, 6, 5, 4, 3]

names = ["Blue", "Red", "Green", "Yellow"]
# Sort list based on a key (len for the len of each string)
sorted(names, key=len) # ['Red', 'Blue', 'Green', 'Yellow']
```

### Lambda Functions

Lambda functions are powerful (usually one liner) functions that allow us to simplify our code, with any number of arguments, but written as one singular expression.

```python
# Method 1 - Function
def square(x):
    return x * x
square(4) # 16

# Method 2 - Lambda function
square = lambda x: x * x
square(4) # 16
```

### Sorting using Lambda functions

The more complex the data structure we have, the more we have to give details on how the sorting comparator will give us what we want sorted.

**Sorting a dictionary**
```python
nums = {1: 'a', 3: 'b', 2: 'b', 9: 'd', 7: 'd'}
# Sorting a dictionary based on its keys
dict(sorted(nums.items())) # {1: 'a', 2: 'b', 3: 'b', 7: 'd', 9: 'd'}

# Note: in nums.items(), for each tuple, the [0] index is the key, the [1] is the value
nums.items() # [(1, 'a'), (3, 'b'), (2, 'b'), (9, 'd'), (7, 'd')]

# Sorting a dictionary based on its values (item[1] is the value)
dict(sorted(nums.items(), key=lambda item: item[1])) # {1: 'a', 3: 'b', 2: 'b', 9: 'd', 7: 'd'}

# Sorting a dictionary by values (item[1] is the value), then its keys (item[0] is the key)
dict(sorted(nums.items(), key=lambda item: (item[1], item[0])))
```
**Sorting a list of dictionaries**
```python
clothing = [
    {"name" : "Shoes" , "price" : 60},
    {"name" : "Hat", "price" : 25},
    {"name" : "Shoes", "price" : 50},
    {"name" : "Shirt" , "price" : 75}
]

# Sorts based on price
sorted(clothing, key=lambda x: x["price"]) 
# In place sorts based on Alphabetical name
clothing.sort(key=lambda x: x["name"]) 
# In place sorts based on Alphabetical name then price
clothing.sort(key=lambda x: (x["name"], x["price"])) 
```

### Filter

Filter allows us to extract elements from a collection based on a function determining each element to be `True`.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Method 1 - Using a function
def is_even(num):
    return True if num % 2 == 0 else False

even_nums = list(filter(is_even, nums)) # [2, 4, 6, 8]

# Method 2 - Using a lambda function
even_nums = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4, 6, 8]
```

### Map

Map allows us to apply a function on each element of a collection.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Method 1 - Using a function
def square(num):
    return num * num

list(map(square, nums)) # [1, 4, 9, 16, 25, 36, 49, 64]

# Method 2 - Using a lambda function
list(map(lambda x: x * x, nums)) # [1, 4, 9, 16, 25, 36, 49, 64]
```

### Reduce

Reduce applies a function to all elements of a collection, and 'reduce' it to a single value.

```python
from functools import reduce

nums = [1, 2, 3, 4]

# Method 1 - Using a function
def multiply(x, y):
    return x * y

reduce(multiply, nums) # Factorial of 4 == 24

# Method 2 - Using a lambda function
reduce(lambda x, y : x * y, nums)
```

## Importing & Packages

### Importing

When importing, you want to be careful or 'polluting' the namespace (i.e. having imported functions with the same name). You also want to be careful of circular imports (cycles in dependencies across multiple files).

**Different ways of Importing**
```python
from numpy import sqrt
sqrt(4)

from numpy import sqrt as square_root # You can rename functions
square_root(4) 

import numpy
numpy.sqrt(4)

import numpy as np # You can also rename modules
np.sqrt(4)

from numpy import * # Very bad - Don't do this
```
**'Main' Function**
```python
# Whenever you run python3 filename.py, the main function in filename.py will execute
if __name__ == "__main__":
    pass
```

### Packages & Virtual Environments

When you pip3 install, you may be install packages globally. One thing to take into account is we can use virtual environments to associate projects with specific packages, and we can further extract a requirements.txt of specific installed packages and their versions.

**Pip Commands**
```bash
pip3 install numpy # Install a new package
pip3 uninstall numpy # Remove an installed package
pip3 install --upgrade numpy # Upgrade package
```

**VirtualEnvironment Commands**
```bash
virtualenv venv # 'venv' is the name of the virtual environment (you can change it)
source venv/bin/activate # Activates the newly created virtual environment
pip3 install -r requirements.txt # Takes a requirements file and installs the packages listed
pip3 freeze > requirements.txt # Creates a file with a list of installed packages and their versions
deactivate # Exits the 'venv' virtual environment, back to the global environment
```

## Miscellaneous Python

### String Manipulation

There are number of methods where we can manipulate strings or checking strings based on some check such as if the string is a number.

**Float/Decimal Place Strings**
```python
# Printing decimal places
pi = 3.14159265
print(f"{pi:.2f}") # 3.14
print(f"{pi:.4f}") # 3.1416
print(f"{round(pi, 3)}") # 3.142

# String with padded zeroes to the left under the max length given
str(pi).zfill(20) # '00000000003.14159265'
``` 
**Constructing and Manipulating Strings**
```python
# Repeat and concatenate strings
game = "duck " * 2 + "goose" # game == 'duck duck goose'

# Replace each matching occurrence in a string with a new substring
game.replace("duck", "hippo") # 'hippo hippo goose'
# You can give an optional max replacement count
game.replace("duck", "hippo", 1) # 'hippo duck goose'

# We can use join, to combine strings or characters
letters = ['S', 'e', 'a', 'n', ' ', 'S', 'm', 'i', 't', 'h']
name = "".join(letters) # name == "Sean Smith"

# We can remove leading and trailing whitespace
sentence = " How are you today    " 
sentence.lstrip() # 'How are you today    '
sentence.rstrip() # ' How are you today'
sentence = sentence.strip() # sentence == 'How are you today'

# Breaks up a string into a list based on a string separator
sentence.split() # ['How', 'are', 'you', 'today']
sentence.split("you") # ['How are ', ' today']
```
**Counting Occurences & Indexing**
```python
phrase = "hello world!"

# Count the occurrences of a substring
phrase.count('l') # 3
phrase.count('hello') # 1

# Find the index of the first occurrence of a substring
phrase.find('l') # 2
phrase.rfind('l') # 9
phrase.find('zebra') # -1
phrase.index('l') # 2
phrase.rindex('l') # 9
phrase.index('zebra') # ValueError
```
**Adjusting string case**
```python
sentence = "How are you Today?"

# Transform string - These methods will output a new string (no mutation)
sentence.upper() # 'HOW ARE YOU TODAY?'
sentence.lower() # 'how are you today?'
# Capitalises the first letter and makes every other character lower case
sentence.capitalize() # 'How are you today?'
# Capitalises the first letter of each word
sentence.title() # 'How Are You Today?'
```
**String checks**
```python
name = "Sean Smith"

# If a string ends with a substring
name.startswith("Sean") # True
name.endswith('Sean') # False

# Check if a string follows certain conditions
name.islower() # False - If the string is all lowercase characters
name.isupper() # False - If the string has all uppercase characters
name.istitle() # True - If the first character of each word is uppercase
name.isalnum() # False (the whitespace) - If a string has only alphanumeric characters
name.isalpha() # False (the whitespace) - If a string has only alphabetical characters
```
**Numerical string checks**
```python
number = "69420"

# Checking if a string is a number
number.isdecimal() # True - If all characters are decimal characters
number.isdigit() # True - Decimal + subscript/superscript,
number.isnumeric() # True - Decimals + Digits + fraction, roman numerals
```

### Any & All

You can use any and all when you have transformed a container of elements in Boolean values, and you can further check if 'any' or 'all' elements are True.

**Any**
```python
# Any allows us to check if 'any' element of a collection is true
names = ["Sean", "Hayden", "Miguel"]
# If any name starts with the letter 'S'
if any(name.startswith('S') for name in names): # True
    pass

any([True, True, False, True]) # True
```
**All**
```python
# All allows us to check if 'all' elements of a collection are true
numbers = [1, 2.3, '3', "4.5"]
# If all elements in numbers are ints or floats
if all(isinstance(num, (int, float)) for num in numbers): # False
    pass

all([True, True, True, True]) # True
```

### Shallow & Deep Copying

When copying nested data structures, we need to be wary that `.copy()` will handle nested data as pointers. The way to solve this is to use `deepcopy()` from the copy library.

**Shallow Copying**
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
```
**Deep Copying**
```python
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

### Files

We can read, write or append text to files with two main methods. One with the traditional open function and one with a 'with' statement which automatically handles closing a file after its scope (indentation) has been completed.

```python
# You can open a file this way, but remember to close it
f = open("file.txt", 'r')
f.readlines() # e.g. ["list of\n", "lines of\n", "the file\n"]
f.close()

# Using the with statement will automatically close the file
with open("file.txt", 'r') as f:
    # Read each line of the file in a loop
    for line in f:
        print(line.strip())

# Write lines to a file
with open("new.txt",'w') as f:
    f.write("First line of file\n")
    f.write("Second line\n")

# Append lines to a file
with open("new.txt",'a') as f:
    f.writelines(["Third\n", "Fourth\n"])
```

### Decorators

Decorator take in a function and then add some further functionality to it, and then returns it. When building a custom decorator, we need to be wary of functions have a different number or type of arguments, thus we use `*args` and `**kwargs`. `*args` are a variable number of non-keyword arguments and `**kwargs` are a variable number of keyword arguments.

```python
def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"The result is {result}")
        return result
    return wrapper

@print_result
def multiply(a, b):
    return a / b

@print_result
def square(a):
    return a
```

### Docstrings

Docstrings are powerful commenting paradigms that allow any developer to understand modules and functions, what the arguments are, any exceptions that can be raised, what the return value actually is and an overall summary of what is happening.

```python
def square(num):
    """Calculates and returns the square result of a number

    Args:
        num (int, float): A number parameter

    Raises:
        ValueError: If the number argument is not numeric

    Returns:
        int, float: A square number result
    """
    if not isinstance(num, (int, float)):
        raise ValueError("Number must be numeric")

    return num * num
```

### Types

There are types in Python: str, chr, int, float, bool and more (see the Typing library), and we can further check a variable's typing.

```python
goose = "honk"
# Checking types
isinstance(goose, str) # True
type(goose) == str # True
```

### Type Hinting

Type hinting allows us to add non-required, but useful types to arguments, constants and function return types. For type hinting, you will need to run mypy *filename.py* to check if there are any issues.

```python
from typing import List, Dict, Optional, Union
from collections import Counter

def multiply(a : Union[int, float], b : Union[int, float]) -> Union[int, float]:
    return a * b

def shout(message, capital: Optional[bool]=False) -> None:
    print(message.upper()) if capital else print(message)

def occurrences(letters: List[str]) -> Dict[str, int]:
    return dict(Counter(letters))
```


### Classes

Classes are code templates for creating objects. There will usually be a constructor `__init__` method within the class, custom methods and builtin definable methods that allow for the class to access Python operations such as `str()`, `+`, `*`, etc.

```python
# Class name is usually capitalised
class Pokemon():
    # A constructor, pay attention to the arguments needed
    def __init__(self, pokemon, level):
        self.pokemon = pokemon
        self.name = pokemon
        self.level = level

    # Method 1 - Non-pythonic setter
    def rename(self, name):
        self.name = name

    # Method 2 - Pythonic Getter and setter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def level_up(self):
        self.level += 1

    # String representation of the class
    def __repr__(self):
        return f"Pokemon: {self.pokemon} ({self.name}) [Level: {self.level}]"

if __name__ == "__main__":
    # When initialising a class, pay attention to the __init__ to know what arguments are needed
    charmander = Pokemon('Charmander', 1)
    charmander.level_up()
    charmander.name = "Charlie"
    print(charmander)
    charmander.rename("Christopher")
    print(charmander)
```
