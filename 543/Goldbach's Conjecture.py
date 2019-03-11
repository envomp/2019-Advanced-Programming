def sieve(n):
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)


primes = [int(x) for x in sorted(set(sieve(1000000)))]
hashmap = {}
for prime in primes:
    hashmap[prime] = None

tot_len = len(primes)

while True:
    nr = int(input())
    if nr == 0:
        exit()

    for i in primes:
        pair = nr - int(i)
        if pair in hashmap:
            print(nr, "=", i, "+", pair)
            break

