num = [1]
c2 = c3 = c5 = c7 = 0
while max(num) < 2000000000:
    next = min(2 * num[c2], 3 * num[c3], 5 * num[c5], 7 * num[c7])
    num.append(next)
    if next == 2 * num[c2]:
        c2 += 1
    if next == 3 * num[c3]:
        c3 += 1
    if next == 5 * num[c5]:
        c5 += 1
    if next == 7 * num[c7]:
        c7 += 1

while True:
    nr = input()
    if nr == "0":
        exit()
    if not(len(nr) >= 2 and nr[-2] == "1"):
        if nr[-1] == "1":
            ending = "st"
        elif nr[-1] == "2":
            ending = "nd"
        elif nr[-1] == "3":
            ending = "rd"
        else:
            ending = "th"
    else:
        ending = "th"
    print("The " + nr + ending + " humble number is " + str(num[int(nr) - 1]) + ".")
