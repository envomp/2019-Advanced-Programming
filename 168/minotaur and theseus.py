while True:
    Input = input()
    if Input == "#":
        break

    candle_list = []
    candle_counter = 0
    a, minotaur, enrico, candle_step = Input.split()
    a = a[:-1]
    tree = {}
    for i in a.split(";"):
        if len(i) > 2:
            tree[i.split(":")[0]] = list((i.split(":")[1]))
        else:
            tree[i.split(":")[0]] = []

    while True:
        found = False
        if minotaur not in tree:
            break
        for i in tree[minotaur]:
            if i != " " and i != enrico and i not in candle_list:
                enrico = minotaur
                minotaur = i
                found = True
                break
        candle_counter += 1
        if not found:
            break
        if candle_counter >= int(candle_step):
            candle_list.append(enrico)
            candle_counter = 0
    if not candle_list:
        print("/" + minotaur)
    else :
        print(" ".join(candle_list), "/" + minotaur)
