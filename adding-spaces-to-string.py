class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.append(len(s))
        stringList = []

        startIndex = 0
        for index in spaces:
            stringList.append(s[startIndex: index])
            startIndex = index

        return ' '.join(stringList)
