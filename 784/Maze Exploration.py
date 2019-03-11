cases = int(input())

while cases:
    aMazing = []
    number = 0
    while True:
        line = input()
        if "_" in line:
            break
        if '*' in line:
            line = list(line[:line.index("*")]) + [0] + list(line[line.index("*") + 1:])

            aMazing.append(line)
        else:
            aMazing.append(list(line))
    start = [(i, colour.index(0)) for i, colour in enumerate(aMazing) if 0 in colour]
    while True:
        found = False
        temp = []
        for e in start:
            if aMazing[e[0]][e[1]] == number:
                if e[0] + 1 < len(aMazing) and aMazing[e[0] + 1][e[1]] == ' ':
                    aMazing[e[0] + 1][e[1]] = number + 1
                    temp.append((e[0] + 1, e[1]))
                    found = True
                if e[0] - 1 >= 0 and aMazing[e[0] - 1][e[1]] == ' ':
                    aMazing[e[0] - 1][e[1]] = number + 1
                    temp.append((e[0] - 1, e[1]))
                    found = True
                if e[1] + 1 < len(aMazing[e[0]]) and aMazing[e[0]][e[1] + 1] == ' ':
                    aMazing[e[0]][e[1] + 1] = number + 1
                    temp.append((e[0], e[1] + 1))
                    found = True
                if e[1] - 1 >= 0 and aMazing[e[0]][e[1] - 1] == ' ':
                    aMazing[e[0]][e[1] - 1] = number + 1
                    temp.append((e[0], e[1] - 1))
                    found = True

                start = temp

        if not found:
            break
        number += 1

    for lone in aMazing:
        print("".join(["#" if str(c).isdigit() else c for c in lone]))
    print(line)
    cases -= 1
