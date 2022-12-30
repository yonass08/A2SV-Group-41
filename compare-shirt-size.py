
lookup = {'S': -1, 'M': 0, 'L': 1}

num_test_cases = int(input())

for _ in range(num_test_cases):
    first, second = input().split()
    
    first_value = (lookup[first[-1]] * len(first))
    second_value = (lookup[second[-1]] * len(second))

    if first_value > second_value:
        print('>')
    elif first_value < second_value:
        print('<')
    else:
        print('=')

