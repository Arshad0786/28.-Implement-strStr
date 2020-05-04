class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if(len(needle) > len(haystack)):
            return -1
        for haystackIndex in range(len(haystack)-len(needle) + 1):
            if(haystack[haystackIndex] == needle[0]):
                for needleIndex in range(len(needle)):
                    if(haystack[haystackIndex + needleIndex] != needle[needleIndex]):
                        break
                else:
                    return haystackIndex    
        return -1
