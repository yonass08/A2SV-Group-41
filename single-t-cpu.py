class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(s,p,i) for i,(s,p) in enumerate(tasks)])
        tasks = tasks+[(float('inf'),0,0)]
        n = len(tasks)
        res, h = [], []
        j = far = 0
        for s, p, i in tasks:
            if s > far:
                if h:
                    while h and s > far:
                        tmp_p, tmp_i = heappop(h)
                        res.append(tmp_i)
                        far += tmp_p
                far = max(far, s)
            heappush(h, (p,i))
        return res