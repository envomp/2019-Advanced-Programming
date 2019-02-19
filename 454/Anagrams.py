nr_of_cases = int(input())
input()
for _ in range(nr_of_cases):
    b_list = []
    while True:
        lane = input()
        if not lane:
            break
        b_list.append([lane, sorted(lane.replace(" ", ""))])
    a_list = list(sorted(b_list, key=lambda x: x[0]))
    for original in range(len(a_list)):
        for match in range(len(a_list)):
            if match > original:
                if original != match:
                    if len(a_list[original][1]) == len(a_list[match][1]):
                        if a_list[original][1] == a_list[match][1]:
                            print(f"{a_list[original][0]} = {a_list[match][0]}")
    print()
