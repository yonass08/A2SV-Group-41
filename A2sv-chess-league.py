n, k = map(int, input().split())

nums = list(map(int, input().split()))


def possible_winners(nums, start, end, k):
    if start + 1 == end:
        small = min((nums[start], start), (nums[end], end))
        large = max((nums[start], start), (nums[end], end))

        if small[0] + k < large[0]:
            return [large[1]]
        else:
            return [small[1], large[1]]

    mid = (start + end + 1) // 2
    left_winners = possible_winners(nums, start, mid-1, k)
    right_winners = possible_winners(nums, mid, end, k)
    res = merge(nums, left_winners, right_winners, k)
    return res


def merge(nums, left_winners, right_winners, k):
    ls, rs = 0, 0

    while ls < len(left_winners) and nums[left_winners[ls]] + k < nums[right_winners[0]]:
        ls += 1

    while rs < len(right_winners) and nums[right_winners[rs]] + k < nums[left_winners[0]]:
        rs += 1

    res = []
    while ls < len(left_winners) and rs < len(right_winners):
        if nums[left_winners[ls]] < nums[right_winners[rs]]:
            res.append(left_winners[ls])
            ls += 1
        else:
            res.append(right_winners[rs])
            rs += 1

    res += left_winners[ls:]
    res += right_winners[rs:]

    return res


res = [x + 1 for x in possible_winners(nums, 0, len(nums)-1, k)]
res.sort()
print(*res)
