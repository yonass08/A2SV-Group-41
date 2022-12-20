# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

def pilingUp(arr):
    l, r = 0, len(arr)-1
    curr = max(arr[l], arr[r])
    
    while l <= r:
        left, right = arr[l], arr[r]
        if left > right:
            if left > curr: return 'No'
            curr = left
            l += 1
        else:
            if right > curr: return 'No'
            curr = right
            r -= 1
            
    return 'Yes'

for _ in range(n):
    sz = input()
    arr = list(map(int, input().split()))
    print(pilingUp(arr))
