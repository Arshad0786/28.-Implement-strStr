class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if(len(needle) > len(haystack)):
            return -1
        SameFlag = False
        for haystackIndex in range(len(haystack)):
            if(haystack[haystackIndex] == needle[0]):
                SameFlag = True
                for needleIndex in range(len(needle)):
                    if(haystackIndex + needleIndex == len(haystack)):
                        return -1
                    if(haystack[haystackIndex + needleIndex] != needle[needleIndex]):
                        SameFlag = False
                if(SameFlag):
                    return haystackIndex
        return -1
