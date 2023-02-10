n, m = map(int, input().split())

first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

first_pointer = 0
second_pointer = 0

res = []

while first_pointer < n and second_pointer < m:
    if first_list[first_pointer] <= second_list[second_pointer]:
        res.append(first_list[first_pointer])
        first_pointer += 1
    else:
        res.append(second_list[second_pointer])
        second_pointer += 1

res += first_list[first_pointer:]
res += second_list[second_pointer:]

print(*res)
