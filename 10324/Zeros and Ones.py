try:
    case = 0
    while True:
        case += 1
        lane = input().split()
        print(f"Case {case}:")
        rule = [int(x) for x in lane[0]]
        nr = int(input())
        for _ in range(nr):
            testcase = [int(x) for x in input().split()]
            substring = rule[min(testcase):max(testcase) + 1]
            if sum(substring) in [0, len(substring)]:
                print("Yes")
            else:
                print("No")

except EOFError:
    exit()
