'''
This file does something
'''

from calendar import isleap

ORIGIN_YEAR = 1970

def day_to_year(days):
    """[summary]

    Args:
        days ([type]): [description]

    Returns:
        [type]: [description]
    """
    year = ORIGIN_YEAR

    while days > 0:
        if isleap(year):
            days -= 366
        else:
            days -= 365
        if days > 0:
            year += 1

    return year
