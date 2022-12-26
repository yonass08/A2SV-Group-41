# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
englishSubscribers = set(input().split())

m = int(input())
frenchSubscribers = set(input().split())

print(len(englishSubscribers.union(frenchSubscribers)))
