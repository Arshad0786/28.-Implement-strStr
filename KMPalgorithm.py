class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if(len(needle) > len(haystack)):
            return -1
        FailureFunctionList = self.FailureFunction(needle)
        

    def FailureFunction(self, needle):
        prefixIndex = 0
        currentPos = 1
        FailureFunctionList = list()
        for i in range(len(needle)):
            FailureFunctionList.append(0)
        FailureFunctionList[0] = -1
        while(currentPos < len(needle)):
            if(needle[currentPos] == needle[prefixIndex]):
                FailureFunctionList[currentPos] = FailureFunctionList[currentPos - 1] + 1
                prefixIndex = prefixIndex + 1
            else:
                FailureFunctionList[currentPos] = -1
                prefixIndex = 0
            currentPos = currentPos + 1
        return FailureFunctionList
