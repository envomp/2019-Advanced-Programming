try:
    def mod(a, b, c):
        if b == 0:
            return 1
        if b % 2 == 0:
            x = mod(a, b / 2, c)
            return (x * x) % c
        else:
            return (a % c * mod(a, b - 1, c)) % c

    while True:
        a = int(input())
        b = int(input())
        c = int(input())
        print(mod(a, b, c))
        input()

except Exception:
    exit()

'''
5 ** 5 % 9 = 2
(5 % 9 * 5 ** 4 % 9) % 9 | 5 * 4 % 9 = 2
(5 * 5**2 % 9 * 5**2 % 9) % 9 | 5 * 4 * 4 = 2
(5 * (5 % 9 * 5 % 9) * (5 % 9 * 5 % 9)) % 9 | 2
'''
