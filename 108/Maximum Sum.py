def kadane1d(matrix, dist):
    array = matrix[0]
    best = [-128, 0, 0]
    cur_sum = [0, 0, 0]
    for el in range(len(array)):
        cur_sum[0] += array[el]
        cur_sum[2] = el + 1
        if cur_sum[0] >= best[0]:
            best = cur_sum.copy()
        if cur_sum[0] < 0:
            cur_sum = [0, el+1, el+1]
    return best


def kadane2d(matrix):
    test = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            test.append(matrix, j)


while True:
    side = int(input())
    total = []
    while len(total) != side ** 2:
        new = [x for x in input().split() if x != ""]
        total += new
    total = list(map(int, total))
    kadane2d(total)
