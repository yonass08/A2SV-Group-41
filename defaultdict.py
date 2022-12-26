# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())

dictionary = defaultdict(list)

for index in range(1, n+1):
    dictionary[input()].append(index)
    
for _ in range(m):
    res = dictionary[input()] or ['-1']
    print(*res)
