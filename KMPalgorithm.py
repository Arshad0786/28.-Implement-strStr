class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if(len(needle) > len(haystack)):
            return -1
        FailureFunctionList = self.FailureFunction(needle)
        haystackIndex = 0
        needleIndex = 0

        while(haystackIndex < len(haystack)):
            if (haystack[haystackIndex] == needle[needleIndex]):
                needleIndex = needleIndex + 1
                haystackIndex = haystackIndex + 1
            else:
                if(needleIndex == 0):
                    haystackIndex = haystackIndex + 1
                    needleIndex = 0
                else:
                    needleIndex = FailureFunctionList[needleIndex - 1]
            if(needleIndex == len(needle)):
                return haystackIndex - len(needle)
        return -1

    def FailureFunction(self, needle):
        prefixIndex = 0
        currentPos = 1
        FailureFunctionList = list()
        for i in range(len(needle)):
            FailureFunctionList.append(0)  # initialize list
        FailureFunctionList[0] = 0
        while(currentPos < len(needle)):
            if(needle[currentPos] == needle[prefixIndex]):
                FailureFunctionList[currentPos] = prefixIndex + 1
                prefixIndex = prefixIndex + 1
                currentPos = currentPos + 1
            else:
                if(prefixIndex == 0):
                    FailureFunctionList[currentPos] = 0
                    currentPos = currentPos + 1
                else:
                    prefixIndex = FailureFunctionList[prefixIndex - 1]

        return FailureFunctionList

