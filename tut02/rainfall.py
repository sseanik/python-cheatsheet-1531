import pytest
from time import sleep


def rainfall(integers):
    '''
    Compute the average of only the positive elements in the list.
    Pythonic solution
    '''
    # Convert the integers into a list of Boolean values, where True is when a 
    # non-int or non-float is found
    if any(not (isinstance(num, int) or isinstance(num, float)) for num in integers):
        raise ValueError("You can only use a list of Integers or Floats")
    # Create a list with only the positive integers
    positives = [num for num in integers if num > 0]
    # Use a ternary if/else statement for the return
    return sum(positives) / len(positives) if len(positives) > 0 else None

def rainfall_alternative(integers):
    '''
    Compute the average of only the positive elements in the list.
    '''
    count = 0
    total = 0
    for num in integers:
        # If the number is not an int or float
        if not (isinstance(num, int) or isinstance(num, float)):
            raise ValueError("You can only use a list of Integers or Floats")
        if num > 0:
            count += 1
            total += num
    # Need to account for empty lists avoiding division by zero
    if count == 0:
        return None
    else:
        return total / count


# Tests
@pytest.fixture()
def simple_variable():
    return [1, 2, 3]

def test_simple(simple_variable):
    assert rainfall(simple_variable) == 2

def test_alt(simple_variable):
    assert rainfall_alternative(simple_variable) == 2

def test_empty():
    assert rainfall([]) == None

def test_negatives():
    assert rainfall([-1,-2,-2,2]) == 2

def test_all_negatives():
    assert rainfall([-1,-2,]) == None

def test_zero():
    assert rainfall([0, 0, 0]) == None

def test_wacky():
    with pytest.raises(ValueError):
        rainfall([1, 2, "Goose"])
