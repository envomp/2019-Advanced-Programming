import math

try:
    while True:
        number = int(input())
        print(number, end="!\n")
        print(math.factorial(number))

except EOFError:
    exit()
