nr_of_cases = int(input())
input()
replacement_dict = {"A": "2",
                    "B": "2",
                    "C": "2",
                    "D": "3",
                    "E": "3",
                    "F": "3",
                    "G": "4",
                    "H": "4",
                    "I": "4",
                    "J": "5",
                    "K": "5",
                    "L": "5",
                    "M": "6",
                    "N": "6",
                    "O": "6",
                    "P": "7",
                    "R": "7",
                    "S": "7",
                    "T": "8",
                    "U": "8",
                    "V": "8",
                    "W": "9",
                    "X": "9",
                    "Y": "9",
                    "-": ""
                    }
for _ in range(nr_of_cases):
    b_list = []
    number_dict = {}
    number_numbers = int(input())
    for _ in range(number_numbers):
        lane = input().replace("-", "").strip()
        if not lane:
            break
        b_list.append(lane)
    for i in b_list:
        new_number = []
        for k in i:
            if not k.isdigit():
                new_number.append(replacement_dict[k])
            else:
                new_number.append(k)
        new_number = "".join(new_number)
        if not new_number in number_dict.keys():
            number_dict[new_number] = 1
        else:
            number_dict[new_number] += 1
    answer = sorted([y for x, y in enumerate(number_dict) if number_dict[y] != 1])
    if not answer:
        print("No duplicates.")
    else:
        for element in answer:
            print(f"{element[:3]}-{element[3:]} {number_dict[element]}")
    try:
        input()
    except EOFError:
        exit()
    print()
