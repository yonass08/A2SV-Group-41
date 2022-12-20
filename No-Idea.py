# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculateHappiness(arr, like, dislike):
    res = 0
    for num in arr:
        if num in like: res += 1
        elif num in dislike: res -= 1
    return res

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = map(int, input().split())
    like = set(map(int, input().split()))
    dislike = set(map(int, input().split()))
    print(calculateHappiness(arr, like, dislike))
