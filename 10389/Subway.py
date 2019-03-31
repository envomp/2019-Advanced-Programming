testcases = int(input())
try:
    for _ in range(testcases):
        rider = input().split()
        cur_coord = rider[:2]
        goal = rider[2:]
        subways = []
        time_elapsed = 0
        while True:
            line = input()
            if not line:
                break
            subways.append([int(x) for x in line.split() if x != "-1"])
        while cur_coord != goal:

            print(subways)

except EOFError:
    exit()
