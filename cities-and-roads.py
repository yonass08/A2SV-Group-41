n = int(input())

count = 0
for start in range(1, n+1):
    count += sum(map(int, input().split()))

print(count//2)



