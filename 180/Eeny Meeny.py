while True:
    ranges = input()
    if ranges == '0 0':
        break
    min_count, max_count = ranges.split()
    max_count = int(max_count)
    min_count = int(min_count)
    if min_count <= 3:
        print("Better estimate needed")
        continue
    x = 0
    for i in range(2, min_count):
        x = (x + min_count) % i

    # for(i = 2; i <=num; i++)
    #    x = (x + cycle) % i;

    print(x)
