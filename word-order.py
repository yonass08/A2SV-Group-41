# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
counter = Counter()

for _ in range(n):
    counter[input()] += 1
    
print(len(counter))
print(*counter.values())
