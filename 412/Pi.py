import itertools
from math import gcd

while True:
    times = int(input())
    if times == 0:
        exit()
    else:
        cases = []
        n = 0
        for _ in range(times):
            cases.append(int(input()))
        combinisations = tuple(itertools.combinations(cases, 2))
        for combo in combinisations:
            if gcd(combo[0], combo[1]) == 1:
                n += 1
        if n == 0:
            print("No estimate for this data set.")
        else:
            print("%.6f" % (round((((6 * len(combinisations)) / n) ** 0.5), 6)))
