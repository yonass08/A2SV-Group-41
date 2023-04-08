num_test_cases = int(input())
swaps = 0


def MashaSort(nums, start, end):
    global swaps
    if start + 1 == end:
        return [nums[start]]

    mid = (start + end) // 2
    left = MashaSort(nums, start, mid)
    right = MashaSort(nums, mid, end)

    if left[0] > right[0]:
        swaps += 1
        return right + left
    return left + right


for _ in range(num_test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    swaps = 0

    final = MashaSort(nums, 0, len(nums))
    res = swaps

    for i in range(len(final)-1):
        if final[i] > final[i+1]:
            res = -1
            break

    print(res)

    # end of current test case
# end of test case loop
