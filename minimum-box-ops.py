class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        length 
        postfix = [0] * len(boxes)
        prefix = [0] * len(boxes)

        count = int(boxes[0])
        for i in range(1, len(boxes)):
            prefix[i] = prefix[i-1] + count
            count += int(boxes[i])

        count = int(boxes[-1])
        for i in range(len(boxes)-2, -1, -1):
            postfix[i] = postfix[i+1] + count
            count += int(boxes[i])

        res = [0] * len(boxes)
        for i in range(len(res)):
            res[i] = prefix[i] + postfix[i]

        return res
