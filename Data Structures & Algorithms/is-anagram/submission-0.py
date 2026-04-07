class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bucket1={}
        bucket2={}
        for i in range(len(s)):
           bucket1[s[i]] = bucket1.get(s[i], 0) + 1
           bucket2[t[i]] = bucket2.get(t[i], 0) + 1

        if(bucket1 == bucket2):
            return True
        else: 
            return False