# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
s = set(input().split())
m = input()
print(len(s.difference(input().split())))
