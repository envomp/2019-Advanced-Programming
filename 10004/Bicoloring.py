def loop(true, match):
    temp = []
    for ele in match:
        a = ele[0]
        b = ele[1]
        if true:
            if a in tree.keys():
                if b in tree.keys():
                    if tree[a] == tree[b]:
                        true = False
                else:
                    tree[b] = swap[tree[a]]

            else:
                if b in tree.keys():
                    tree[a] = swap[tree[b]]
                else:
                    temp.append([b, a])
    return true, temp


while True:
    times = int(input())
    if times == 0:
        exit()
    length = int(input())
    tree = {}
    true = True
    cur_color = 0
    swap = [1, 0]
    match = []
    if length == 0:
        print("BICOLORABLE.")
        true = False
    if true:
        for _ in range(length):
            match.append(input().split())

        match.sort(key=lambda x: x[1])
        match.sort(key=lambda x: x[0])
        tree[match[0][0]] = 0
        while len(match) and true:
            true, match = loop(true, match)

        if true:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
