'''
Hello
'''

import sys

for line in sys.stdin:
    hours = int(line[:2])
    minutes = int(line[2:])

    time_period = "AM" #pylint: disable=invalid-name
    if hours >= 12:
        time_period = "PM" #pylint: disable=invalid-name
        if hours > 12:
            hours -= 12

    print(f"{hours:02}:{minutes:02} {time_period}")