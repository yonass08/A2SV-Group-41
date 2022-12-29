class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        listResult = []
        source = '\n'.join(source)

        index = 0
        while index < len(source):
            if source[index: index+2] == '//':
                index += 2
                while index < len(source) and source[index] != '\n':
                    index += 1

            elif source[index: index+2] == '/*':
                index += 2
                while index < len(source) and source[index: index+2] != '*/':
                    index += 1
                index += 2
                
            else:
                listResult.append(source[index])
                index += 1
        
        listResult.append('\n')
        result = []
        nextLine = []

        for char in listResult:
            if char == '\n':
                line = ''.join(nextLine)
                if line:
                    result.append(line)
                nextLine = []
            else:
                nextLine.append(char)

        return result
      
