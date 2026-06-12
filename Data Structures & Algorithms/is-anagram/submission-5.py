class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i],0)

        for i in range(len(t)):
            tMap[t[i]] = 1 + tMap.get(t[i],0)

        if sMap == tMap:
            return True
        return False
