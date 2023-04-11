"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapp = {}

        for emp in employees:
            mapp[emp.id] = emp


        def getImportantId(id):
            emp = mapp[id]
            if emp.subordinates == []:
                return emp.importance

            res = emp.importance
            for child in emp.subordinates:
                res += getImportantId(child)
            return res

        return getImportantId(id)
            

        


