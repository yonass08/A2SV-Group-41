# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
li = [int(x) for x in input().split()]
st = set(li)

print((sum(st) * K - sum(li)) // (K-1)) 
