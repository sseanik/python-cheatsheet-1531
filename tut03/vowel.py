import pytest

def find_vowels(message):
    # Method 1 - Manually defining
    vowels = {'a': 0, 'e': 0, 'i': 0, 'u': 0, 'o': 0}
    
    # Method 2 - Using a loop (better if the 'aeiou' part was larger)
    vowels = dict()
    for letter in "aeiou":
        vowels[letter] = 0

    # Method 3 - Dictionary comprehension
    vowels = {letter: 0 for letter in "aeiou"}

    for char in message:
        if char.isupper():
            raise ValueError
        if char in "aeiou":
            vowels[char] += 1
    return vowels

def test_uppercase():
    with pytest.raises(ValueError):
        find_vowels("HELLO")
        
if __name__ == '__main__':
    message = input("What is your message? ")
    try:
        print(find_vowels(message))
    except ValueError:
        print("Only use lowercase letters")