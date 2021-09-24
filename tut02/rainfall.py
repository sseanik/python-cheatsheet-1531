import pytest

'''
Compute the average of only the positive elements in the list.
'''
def rainfall(integers):
    # for i in integers:
    #     if not (isinstance(i, int) or isinstance(i, float)):
    #         raise ValueError
    if any(not (isinstance(num, int) or isinstance(num, float)) for num in integers):
        raise ValueError("Make sure you only use ints or floats")
    positives = [num for num in integers if num > 0]
    return sum(positives) / len(positives) if len(positives) > 0 else None

def test_simple():
    assert rainfall([1,2,3]) == 2

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
# Write tests here
