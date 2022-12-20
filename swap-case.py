def swap_case(s):
    li = []
    for ch in s:
        if ch.islower():
            li.append(ch.upper())
        else:
            li.append(ch.lower())
        
    return ''.join(li)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
