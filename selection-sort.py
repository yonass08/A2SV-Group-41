#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        least = float('inf')
        result = i
        for j in range(i, len(arr)):
            if arr[j] < least:
                result = j
                least = arr[j]
        return result
        
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            index = self.select(arr, i)
            arr[i], arr[index] = arr[index], arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
