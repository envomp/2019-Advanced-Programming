import itertools

times = int(input())
for x in range(times):
    base = list(input())
    answer = sorted(list(set(itertools.permutations(base))))
    [print(''.join(perm)) for perm in answer]
    print()
