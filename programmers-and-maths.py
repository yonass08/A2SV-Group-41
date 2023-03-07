num_test_cases = int(input())
 
 
def is_possible(a, b, n):
    if n == 0:
        return True
 
    if a // n < 1 or b // n < 1:
        return False
 
    return (a + b) // n >= 4
 
 
for _ in range(num_test_cases):
    a, b = map(int, input().split())
 
    high = min(a, b)
    low = 0
 
    while low <= high:
        mid = (low + high) // 2
 
        if is_possible(a, b, mid):
            low = mid + 1
        else:
            high = mid - 1
 
    print(high)
 
    # end of current test case
# end of test case loop
