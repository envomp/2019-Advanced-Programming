testcases = int(input())
input()
for _ in range(testcases):
    tree = {}
    start = None
    while True:
        next = input()
        if not start:
            start = next
        if next == "":
            break
        next = int(next)
        tree[next] = []
        for key in tree.keys():
            if key < next:
                tree[key] += [next]
    best = []
    for sets in tree.items():
        new = list(sets[1])
        if len(new) > len(best):
            best = new
    best.append(start)
    best = set(best)
    print("Max hits:", len(best))
    for element in best:
        print(element)
    print()
