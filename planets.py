from collections import Counter
num_test_cases = int(input())

for _ in range(num_test_cases):
    second_machine_cost = int(input().split()[1])
    orbitCounter = Counter(input().split())

    res = 0
    for orbit in orbitCounter:
        res += min(second_machine_cost, orbitCounter[orbit])

    print(res)
    
