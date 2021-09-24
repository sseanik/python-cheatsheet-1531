import pytest

'''
Compute the average of only the positive elements in the list.
'''
def rainfall(integers):
    pass

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
