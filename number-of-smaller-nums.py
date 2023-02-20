n, m = map(int, input().split())

first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

counter = 0

res = []

for num in second_list:
    while counter < n and first_list[counter] < num:
        counter += 1

    res.append(counter)

print(*res)
