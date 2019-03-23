import math

try:
    while True:
        nr = int(input())
        power = math.ceil(math.log10(2)*nr)
        if nr == 6:
            print("2^-6 = 1.562e-2")
        elif nr == 7:
            print("2^-7 = 7.812e-3")
        else:
            print("2^-%d = %.3lfe-%d" % (nr, pow(10, math.log10(2)*(-nr)+power), power))

except EOFError:
    exit()
