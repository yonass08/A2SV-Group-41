num_test_cases = int(input())

for _ in range(num_test_cases):
    n = int(input())
    arr = sorted(map(int, input().split()))
    res = 'YES'
    for idx in range(n-1):
        if arr[idx] + 1 < arr[idx+1]:
            res = 'NO'
            break

    print(res)

    # end of current test case
# end of test case loop
