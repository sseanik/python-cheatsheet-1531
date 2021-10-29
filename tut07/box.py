SIZE = 10 # DRY don't repeat yourself

# Top down thinking
def border(i, j):
    return i == 0 or i == (SIZE - 1) or j == 0 or j == (SIZE - 1)

for row in range(SIZE): # KISS
    for col in range(SIZE): # KISS
        print("*" if border(row, col) else " ", end="")
    print()