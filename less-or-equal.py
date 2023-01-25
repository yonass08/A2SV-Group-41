n, k = map(int, input().split())

arr = sorted(map(int, input().split()))

if k == n:
    print(arr[-1])
elif k == 0:
    print(arr[0]-1 if arr[0]-1 > 0 else -1)
elif arr[k] == arr[k-1]:
    print(-1)
else:
    print(arr[k-1])
