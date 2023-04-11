n = int(input())
vertices = [[] for _ in range(n+1)]

for start in range(1, n+1):
    row = list(map(int, input().split()))
    for i in range(n):
        if row[i] == 1:
            vertices[start].append(i+1)

for i in range(1, n+1):
    print(len(vertices[i]), *vertices[i])


