# Exercise3: Take a list of integers as argument and returns the greatest element in the list.
def max_list(inlist):
    max_ = inlist[0]
    for i in inlist:
        if max_ < i:
            max_ = i
    return max_


print(max_list([1, 2, 8, 3, 10, 5]))

# Exercise4: Improvement of exercise1
import math
x = input('Please input the radius of the circle: ',)
if type(x) == int:
    m = int(x)
    y = 2 * math.pi * m
    z = math.pi * m * m
    print('Perimeter: ', y)
    print('Area: ', z)
else:
    print('You have not inserted a valid number!')