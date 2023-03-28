class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [0]

        for i in range(len(arr)):
            if len(arr[i]) == len(set(arr[i])):
                self.backtrack(arr, 0, set(), i, res)

        return res[0]


    def backtrack(self, arr, count, distinct, idx, res):
        count += len(arr[idx])
        for ch in arr[idx]:
            distinct.add(ch)

        res[0] = max(res[0], count)
        print(distinct, res[0], count)

        for i in range(idx+1, len(arr)):
            if len(arr[i]) == len(set(arr[i])) and not distinct.intersection(arr[i]):
                self.backtrack(arr, count, distinct, i, res)

        count -= len(arr[idx])
        for ch in arr[idx]:
            distinct.remove(ch)


