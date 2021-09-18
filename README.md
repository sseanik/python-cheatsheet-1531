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