def add(connectionss, startt, endd):
    if startt not in connectionss:
        connectionss[startt] = [endd]
    else:
        for key in connectionss[start]:
            connectionss[key] += [endd]
        connectionss[startt] += [endd]
    return connectionss


try:
    caes = int(input())
    input()

    for _ in range(caes):
        yes = 0
        no = 0
        connections = {}
        cases = int(input())
        while True:
            line = input()
            if not line:
                break
            line = line.split()
            start = int(line[1])
            end = int(line[2])

            if line[0] == "c":
                connections = add(connections, start, end)
                connections = add(connections, end, start)

                print(connections)

            else:
                if start == end:
                    yes += 1
                elif end in connections[start]:
                    yes += 1
                else:
                    no += 1
        print(str(yes) + "," + str(no) + "\n")

except EOFError:
    exit()
