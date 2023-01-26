num_test_cases = int(input())

for _ in range(num_test_cases):
    n = int(input())
    arr = list(map(int, input().split()))

    left, right = 0, 0

    curr_max = arr[left]
    res = 0

    while right < n:
        if arr[left] * arr[right] > 0:
            curr_max = max(curr_max, arr[right])
            right += 1
        else:
            res += curr_max
            left = right
            curr_max = arr[left]

    res += curr_max

    print(res)

    # end of current test case
# end of test case loop
