num_test_cases = int(input())

for _ in range(num_test_cases):
    n, m = map(int, input().split())

    matrix = []
    for row in range(n):
        matrix.append(list(map(int, input().split())))

    sum_diag = [0] * (n + m - 1)
    diff_diag = [0] * (n + m - 1)

    for i in range(len(sum_diag)):
        row, col = 0, 0
        if i < n:
            row = i
        else:
            row = n-1
            col = i - row

        while row >= 0 and col < m:
            sum_diag[i] += matrix[row][col]
            row -= 1
            col += 1

    for i in range(len(diff_diag)):
        row, col = 0, 0
        if i < n:
            row = n - i - 1 
        else:
            col = i - n + 1


        while row < n and col < m:
            diff_diag[i] += matrix[row][col]
            row += 1
            col += 1
            

    res = 0

    for row in range(n):
        for col in range(m):
            current = sum_diag[row + col] + diff_diag[col - row + n - 1] - matrix[row][col]
            res = max(current, res)

    print(res)
