def isValid(isbn):
    """
    Determines whether the ISBN is valid or not
    """
    # Multiply each of the first 9 digits by its position. The positions go 
    # from 1 to 9. Add up the 9 resulting products.
    total = 0
    for index, number in enumerate(isbn[:9]):
        total += (index + 1) * int(number)

    # Divide this sum by 11, and get the remainder, which is a number between 
    # 0 and 10.
    remainder = total % 11

    # If the remainder is 10, the last character should be the letter 'X'. 
    # Otherwise, the last character should be the remainder (a single digit).
    if remainder == 10:
        return isbn[-1] == "X"
    else:
        return int(isbn[-1]) == remainder


if __name__ == "__main__":
    isbn = input("What is your ISBN? ")
    if isValid(isbn):
        print(f"{isbn} is valid")
    else:
        print(f"{isbn} is invalid")
    