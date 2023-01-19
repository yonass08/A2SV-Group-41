n, m = list(map(int, input().split()))

cross_word = []
for row in range(n):
    cross_word.append(list(input()))

row_elements = [set() for _ in range(n)]
col_elements = [set() for _ in range(m)]

row_deletions = [set() for _ in range(n)]
col_deletions = [set() for _ in range(m)]

# find which characters to delete
for row in range(n):
    for col in range(m):
        char = cross_word[row][col]

        if char in row_elements[row]:
            row_deletions[row].add(char)
        else:
            row_elements[row].add(char)

        if char in col_elements[col]:
            col_deletions[col].add(char)
        else:
            col_elements[col].add(char)
    # end of inner loop
# end of nesting

for row in range(n):
    for col in range(m):
        char = cross_word[row][col]

        if char in row_deletions[row] or char in col_deletions[col]:
            cross_word[row][col] = ""

# end of deletion

res = ''.join([''.join(cross_word[row]) for row in range(n)])
print(res)
