# COMP1531 21T3 F11A

## Python Cheatsheet

### Looping
```python
shopping = ["bread", "milk", "apple", "banana", "weetbix"]

# For range loop 
# (You can't do item = "something" in the loop)
for item in shopping:
    print(item)

# Traditional loop with index variable 
# (You're allowed to do shopping[i] = "something" in the loop)
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
# Remember code blocks are denoted by the ':' colon symbol and indentation
if "bread" in shopping and "milk" in shopping:
    print("We need fruit")
elif "apple" in shopping and "banana" not in shopping:
    print("We got apples, but need bananas")
else:
    print("We basically need everything")
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

### Pythonic One Liners
```python
# Ternary
# List Comprehension
# Dictionary Comprehension
# Python functions e.g. join

```