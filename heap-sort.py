#User function Template for python3

class Solution:
    def leftChild(self, i):
        return 2*i + 1
        
    def rightChild(self, i):
        return 2*i + 2
        
    def parent(self, i):
        return (i-1)//2
        
    def heapDown(self, arr, n, i):
        if 2 * i + 1 >= n:
            return
        
        max_idx = self.leftChild(i)
        if self.rightChild(i) < n and arr[self.rightChild(i)] > arr[self.leftChild(i)]:
            max_idx = self.rightChild(i)
            
        if arr[i] < arr[max_idx]:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            self.heapDown(arr, n, max_idx)
            
    def heapUP(self, arr, n, i):
        if i == 0:
            return
        
        parent = self.parent(i)
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            self.heapUp(arr, n, parent)
    
    
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        self.heapUp(arr, n, i)
        self.heapDown(arr, n, i)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n//2 -1, -1, -1 ):
            self.heapDown(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        for i in range(n-1, -1, -1 ):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapDown(arr, i, 0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
