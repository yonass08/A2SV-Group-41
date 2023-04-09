n = int(input())

matrix = []
for row in range(n):
    matrix.append(list(map(int, input().split())))

outs = set()
ins = set()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 1:
            outs.add(row+1)
            ins.add(col+1)

source = set(range(1, n+1)).difference(ins)
sink = set(range(1, n+1)).difference(outs)

print(len(source), *sorted(source))
print(len(sink), *sorted(sink))
