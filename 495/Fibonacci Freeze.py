
def fib_last_digit(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for i in range(1,n):
            a, b = b, (a+b)
        return b


try:
    while True:
        n = int(input())
        print(f"The Fibonacci number for {n} is {fib_last_digit(n)}")
except EOFError:
    exit()
