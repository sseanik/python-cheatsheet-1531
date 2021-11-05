from math import ceil, sqrt

def divisors(n):
    '''
    Given some number n, return a set of all the numbers that 
    divide it. For example:
    >>> divisors(12)
    {1, 2, 3, 4, 6, 12}
    24

    Params:
      n (int): The operand

    Returns:
      (set of int): All the divisors of n

    Raises:
      ValueError: If n is not a positive integer
    '''
    #if type(n) is not int or n < 1:
    if not isinstance(n, int) or n < 1:
      raise ValueError("Not a positive integer")

    result = set()

    for i in range(1, ceil(sqrt(n)) + 1):
      if n % i == 0:
        result.add(i)
        result.add(n // i)
    return result