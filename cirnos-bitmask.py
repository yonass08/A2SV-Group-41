num_test_cases = int(input())

for _ in range(num_test_cases):
    x = int(input())

    res = 1
    temp = x
    while temp & 1 == 0:
        temp >>= 1
        res <<= 1

    if x == 1:
        print(3)
    elif x > res:
        print(res)
    else:
        print(res + 1)

    # end of current test case
# end of test case loop
