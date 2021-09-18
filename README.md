# COMP1531 21T3 F11A

## Python Cheatsheet

### Looping
```python
shopping = ["bread", "milk", "apple", "banana", "weetbix"]

# For range loop
for item in shopping:
    print(item)

# Traditional loop with index variable
for i in range(len(shopping)):
    print(shopping[i])

# Loop with both the index and item available
for i, item in enumerate(shopping):
    print(f"Item: {item}, Index: {i}")

# While loops
i = 0
while i < len(shopping):
    print(shopping[i])
```


### If Statements
```python
# Remember code blocks are denoted by the ':' colon symbol and indentation
if "bread" in shopping:
    print("We need bread")
elif shopping[1] == "milk":
    print("We need milk")
else:
    print("We need bread and milk")
```

### List Slicing
```python
output = [1, 2, 3, 4, 5, 6]

output[::-1] # Will reverse the list -> [6, 5, 4, 3, 2, 1]
output[2:5]  # Inclusive of 2nd index, but not 5th -> [3, 4, 5]]
output[2:]   # Will include index values from 2 until the end -> [3, 4, 5, 6]
output[:4]   # Will include first 4 elements -> [1, 2, 3, 4]
output[-3:]  # Will include last 3 elements -> [4, 5, 6]
```