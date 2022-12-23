# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
N = int(input())

res = True
for i in range(N):
    mSet = set(input().split())
    
    #check if A is a strict super set of mSet
    if len(A) <= len(mSet):
        res = False
        break
    
    for num in mSet:
        if num not in A:
            res = False
            break
        
print(res)
    
