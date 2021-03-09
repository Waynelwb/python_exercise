# Exercise1:
pi = float(3.1416)
x = int(input("Please enter the radius of the circle: "))
Perimeter = pi * 2 * x
Area = pi * x * x
print("Perimeter: ", Perimeter)
print("Area: ", Area)

# Exercise2:
x = int(input("Please enter the first number: "))
y = int(input("Please input the second number: "))
if x % y == 0:
    print(x, "is a multiple of ", y)
else:
    print(x, "is not a multiple of ", y)

# Exercise3: Take a list of integers as argument and returns the greatest element in the list.
def max_list(inlist):
    max_ = inlist[0]
    for i in inlist:
        if max_ < i:
            max_ = i
    return max_


print(max_list([1, 2, 8, 3, 10, 5]))

# Exercise4: Improvement of exercise1
try:
    x = int(input('Please input the radius of the circle: ',))
    if type(x) == int:
        m = int(x)
        y = 2 * pi * m
        z = pi * m * m
        print('Perimeter: ', y)
        print('Area: ', z)
except ValueError as err:
    print("You have not inserted a valid number!")

# Exercise5-2.1:
import sys


Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *",
        " *   * ", "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for c in digit[row]:
                if c == "*":
                    c = str(number)
                line += c
            line += "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)

# Exercise5-2.2:
