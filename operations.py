from collections import defaultdict
n = int(input())

vertices = defaultdict(list)
k = int(input())

res = []
for _ in range(k):
    op = list(map(int, input().split()))
    if op[0] == 1:
        vertices[op[1]].append(op[2])
        vertices[op[2]].append(op[1])
    else:
        res.append(vertices[op[1]])

for line in res:
    print(*line)
