class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)

        for path in paths:
            dir_info = path.split()
            for i in range(1, len(dir_info)):
                contentIndex = dir_info[i].index('(') + 1
                filePath = f"{dir_info[0]}/{dir_info[i][:contentIndex-1]}" 
                content = dir_info[i][contentIndex: -1]
                contents[content] += [filePath]

        return [contents[content] for content in contents if len(contents[content]) > 1 ]


