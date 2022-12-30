num_test_cases = int(input())

for _ in range(num_test_cases):
    size = int(input())
    array = list(map(int, input().split()))
    string = input()
    
    res = 'YES'
    lookup = {}
    for index in range(size):
        if array[index] in lookup and lookup[array[index]] != string[index]:
            res = 'NO'
            break
        else:
            lookup[array[index]] = string[index]
            
    print(res)
