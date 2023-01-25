n = int(input())
arr = list(map(int, input().split()))

parity = [0, 0]

for num in arr:
    parity[num % 2] += 1

if parity[0] * parity[1] == 0:
    print(*arr)
else:
    print(*sorted(arr))
