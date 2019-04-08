
def find_set(ii):
    if connections[ii] == ii:
        return ii
    else:
        connections[ii] = find_set(connections[ii])
        return find_set(connections[ii])


def upgrade_set(a, b):
    connections[find_set(a)] = connections[find_set(b)]


try:
    caes = int(input())
    input()

    for _ in range(caes):
        yes = 0
        no = 0
        connections = []
        cases = int(input())
        for i in range(cases):
            connections.append(i)
        while True:
            line = input()
            if not line:
                break
            line = line.split()
            start = int(line[1]) - 1
            end = int(line[2]) - 1

            if line[0] == "c":
                upgrade_set(start, end)
            else:
                if start == end or find_set(start) == find_set(end):
                    yes += 1
                else:
                    no += 1
        print(str(yes) + "," + str(no) + "\n")

except EOFError:
    exit()
