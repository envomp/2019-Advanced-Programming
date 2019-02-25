alphabet = {
    "A": 1,
    "C": 2,
    "G": 3,
    "T": 4
}
cases = int(input())
for a in range(cases):
    input()
    rule = int(input().split()[1])
    allYall = []
    for i in range(rule):
        line = input()
        recc = 0
        table = [0, 0, 0, 0]
        for x in line:
            for y in range(alphabet[x], 4):
                recc += table[y]
            table[alphabet[x] - 1] += 1
        allYall.append([line, recc])
    allYall = sorted(allYall, key=lambda x: x[1])
    for o in allYall:
        print(o[0])
    if a != cases - 1:
        print()
