def check(lastword, foundwords, table, i, j, checked_coords):
    checked_coords.append((i, j))
    foundwords[(i, j)].append((lastword, checked_coords))
    for y in range(-1, 2):
        for x in range(-1, 2):
            if x == 0 and y == 0:
                continue
            newY = j + y
            newX = i + x
            if (newX, newY) not in checked_coords and (0 <= newX < len(table[0])) and (0 <= newY < len(table)):
                newWord = lastword + table[newX][newY]
                # print("\n" + newWord + "\n" + "".join(sorted(newWord)) + "\n")
                sorte = sorted(newWord)
                if newWord == "".join(sorte) and len(sorte) == len(set(sorte)):
                    foundwords[(i, j)].append((newWord, checked_coords))
                    check(newWord, foundwords, table, newX, newY, checked_coords.copy())

                    for found in foundwords.get((newX, newY)):
                        if any(i == j for i in checked_coords for i in found[1]):
                            foundwords[(newX, newY)].append((newWord + found[0], checked_coords + found[1]))
                    # if len(newWord) > 2:


lines = int(input())

for timer in range(lines):
    input()
    dimention = int(input())
    table = []
    found_words = {}
    for a in range(dimention):
        table.append(list(input()))
        for b in range(dimention):
            found_words[(b, a)] = []

    for i, word in enumerate(table):
        for j, letter in enumerate(word):
            check(table[i][j], found_words, table, i, j, [])
    all_answers = set()
    for answers in found_words.values():
        for answer in answers:
            all_answers.add(answer[0])
    printables = list(filter(lambda x: len(x) > 2, list(all_answers)))
    printables.sort()
    printables.sort(key=len)
    for printable in printables:
        print(printable)
    if timer + 1 < lines:
        print()
